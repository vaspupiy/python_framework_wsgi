from os.path import join
from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры, передаваемые в шаблон
    :return:
    """
    file_path = join(folder, template_name)
    # Открываем шаблон по имени
    with open(file_path, encoding='utf-8') as f:
        # читаем
        template = Template(f.read())
    # рендерим шаблон с параметроми
    return template.render(**kwargs)
