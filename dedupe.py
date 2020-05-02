#!/usr/bin/python

from urllib import urlopen
from optparse import OptionParser

"""
Extracts the songs from a setlist.fm page
and displays them in alphabetical order

USAGE EXAMPLE:
python setlistalpha.py -u http://www.setlist.fm/setlist/rush/2010/superpagescom-center-dallas-tx-1bd5c1b8.html
"""

if __name__ == "__main__":
    
    version = "1.0"
    usage = "%prog [options]\n" + \
            "Version " + version + "\n"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="inputfile", help="the html file")
    parser.add_option("-u", "--url", dest="inputurl", help="the url of the html")
    (op, args) = parser.parse_args()
    
    if op.inputfile:
        with open(op.inputfile) as f:
            data = f.readlines()
            songs = [x.strip() for x in data if len(x) > 0 and not x.startswith("Total:")]
            deduped = sorted(list(set(songs)))
     
            print("\n".join(deduped))

