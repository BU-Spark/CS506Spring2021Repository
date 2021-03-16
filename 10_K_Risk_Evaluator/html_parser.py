"""
<CS506 Project: 10-K Risk Evaluator>.

Written by Evie Wan, Nicholas Mosca, Eric South
"""
from bs4 import BeautifulSoup, NavigableString, Tag
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import regexp_tokenize
nltk.download('wordnet')


def import_data(html_file):
    """
    Convert an HTML file into a BeautifulSoup object.

    :param html_file: an HTML file.
    :return soup: a BeautifulSoup HTML tree.
    """
    with open(html_file) as f:
        soup = BeautifulSoup(f, 'lxml')
        return soup


def grab_section_text(soup_object, start_terms, end_terms):
    """
    Collect strings that are found within a specified section of an HTML tree.

    :param soup_object: an HTML tree generated by BeautifulSoup.
    :param start_terms: list of strings--should specify the upper boundary.
    :param end_terms: list of strings--should specify the lower boundary.
    :return section_text: list of strings found within specified 10-K section.
    """
    section_text = []  # Populated with text found in specified 10-K section
    within_item_1A = False
    for tag in soup_object.html.strings:  # Search each element in the tree

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


def clean_strings(input_list):
    """
    Remove whitespace/stopwords, tokenizes, and lemmatizes a list of strings.

    :param input_list: a list of strings.
    :return cleaned_list: a cleaned version of input_list.
    """
    misfits = ['•', '\n', '\xa0']  # Remove misfit lines
    input_list = [x.lower() for x in input_list if x not in misfits]

    # Tokenize strings (i.e., break sentences down into a list of tokens)
    temp = ' '.join(input_list)  # Join elements in list into single string
    temp = regexp_tokenize(temp, "[\w']+")  # Use a regex to split words

    # Lemmatization (i.e., grouping together any inflected forms of a word)
    lemmatizer = WordNetLemmatizer()
    temp = [lemmatizer.lemmatize(word) for word in temp]

    # Uncomment to see how the lemmatization class works
    # for w in temp:
    #     print(w, " : ", lemmatizer.lemmatize(w))

    # Removing information-poor stopwords (e.g., 'in', 'the' 'to', etc.)
    stop_words = stopwords.words('english')
    temp = [w for w in temp if w not in stop_words]

    # Remove digit-value and single-character strings from text
    temp = [x for x in temp if not (x.isdigit())]
    cleaned_list = [x for x in temp if len(x) > 1]

<<<<<<< HEAD
    return cleaned_list


def main():
    soup_object = import_data('filing-details.html')  # Import html file
=======
def main(path):
    tree = import_data(str(path))  # Import html file
>>>>>>>  developing function to produce bulk local file paths

    # Specify a set of words that are unique to the boundaries of a section
    start_terms = ['ITEM', '1A.', 'RISK', 'FACTORS']
    end_terms = ['ITEM', '1B.', 'UNRESOLVED', 'STAFF', 'COMMENTS']

    risk_text = grab_section_text(soup_object, start_terms, end_terms)
    risk_text = clean_strings(risk_text)

    # print(risk_text)
    # print(len(risk_text))

    all_text = []
    all_text.append(risk_text)

    return all_text


#if __name__ == '__main__':
   # main()