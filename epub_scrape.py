# This program scrapes a tree structured webbook, and parses it to a single file

# Load page and crawl it

# Ask user which link he wants to scrape

# Scrape the pages to a single html file for further processings.

# Remove <a> tags

text = """<p id="a_zen_master_st">A <a id="I_indexterm2_d1e919" class="indexterm"></a>Zen master of great <a id="I_indexterm2_d1e923" class="indexterm"></a>renown was visited by a young philosopher who had traveled
    from a distant land to meet him. The master agreed to see him because the
    philosopher came with high recommendations by his teachers. The two sat
    under a tree to converse and the subject hastily turned to what the master
    could teach the young philosopher. Recognizing the flame of youth, the
    master smiled warmly and started to describe his meditation techniques. He
    was cut short by the philosopher, who said: “Yes, I understand what you
    are talking about! We did a similar technique at the temple, but instead
    we used images to focus!”</>"""

def rem_tag(text, start, end):
    # These need deleting:
    # <a ... > and </a>
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

atext = rem_all_tag(text, '<a', 'a>')
print(atext)
