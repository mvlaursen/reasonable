import csv
import os
import sys

def write_li(article, output_file):
    output_file.write("            <li><a href='" + article['href'] + "'>" + article['title'] + "</a> -- " + article['author'] + ": <i>" + article['subtitle'] + "</i></li>")

def write_html(articles, output_file):
    output_file.write("<html>")
    output_file.write("    <body>")
    output_file.write("        <ul>")

    for article in articles:
        write_li(article, output_file)

    output_file.write("        </ul>")
    output_file.write("    </body>")
    output_file.write("/<html>")
    
def main():
    if len(sys.argv) != 3:
        print("usage: " + os.path.basename(sys.argv[0]) + " input-filepath.csv output-filepath.html")
    else:
        input_filepath = sys.argv[1]
        output_filepath = sys.argv[2]

        with open(input_filepath, 'r') as input_file:
            articles = []
            csv_reader = csv.DictReader(input_file)
            for row in csv_reader:
                article = {}
                article['author'] = row['article-author']
                article['href'] = row['article-link-href']
                article['title'] = row['article-title']
                article['subtitle'] = row['article-subtitle']
                articles.append(article)

            with open(output_filepath, 'w') as output_file:
                write_html(articles, output_file)

if __name__ == "__main__":
    main()