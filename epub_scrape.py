# This program scrapes a tree structured webbook, and parses it to a single file

import os


# Load page and crawl it

# Ask user which link he wants to scrape

# Scrape the pages to a single html file for further processing.

# Remove <any> tags

def rem_tag(text, start, end):
    start_i = 0
    end_i = 0
    start_i = text.find(start)
    end_i = text.find(end, start_i)
    if start_i == -1:
        return text, start_i
    text = text[:start_i] + text[end_i+2:]
    return text, start_i

def rem_all_tag(text, start, end):
    find = 0
    atext = text
    while find != -1:
        atext, find = rem_tag(atext, start, end)
    return atext

def ret_in_tag(text, start, end, start_pos):
    end_pos = text.find(end, start_pos)
    o_text = text[start_pos:] + text[:end_pos+2]
    return o_text

def extract_paragraph(page):
    in_text = page[page.find('<body>'):]
    out_text = ''
    for i in range(len(in_text)):
        if page[i] == '<':
            if page[i+1] == 'p' and page[i+2] == ' ':
                out_text += ret_in_tag(in_text, '<p', 'p>', i)
    return out_text

def test():
    inpath = 'test_page.html'
    outpath = 'test_out_page.html'
    with open(inpath, 'r') as page_source:
        page = page_source.read()
    with open(outpath, 'w') as outfile:
        out_source = extract_paragraph(page)
        # out_source = rem_all_tag(out_source, '<a', 'a>')
        outfile.write(out_source)
    print('Done.')
