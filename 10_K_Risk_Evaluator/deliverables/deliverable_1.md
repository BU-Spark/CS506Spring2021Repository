# Deliverable 1
Weekly meetings: Thursdays, 3:15-4:00 pm. Yifu and Lance are welcome to join whenever.

## Update on Importing 10-K Filings
For our Financial analysis of the IBB index we have decided to use yearly 10-K documents to extract information. To do so we developed a function that ties into the SEC financial dase and bulk downloads financial documents of choice. The function was paired with a file containing al of the IBB ticker symbols as of 2/19/2021. Files for the entire index are downloaded local in both .txt and .html format in a location determined by the user.  Once downloaded the html file would feed into or parser for data extraction. 

We are also in the progress of developing a function that links local file location to html parser function for a more streamlined and bulk data organizing. This function would automatically feed the html files into the parser function given the different location of files. This is our solution to manage the almost 10GB data already downloaded. The user would download the files locally and this path_mover function would be able to bridge that file location with out other functions.

- The goal for this week is to finish the path mover/ bridge function and link it to the html parser.
-  This should allow users to download all of the data and already clean and extract useful risk factor information.

- Nick Mosca_

## Update on 10-K Data Extraction
We've written a parser that extracts financial metrics data from .xml and .html files and combine them into pandas dataframes for downstream analyses.

## Update on Clustering
### tl;dr ###
The simplest (and probably most inaccurate) method to compare English strings: chopping them up into a Bag of Words (BoW), calculating unique word counts, and then mapping those features onto a vector space. Cosine similarity would then quantitate 'likeness' between strings (i.e. vectors), which can then be used for clustering. We want a more sophisticated sentiment analysis, thus we're digging into NLP theory. Our current envisioned workflow: String data -> Word2Vec (semantic-sensitive algorithim) -> Vector Space Model -> Cosine Similarity -> GMM for clustering.

### ts;wm ###
Originally, we planned to quantitate the similarity of strings (i.e. paragraphs in a 10-K's Item 1A. Risk Section) by calculating cosine similarity between strings mapped onto a vector space model. However, upon further reading, we realized cosine similarity (on its own) only addressed part of our use case.

Strings can be preprocessed in various ways. For example, similarity can be based on term frequency (e.g. using a Count Vectorizer to enumerate the number of words in a 'Bag of Words' (BoW)). The summation of 'word counts' in a string will produce a multi-dimensional vector, which can then be fed into a cosine similarity function. While atomizing and counting distrete words can effectively compare lexical similarities between strings, this method fails to acknowledge semantic similarities.

To illustrate the importance of semantic similarity, here's an example from an article of NTL (https://medium.com/@adriensieg/text-similarities-da019229c894):

s1 = "The president greets the press in Chicago"
s2 = "Obama speaks to the media in Illinois"

Although we recognize s1 and s2 as being similar in meaning, applying a Count Vectorizer + Cosine Similarity would yield low similarity (the algorithm would only notice two strings with different words).

Ideally we need an algortihm that recognizes both semantic & lexical similarity. Recognizing semantic similarity requires an underlying map of word embeddings, where 1) words are represented as real-valued vectors and 2) words that are closer in the vector space are expected to be similar in meaning. Word embeddings enable words with similar meanings to have similar vector representations (https://machinelearningmastery.com/what-are-word-embeddings/).

Right now, we're researching how to implement word embeddings into our pipeline.

-Eric South

