# Executable of weebook
#
# Where applicable, the program provides useful default, which shows, how to
# use the function.

from webook_class import Webook

def main():
    """
    Docstring placeholder.
    """

    # Insert the index of the page you want to download.
    # url = 'http://something.com/or/other/index.html'
    # If you want to download from the internet, leave <path> empty.
    # You can use and existing html file. In this case leave <url> empty
    # and write the absolute path to file.
    # path = '/home/user/file.html'
    url = 'http://www.paulgraham.com/articles.html'
    path = ''
    book = Webook(url, path)

    # Prints all the links on the index page. Uncomment it to determine wich
    # ones you don't need, then comment it after, for brevity.
    # book.print_links()

    # Write in the list below some unique marker of the links you don't want.
    # unwanted = ['mailto', '/', 'http']
    unwanted = ['mailto', 'rss', 'http', 'index']
    book.sort_links(unwanted)
    book.print_links()

    book.download_book()

    # Write in the list below, which html tags you want the program to remove.
    tags = ['script', 'header', 'footer', 'select', 'area', 'a', 'font', 'link']
    book.remove_tags(tags)

    # book.remove_tags_extra is for removing non-symmetric tags like the
    # examples below. It's for fine tuning the html file before converting
    # with calibre or the like.
    book.remove_tags_extra('<div class="extra-footer"', '/div>')
    book.remove_tags_extra('<div id="menu"', '/div>')
    book.remove_tags_extra('<ul id="menu-right"', '/ul>')

    # Write in the export path. Be careful, if the file exists, it will
    # overwrite it.
    output = 'paul_graham.html'
    book.export(output)


if __name__ == '__main__':
    main()
