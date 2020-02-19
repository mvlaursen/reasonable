import csv
import os
import sys

SCRAPER_AUTHOR_KEY = 'article-author'
SCRAPER_HREF_KEY = 'article-link-href'
SCRAPER_ORDER_KEY = '\ufeffweb-scraper-order'
SCRAPER_SUBTITLE_KEY = 'article-subtitle'
SCRAPER_TIME_KEY = 'article-datetime'
SCRAPER_TITLE_KEY = 'article-title'

AUTHOR_KEY = 'author'
HREF_KEY = 'href'
ORDER_KEY = 'order'
SUBTITLE_KEY = 'subtitle'
TIME_KEY = 'time'
TITLE_KEY = 'title'

def write_li(article, output_file):
    output_file.write("        <li><a href='" + article[HREF_KEY] + "'>"
        + article[TITLE_KEY] + "</a> -- "
        + article[AUTHOR_KEY] 
        + ": <i>" + article[SUBTITLE_KEY] + "</i></li>\n")

def write_html(articles, output_file):
    output_file.write("<!doctype html>\n")
    output_file.write("<html lang='en'>\n")
    output_file.write("<head>\n")
    output_file.write("    <meta charset='utf-8'>\n")
    output_file.write("</head>\n")
    output_file.write("<body>\n")
    output_file.write("    <ul>\n")

    for article in articles:
        write_li(article, output_file)

    output_file.write("    </ul>\n")
    output_file.write("</body>\n")
    output_file.write("/<html>\n")
    
def main():
    if len(sys.argv) != 3:
        print("usage: " + os.path.basename(sys.argv[0]) + " input-filepath.csv output-filepath.html")
        print("    input-file.csv: Path to an input file created by the Firefox Web Scraper extension.")
        print("    output-filepath.csv: An HTML file listing the articles in an unordered, bulleted list.")
    else:
        input_filepath = sys.argv[1]
        output_filepath = sys.argv[2]

        with open(input_filepath, 'r', encoding='utf-8') as input_file:
            articles = []
            csv_reader = csv.DictReader(input_file)
            for row in csv_reader:
                article = {}
                article[AUTHOR_KEY] = row[SCRAPER_AUTHOR_KEY]
                article[HREF_KEY] = row[SCRAPER_HREF_KEY]
                article[ORDER_KEY] = row[SCRAPER_ORDER_KEY]
                article[SUBTITLE_KEY] = row[SCRAPER_SUBTITLE_KEY]
                article[TIME_KEY] = row[SCRAPER_TIME_KEY]
                article[TITLE_KEY] = row[SCRAPER_TITLE_KEY]
                articles.append(article)

            articles.sort(key = lambda i: (i[ORDER_KEY]), reverse=True)

            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                write_html(articles, output_file)

if __name__ == "__main__":
    main()