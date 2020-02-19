import csv
import os
import sys

# These are the keys that the Firefox Web Scraper extension uses.
# Some of them may come from Reason's HTML.
AUTHOR_KEY = 'article-author'
HREF_KEY = 'article-link-href'
ORDER_KEY = '\ufeffweb-scraper-order'
SUBTITLE_KEY = 'article-subtitle'
TIME_KEY = 'article-datetime'
TITLE_KEY = 'article-title'

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
                article[AUTHOR_KEY] = row[AUTHOR_KEY]
                article[HREF_KEY] = row[HREF_KEY]
                article[ORDER_KEY] = row[ORDER_KEY]
                article[SUBTITLE_KEY] = row[SUBTITLE_KEY]
                article[TIME_KEY] = row[TIME_KEY]
                article[TITLE_KEY] = row[TITLE_KEY]
                articles.append(article)

            articles.sort(key = lambda i: (i[ORDER_KEY]), reverse=True)
            articles = filter(lambda i: (not i[TITLE_KEY].startswith(("Brickbat", "Review"))), articles)

            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                write_html(articles, output_file)

if __name__ == "__main__":
    main()