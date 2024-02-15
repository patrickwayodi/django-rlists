"""
This program downloads FIDE Rating Lists (XML) from the fide.com website.

python-3.9.14-docs-html/tutorial/inputoutput.html#saving-structured-data-with-json

software/cpython/cpython-3.11.5/Lib/xml/etree/ElementTree.py
"""


import json
import os
import subprocess

from io import StringIO
from urllib.request import urlopen


def fetch_rating_lists(file_urls):

    print("\nStarting fetch_rating_lists() \n")

    print("\ncd ../data: \n", type(file_urls))
    subprocess.run(["cd", "../data")

    print("\nType file_urls: \n", type(file_urls))

    frlist_counter = 0

    while frlist_counter < 3 :

        # file_url = file_urls[frlist_counter][-25:]
        file_url = file_urls[frlist_counter][1:58]

        print("\nfile_url: \n", file_url)
        print("\nType file_url: \n", type(file_url))

        print("\nFetch file using Wget: \n")

        # python-3.9.14-docs-html/library/subprocess.html#module-subprocess
        # wget --no-clobber --wait=45 --random-wait
        # output_path = "../static/rlists/frl/" + file_name
        # subprocess.run(["ls", "-l"])
        # subprocess.run(["wget", "--output-file", output_path, file_url])
        subprocess.run(["wget", file_url])

        print("\nRating lists downloaded so far: \n", frlist_counter)

        frlist_counter = frlist_counter + 1

    print("\nEnding fetch_rating_lists() \n")


def fetch_file_urls():

    print("\nStarting fetch_file_urls() \n")

    input_path = "../static/rlists/json/fide_rating_lists.json"

    with open(input_path, "r", encoding="utf-8") as input_file:
        rating_lists_input = input_file.read()

    print("rating_lists_input: \n", rating_lists_input)
    print("\nType rating_lists_input: \n", type(rating_lists_input))

    rating_lists = rating_lists_input.replace(" ", "").replace("\n", "")

    print("rating_lists: \n", rating_lists)
    print("\nType rating_lists: \n", type(rating_lists))

    file_urls_values = StringIO()

    # python-3.9.14-docs-html/tutorial/inputoutput.html#saving-structured-data-with-json
    # file_urls = json.dumps(rating_lists)
    json.dump(rating_lists, file_urls_values)

    file_urls = file_urls_values.getvalue().replace("\\", "")

    print("\nfile_urls \n", file_urls)
    print("\nType file_urls: \n", type(file_urls))

    # file_urls_list = list(file_urls)
    file_urls_list = file_urls.replace('"[', "").split(",")

    print("\nfile_urls_list \n", file_urls_list)
    print("\nType file_urls_list: \n", type(file_urls_list))

    print("\nfile_urls_list[0] \n", file_urls_list[0])
    print("\nfile_urls_list[1] \n", file_urls_list[1])
    print("\nfile_urls_list[133] \n", file_urls_list[133])

    print("\n\nEnding fetch_file_urls() \n")

    return file_urls_list


if __name__ == '__main__':

    print("\n\nStarting download_frlists.py \n")

    file_urls = fetch_file_urls()
    print("\nType file_urls: \n", type(file_urls))

    fetch_rating_lists(file_urls)

    print("\n\nEnding download_frlists.py \n")

