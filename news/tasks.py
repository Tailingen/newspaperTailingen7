from celery import shared_task
import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news.models import Post, Category

@shared_task
def hello():
    print("Hello, world!")


@shared_task
def mail_spam():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': 'http://127.0.0.1:8000',
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email='Tailingen1@yandex.ru',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def mail_new():
    post = Post.save(commit=False)
    html_content = render_to_string(
        'news/post_created.html',
        {
            'post': post,
            'text': post.preview,
            'link': f'http://127.0.0.1:8000/news/{post.pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'{post.title}',
        body=post.text,
        from_email='Tailingen1@yandex.ru',
        to=Category.subscribers
    )
    msg.attach_alternative(html_content, "text/html")

    msg.send()