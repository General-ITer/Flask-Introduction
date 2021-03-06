from  flask import  Flask
from app.settings import conf
from app.ext import  init_ext
from app.views import  init_blue

def create_app(env_name):
    #做一个校验
    if not env_name in conf.keys():
        raise Exception('您的环境名有问题')

    app = Flask(__name__)
    #各种配置
    app.config.from_object(conf.get(env_name))
    #注册第三方插件
    init_ext(app)
    init_blue(app)
    #注册蓝图
    return  app