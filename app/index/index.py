from flask.views import MethodView


class IndexView(MethodView):
    def get(self):
        return '<hr />1'
