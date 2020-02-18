import csv
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("usage: " + os.path.basename(sys.argv[0]) + " input-filepath.csv output-filepath.html")
    else:
        input_filepath = sys.argv[1]

        with open(input_filepath, 'r') as input_file:
            csv_reader = csv.DictReader(input_file)
            print ("<html><body><ul>")
            for row in csv_reader:
                print("<li><a href='" + row['article-link-href'] + "'>" + row['article-title'] + "</a> -- " + row['article-author'] + ": <i>" + row['article-subtitle'] + "</i></li>")
            print("</ul>")
            print("</body></html>")

if __name__ == "__main__":
    main()