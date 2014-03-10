# -*- coding: utf-8 -*-
import os
import shutil
import sys


sys.path.insert(0, os.getcwd())

from processors import default
from settings import *
from urls import urls


# Clean up previous builds
try:
	shutil.rmtree(BUILD_DIR)
except OSError:
	pass

# Add static files to the build
shutil.copytree(STATIC_DIR, BUILD_DIR)

for url, params in urls.items():
	print '\033[92m/%s\033[0m' % url
	params.get('processor', default)(url, params['template'], params.get('data', {}))