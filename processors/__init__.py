# -*- coding: utf-8 -*-
import codecs
import os

from jinja2 import Environment, FileSystemLoader
from settings import *


def default(url, template, data):
	render_to(template, os.path.join(os.path.join(BUILD_DIR, url), 'index.html'), {})

# Create page for each item in data['items']
def details(url, template, data):
	for item in data['items']:
		render_to(template, os.path.join(BUILD_DIR, url.replace('<id>', str(item['id'])), 'index.html'), item)

def items_list(url, template, data):
	render_to(template, os.path.join(BUILD_DIR, url, 'index.html'), data)

# Render template to filename
def render_to(template, filename, context):
	env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

	# Check if path exists and create if no
	if not os.path.exists(locals().setdefault('path', os.path.split(filename)[0])):
		os.makedirs(locals().get('path'))

	html = codecs.open(filename, 'w', encoding='utf-8')
	html.write(env.get_template(template).render(**(context or {})))
	html.close()