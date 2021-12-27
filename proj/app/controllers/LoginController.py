from masonite.controllers import Controller
from masonite.views import View


class LoginController(Controller):
    def show(self, view: View):
        return view.render('login.html')
#        return view('login.html')
