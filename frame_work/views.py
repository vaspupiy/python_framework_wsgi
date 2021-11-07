"""Модуль, содержащий контроллеры веб-приложений"""
import quopri

from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


class Task:
    def __call__(self, request):
        return '200 OK', render('task.html')


class Form:
    def __call__(self, request):
        with open('bd.txt', 'a', encoding='utf-8') as f:
            f.write('\n\nновая запись: \n')
            for k, v in request['data'].items():
                val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
                val_decode_str = quopri.decodestring(val).decode('UTF-8')
                str_line = f'{k}: {val_decode_str}\n'
                f.write(str_line)
        return '200 OK', render('form.html')
