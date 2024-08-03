#!/usr/bin/python3
"""module containing routes"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    ''' route /status. returns JSON with status OK '''
    return jsonify({'status': 'OK'})
