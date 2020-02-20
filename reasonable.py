import csv
import os
import sys
import webbrowser

# These are the keys that the Firefox Web Scraper extension uses.
# Some of them may come from Reason's HTML.
AUTHOR_KEY = 'article-author'
HREF_KEY = 'article-link-href'
ORDER_KEY = '\ufeffweb-scraper-order'
SUBTITLE_KEY = 'article-subtitle'
TIME_KEY = 'article-datetime'
TITLE_KEY = 'article-title'

def maybeLinkAuthor(author):
    if author == "Elizabeth Nolan Brown":
        return "<a href='https://www.quora.com/profile/Elizabeth-Nolan-Brown'>Elizabeth Nolan Brown</a>"
    elif author == "Jacob Sullum":
        return "<a href='https://www.quora.com/profile/Jacob-Sullum-1'>Jacob Sullum</a>"
    elif author == "John Stossel":
        return "<a href='https://www.quora.com/topic/John-Stossel'>John Stossel</a>"
    elif author == "Katherine Mangu-Ward":
        return "<a href='https://www.quora.com/profile/Katherine-Mangu-Ward'>Katherine Mangu-Ward</a>"
    elif author == "Nick Gillespie":
        return "<a href='https://www.quora.com/profile/Nick-Gillespie-14'>Nick Gillespie</a>"
    else:
        return author

def writeLi(article, output_file):
    output_file.write("        <li><a href='" + article[HREF_KEY] + "'>"
        + article[TITLE_KEY] + "</a> &ndash;&ndash; "
        + maybeLinkAuthor(article[AUTHOR_KEY])
        + ": <i>" + article[SUBTITLE_KEY] + "</i></li>\n")

def writeHtml(articles, output_file):
    output_file.write("<!doctype html>\n")
    output_file.write("<html lang='en'>\n")
    output_file.write("<head>\n")
    output_file.write("    <meta charset='utf-8'>\n")
    output_file.write("</head>\n")
    output_file.write("<body>\n")
    output_file.write("    <ul>\n")

    for article in articles:
        writeLi(article, output_file)

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
                writeHtml(articles, output_file)

            webbrowser.get().open(output_filepath)

if __name__ == "__main__":
    main()