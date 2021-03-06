#!/usr/bin/env python

import os
import sys
import csv
from optparse import OptionParser

"""
This converts a download csv file from Discover.com
into a format suitable for my homegrown financial
accounting spreadsheet (an OpenOffice or LibreOffice Calc spreadsheet)

The converted csv file can be easily imported into
my spreadsheet.

Usage:
1. DOWNLOAD FROM DISCOVER AS .CSV FILE
2. in the downloaded directory, run discover.py passing in that downloaded
file, redirecting output to YYYYMMDD.csv
3. open the converted csv in OpenOffice and paste the cells into existing spreadsheet.

EXAMPLE:
...\data\statements>python \this\path\discover.py -f Discover-Statement-20110502.csv > 20110502.csv
"""

def convert(raw_date):
    """
    converts a standard mm/dd/yyyy date into simple integer form (mdd) ignoring the year

    Examples:
    '02/28/2011' --> 228
    '01/01/2011' --> 101
    '10/13/2012' --> 1013
    """

    pieces = raw_date.strip("'").split("/")
    return "".join([pieces[0].lstrip("0"),pieces[1]])

def guess_code(desc):
    """
    in my accounting spreadsheet each expense transaction requires a code
    (internal to the spreadsheet) such as G for groceries.
    I typically enter these manually after imported the generated csv file.
    This method predetermines the code for some transactions based on
    the description.

    TODO: externalize this mapping

    """
    
    code = ""
    g = "G" # grocery
    d = "D" # dining
    t = "T" # transportation
    
    if desc.count("WHOLE FOOD") > 0 or "WHOLEFDS" in desc:
        code = g
    elif desc.count("TOM THUMB STORE") > 0 or "RANDALLS" in desc:
        code = g
    elif "NATURAL GROCERS" in desc or "SPROUTS FARMERS" in desc:
        code = g
    elif desc.count("CENTRAL MARKET") > 0:
        code = g
    elif desc.count("PEI WEI") > 0:
        code = d
    elif desc.count("SHELL") > 0:
        code = t
    elif desc.count("7-ELEVEN") > 0:
        code = t
    elif "GUMBY CAFE" in desc:
        code = "JDL"
    elif "MATHNASIUM" in desc:
        code = "CLASS"
    elif "TORCHYS TACO" in desc:
        code = "D"
    return code
    
    
#def determine_input_file(inputdate):
    # first look for Discover-Statement-YYYYMMDD.csv
    # else look for Discover-RecentActivity-YYYYMMDD.csv
    # TODO
        

# __________________________________
#
# M A I N
# __________________________________

if __name__ == "__main__":

    version = "1.0"

    usage = "%prog [options]\n" + \
            "Version " + version + "\n"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="inputfile", help="the downloaded csv file")
    #parser.add_option("-d", "--date", dest="inputdate", help="the date of the latest file in YYYYMMDD format")
    (op, args) = parser.parse_args()
    inputfile = op.inputfile
    inputdate = None
    #inputdate = op.inputdate
    if not inputfile and not inputdate:
        parser.error("missing required option; -h for help")
        
    """
    Sample input lines.
    trans date,post date,desc,amount,category
    11/20/2011,11/20/2011,"INTERNET PAYMENT - THANK YOU",-4239.65,Payments and Credits
    11/20/2011,11/20/2011,"WHOLEFDS",178.13,Supermarkets
    11/25/2011,11/25/2011,"RECREATION.GOV BALLSTON SPA NY",27.0,Government Services
    

    logic 1: if a line contains a name "INTERNET PAYMENT..." do not include in the output file
    logic 2: convert other lines to:

    date,description,amount[,,code]

    where date is of the form MDD (example 103 = january 3, 1025 = oct 25; ignore the year part)
    
    Sample output (using above input):
    1120,"WHOLEFDS",178.13,"","",G
    1125,"RECREATION.GOV BALLSTON SPA NY",27.0
    """
    
    # read file
    reader = csv.reader(open(inputfile,'rb'), delimiter=',', quotechar='"')
    lines = []
    for row in reader:
        # skip blank lines
        if len(row) == 0:
            continue
            
        # skip header row
        if "Trans. Date" in row[0]:
            continue
        else:
            raw_date = row[0].strip()

        # skip payments made
        raw_desc = row[2]
        if raw_desc.startswith("INTERNET PAYMENT"):
            continue
            
        raw_amt = row[3]
        
        date = convert(raw_date)
        desc = raw_desc.strip("'")
        amt = raw_amt.strip("'")
        code = guess_code(desc)
        
        lines.append((date,desc,amt,code))
    
    # generate output sorted ascending by date
    for line in sorted(lines, key=lambda tuple: tuple[0]):
        if line[3]:
            print('%s,"%s",%s,"","",%s' % (line[0],line[1],line[2],line[3]))
        else:
            print('%s,"%s",%s' % (line[0],line[1],line[2]))
            
