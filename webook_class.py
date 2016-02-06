# Class framework implementation of webook

import requests
import tqdm
import os

class Webook():

    def __init__(url):
        self.url = url
