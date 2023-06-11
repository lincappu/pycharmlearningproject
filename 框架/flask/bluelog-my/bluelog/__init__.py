#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/28 21:16
# @Project  : pycharmlearningproject
# @File     : __init__.py.py

import logging
import os

from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFError

from settings import config

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_logging(app)
    register_errors(app)


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

    # stream_handler = logging.handlers.StreamHandler()
    stream_handler = logging.handlers.default_handler()
    stream_handler.setLevel(logging.INFO)

    file_handler = logging.handlers.RotatingFileHandler(os.path.join(basedir, 'logs/bluelog.log'),
                                                        maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    mail_handler = logging.handlers.SMTPHandler(mailhost=app.config['MAIL_SERVER'],
                                                fromaddr=app.config['MAIL_USERNAME'],
                                                toaddrs=app.config['ADMIN_EMAIL'],
                                                subject='Bluelog Application Error',
                                                credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))

    mail_handler.setFormatter(request_formatter)
    mail_handler.setLevel(logging.INFO)

    if not app.debug:
        app.logger.addHandler(mail_handler)
        app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)


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
