from apistar import App, Route, http
import proselint


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def lint(request: http.Request) -> dict:
    return proselint.tools.lint(request.body.decode('utf-8'))


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/', method='POST', handler=lint)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)