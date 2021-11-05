from views import Index, About, Task

# Набор привязок: путь-контроллер

routes = {
    '/': Index(),
    '/about/': About(),
    '/task/': Task(),
}
