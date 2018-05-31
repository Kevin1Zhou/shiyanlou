#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

class File_Handler():
    files_path = os.path.abspath(os.path.dirname(__name__)) + '/' + '..' +     '/files'
    def read_all_files():
        file_content = {}
        files_list = os.listdir(self.files_path)
        for filename in files_list:
            file_path = os.path.join(self.files_path, filename)
            with open(file_path) as f:
                file_content[filename[0:-5]] = json.loads(f.read())
        return file_content
