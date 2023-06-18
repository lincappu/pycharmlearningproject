#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/28 21:16
# @Project  : pycharmlearningproject
# @File     : __init__.py.py

import logging
import os
from logging.handlers import  RotatingFileHandler, SMTPHandler

import click
from bluelog.blueprints.auth import auth_bp
from bluelog.extensions import bootstrap, db, login_manager, csrf, ckeditor, mail, moment, toolbar, migrate
from bluelog.models import Admin
from bluelog.settings import config
from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFError

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    register_logging(app)
    register_errors(app)
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app

# 要记录logrecord额外的参数,这就要重新实现Formatter
def register_logging(app):
    class RequestFormatter(logging.Formatter):

        def format(self, record):
            record.rul = request.url
            record.remote_addr = request.remote_addr
            return super(RequestFormatter, self).format(record)

    request_formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    # stream_handler = logging.handlers.default_handler()
    stream_handler.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(os.path.join(basedir, 'logs/bluelog.log'),
                                       maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    mail_handler = SMTPHandler(mailhost=app.config['MAIL_SERVER'],
                               fromaddr=app.config['MAIL_USERNAME'],
                               toaddrs=['ADMIN_EMAIL'],
                               subject='Bluelog Application Error',
                               credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))

    mail_handler.setFormatter(request_formatter)
    mail_handler.setLevel(logging.INFO)

    if not app.debug:
        app.logger.addHandler(mail_handler)
        app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def bad_request(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 400


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='create and drop')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables')

        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=False, help='输入admin的用户名')
    @click.option('--password', prompt=True, confirmation_prompt=True, hide_input=True, help='输入密码')
    def init(username, password):
        click.echo('init database.....')
        db.create_all()
        admin = Admin.query.first()
        print(admin)
        if admin is not None:
            click.echo('admin already exists update....')
            admin.username = username
            admin.password = password
        else:
            click.echo('crealte admin account')
            admin = Admin(
                username=username,
                blog_title='Bluelog',
                blog_sub_title="No, I'm the real thing.",
                name='Admin',
                about='Anything about you.'
            )
            admin.password = password
            db.session.add(admin)

        db.session.commit()
        click.echo('admin create Done')
