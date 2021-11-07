from views import Index, About, Task, Form

# Набор привязок: путь-контроллер

routes = {
    '/': Index(),
    '/about/': About(),
    '/task/': Task(),
    '/form/': Form(),
}
