#Objective: Navigate file paths to access html documents prior to feeding into html parser
from html_parser import import_data
from bs4 import BeautifulSoup, NavigableString, Tag
from pathlib import Path
import os


cwd = Path('.')
#local location that will sync with where user downloads data
data = Path('/Users/nick/Documents/cs506/project')

# full list of directory's with html files
#531 total
full_set = list(data.glob('**/*.html'))
first_10 = full_set[:10]
file = first_10[0]
#attempting to link path to Eric's import data functions
#testing each function
test = import_data(str(first_10[0]))  # creates populated soup object based on file path










#terms from grab section
start_terms = ['ITEM', '1A.', 'RISK', 'FACTORS']
end_terms = ['ITEM', '1B.', 'UNRESOLVED', 'STAFF', 'COMMENTS']

def grab_section_text(soup_object, start_terms, end_terms):
   
    section_text = []  # Populated with text found in specified 10-K section
    within_item_1A = False
    for tag in soup_object.html.strings:  # Search each element in the tree
        #import pdb;pdb.set_trace()
        if not within_item_1A:
            criteria = 0
            # String must contain "ITEM', '1A.', 'RISK', & 'FACTORS'
            for term in start_terms:
                if isinstance(tag, NavigableString):
                    if term in tag.upper():
                        criteria += 1
                elif isinstance(tag, Tag):
                    if term in tag.text.upper():
                        criteria += 1
            if criteria == len(start_terms):
                # Located the start of 'Item 1A: Risk Factors'
                within_item_1A = True
                print('Tag is :',tag)
                section_text.append(tag)
                
                continue

        if within_item_1A:
            section_text.append(tag)  # Collect strings in section of interest
            criteria = 0
            # String must contain "ITEM', '1B.', 'UNRESOLVED', 'STAFF, & 'COMMENTS'
            for term in end_terms:
                if isinstance(tag, NavigableString):
                    if term in tag.upper():
                        criteria += 1
                elif isinstance(tag, Tag):
                    if term in tag.text.upper():
                        criteria += 1
            if criteria == len(end_terms):
                # Located the start of 'Item 1B: Unresolved Staff Comments'
                within_item_1A = False
                break
    return section_text