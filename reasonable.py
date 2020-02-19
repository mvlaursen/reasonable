import csv
import os
import sys

def write_li(article, output_file):
    output_file.write("        <li><a href='" + article['href'] + "'>" + article['title'] + "</a> -- " + article['author'] + ": <i>" + article['subtitle'] + "</i></li>\n")

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
                article['author'] = row['article-author']
                article['href'] = row['article-link-href']
                article['title'] = row['article-title']
                article['subtitle'] = row['article-subtitle']
                articles.append(article)

            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                write_html(articles, output_file)

if __name__ == "__main__":
    main()