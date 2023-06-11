#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/29 16:03
# @Project  : pycharmlearningproject
# @File     : utils.py


# 判断是python2.0 还是3.0
try:
    from urlparse import urlparse
except  ImportError:
    from urllib.parse import urlparse

from flask import request, redirect, url_for,current_app


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    target_url = urlparse(request.host_url, target)
    return target_url.scheme in ('http', 'https') and ref_url.netloc == target_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
        return redirect(url_for(default, **kwargs))


def allow_file(filename):
    return  '.' in filename and filename.split('.',1)[1] in current_app.config['BLUELOG_ALLOWED_IMAGE_EXTENSIONS']