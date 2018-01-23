from flask_classy import FlaskView
from flask_login import login_required
from stock.email import send_mail


class IndexView(FlaskView):
    route_base = '/'

    @login_required
    def home(self):
        return 'I am OK'

    def login(self):
        return 'login'

    def error(self):
        1 / 0

    def email(self):
        send_mail('15234134080@163.com', '账户激活', 'main/email',
                  username='xiaoming')
        return '邮件已发送'
