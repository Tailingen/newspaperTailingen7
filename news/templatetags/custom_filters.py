from django import template


register = template.Library()


@register.filter()
def censor(value: str):
    variants = ['тормоз', 'собака', 'дурак', 'школьник', 'гузно', 'редиска']
    ln = len(variants)
    filtred_message = ''
    string = ''
    pattern = '*'
    for i in value:
        string += i

        flag = 0
        for j in variants:
            if not string in j:
                flag += 1
            if string == j:
                filtred_message += string[0] + (pattern * (len(string) - 1))
                flag -= 1
                string = ''

        if flag == ln:
            filtred_message += string
            string = ''

    if string != '' and string not in variants:
        filtred_message += string
    elif string != '':
        filtred_message += string[0] + (pattern * (len(string) - 1))

    return filtred_message