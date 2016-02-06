# Class framework implementation of webook

import requests
import tqdm
import os

class Webook():

    def __init__(self, url, path):
        self.url = url
        if path != '':
            self.path = path
            self.text = self._import()

    def print_links(self):
        pass

    def sort_links(self, unwanted):
        pass

    def remove_tags(self, tags):
        pass

    def export(self, output):
        pass

    def _import(self):
        pass
