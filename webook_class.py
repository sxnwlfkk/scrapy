# Class framework implementation of webook

import requests
import tqdm
import os
from bs4 import BeautifulSoup


class Webook():

    def __init__(self, url, path):
        if url != '':
            self.url = url
            self.index = self._download_page(self.url)
            self.links = self._extract_links()
            self.text = ''
        elif path != '':
            self.path = path
            self.text = self._import()
            self.links = ''
        else:
            print('No link or path provided. Sry. :(')

    def print_links(self):
        if self.links == '':
            print('No links be here.')
        else:
            for link in self.links:
                print(link)

    def sort_links(self, unwanted):
        good_links = []
        unw_expr = []

        for link in self.links:
            counter = 0
            for excl in unwanted:
                if excl not in link:
                    counter += 1
            if counter == len(unwanted):
                good_links.append(link)
        self.links = good_links

    def remove_tags(self, tags):
        for tag in tags:
            start = '<' + tag
            end = '/' + tag + '>'
            find = 0
            while find != -1:
                find = self._rem_tag(start, end)

    def remove_tags_extra(self, start, end):
        find = 0
        while find != -1:
            find = self._rem_tag(start, end)

    def _rem_tag(self, start, end):
        start_i = 0
        end_i = 0
        start_i = self.text.find(start)
        end_i = self.text.find(end, start_i)
        if start_i == -1:
            return start_i
        self.text = self.text[:start_i] + self.text[end_i+len(end):]
        return start_i

    def export(self, output):
        with open(output, 'w') as outfile:
            outfile.write(self.text)
            print("Write done.")

    def download_book(self):
        url_stump = self.url[:self.url.find('articles.html')]
        for link in tqdm.tqdm(self.links):
            url_usable = url_stump + link
            page = self._download_page(url_usable)
            self.text += page
        print("Downloaded {0} files.".format(len(self.links)))

    def _import(self):
        with open(self.path, 'r') as page_source:
            page = page_source.read()
            return page

    def _extract_links(self):
        links = []
        pointer = 0
        link, pointer = self._find_next_link(self.index, pointer)
        while pointer != -1:
            if '#' not in link:
                if link != links:
                    links.append(link)
            link, pointer = self._find_next_link(self.index, pointer+1)
        return links

    def _download_page(self, url):
        r = requests.get(url)
        page_source = r.text
        return page_source

    def _find_next_link(self, source, start):
        first = '<a href="'
        last = '"'
        first_pos = source.find(first, start)
        last_pos = source.find(last, first_pos+len(first))
        target = source[first_pos + len(first):last_pos]
        return target, first_pos
