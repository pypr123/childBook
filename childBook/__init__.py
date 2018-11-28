from flask import Flask
from models import db,migrate
from views import admin
from flask_apscheduler import APScheduler

def creat_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app,db)
    admin.init_app(app)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    return app



def register_blueprint(app):
    from .web import web
    app.register_blueprint(web)
