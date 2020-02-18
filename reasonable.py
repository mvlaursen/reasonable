import csv
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("usage: " + os.path.basename(sys.argv[0]) + " <.csv file>")
    else:
        filename = sys.argv[1]
        print("Gonna go to town on: " + filename)

        with open(filename, 'r') as csvfile:
            rows = []

            csvreader = csv.DictReader(csvfile)
            print ("<html><body><ul>")
            for row in csvreader:
                print("<li><a href='" + row['article-link-href'] + "'>" + row['article-title'] + "</a> -- " + row['article-author'] + ": <i>" + row['article-subtitle'] + "</i></li>")
            print("</ul>")
            print("</body></html>")

if __name__ == "__main__":
    main()