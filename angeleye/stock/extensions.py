from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_uploads import patch_request_class

# 创建相关对象
db = SQLAlchemy()
mail = Mail()
moment = Moment()
migrate = Migrate(db=db)
login_manager = LoginManager()
# 图片上传
photos = UploadSet('photos', IMAGES)


# 完成相关初始化
def config_extensions(app):
    db.init_app(app)
    mail.init_app(app)
    # 本地化日期和时间
    moment.init_app(app)
    migrate.init_app(app)
    # 用户登录认证
    login_manager.init_app(app)
    # 需要登录才能访问的提示信息
    login_manager.login_message = '需要登录才可访问'
    # 需要登录的视图函数
    login_manager.login_view = 'IndexView:login'
    # 设置session的保护级别，None：禁用，basic：基本（默认），strong：严格
    login_manager.session_protection = 'strong'

    # 图片上传
    configure_uploads(app, photos)
    # 指定上传文件的大小，默认64M，None：采用配置选项MAX_CONTENT_LENGTH的值
    patch_request_class(app, size=None)
