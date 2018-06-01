#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

class File_Handler():
    files_path = os.path.abspath(os.path.dirname(__name__)) + '/' + '..' +     '/files'
    def __init__(self):
        self.files = self.read_all_files()
    def read_all_files(self):
        file_content = {}
        files_list = os.listdir(self.files_path)
        for filename in files_list:
            file_path = os.path.join(self.files_path, filename)
            with open(file_path) as f:
                file_content[filename[0:-5]] = json.loads(f.read())
        return file_content
    def get_title_list(self):
        title_list = []
        for item in self.files.values():
            title_list.append(item.get('title'))
        return title_list
    def get_by_filename(self,filename):
        return self.files.get(filename)
file_handler = File_Handler()
@app.route('/')
def index():
    return render_template('index.html', title_list = file_handler.get_title_list())

@app.route('/files/<filename>')
def file(filename):
    file_item = file_handler.get_by_filename()
    if file_item is None:
        abort(404)
    else:
        return render_template('file.html', file_item = file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()


