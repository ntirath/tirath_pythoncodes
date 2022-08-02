# Assignment 44 : Check URL in string: Author Tirath

import re
def find_url(string):
    url_format=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url_found= re.findall(url_format,string)
    return [x[0] for x in url_found]

string1 = input("Enter the string with url :")
print("Exisiting Url in string: ", find_url(string1))