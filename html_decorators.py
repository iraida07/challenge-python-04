def div(func):
    def add_div(text):
        return '<div>' + func(text) + '</div>'
    return add_div


def article(func):
    def add_article(text):
        return '<article>' + func(text) + '</article>'
    return add_article

def p(func):
    def add_p(text):
        return '<p>' + func(text) + '</p>'
    return add_p


@div
#@article
#@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

