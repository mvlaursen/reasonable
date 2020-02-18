import csv
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("usage: " + os.path.basename(sys.argv[0]) + " <.csv file>")
    else:
        print("Gonna go to town on: " + sys.argv[1])

if __name__ == "__main__":
    main()