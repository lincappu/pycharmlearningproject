# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import asyncio
import functools
import inspect
import pytest

from inspect import isasyncgenfunction


def _is_coroutine(obj):
	'''检查 obj 是不是一个异步协程'''
	return asyncio.iscoroutinefunction(obj) or inspect.isasyncgenfunction(obj)


def pytest_config(config):
	config.addinivalue_line(
		"markers",
		"asyncio: "
		"mark the test as a coroutine, it will be "
		"run using an asyncio event loop",
	)


