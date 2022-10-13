# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  pathlib
import  yaml

BASE_DIR=pathlib.Path(__file__).parent.parent
CONFIG_PATH=BASE_DIR/'config'/'polls.yaml'

def get_config(path):
	with open(path, 'r') as f:
		config=yaml.load(f,Loader=yaml.FullLoader)
	return config

config = get_config(CONFIG_PATH)
print(config)