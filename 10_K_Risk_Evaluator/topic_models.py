'''
--------------------------------------------------------------------------------
<CS506 Project: 10-K Risk Evaluator>

The process of learning, recognizing, and extracting these topics across a
collection of documents is called topic modeling.

Method 1. The Term Frequency – Inverse Document Frequency (TF-IDF)
Involves multiplying a local component like term frequency (TF) with a global
component, that is, inverse document frequency (IDF) and optionally
normalizing the result to unit length. As a result of this, the words that
occur frequently across documents will get downweighted.


Method 2. Latent Dirichlet Allocation (LDA)
LDA represents documents as mixtures of topics (a probabilistic topic model).

E.g., If we have 3 topics, then some specific probability distributions we’d
likely see are:
Mixture X: 90% topic A, 5% topic B, 5% topic C
Mixture Y: 5% topic A, 90% topic B, 5% topic C
Mixture Z: 5% topic A, 5% topic B, 90% topic C

Let's say companies face 4 different kinds of risk:
    market, liquidity, credit, operational

"If you view the number of topics as a number of clusters and the probabilities
as the proportion of cluster membership, then using LDA is a way of soft-
clustering your composites and parts. With the documents now mapped to a lower
dimensional latent/hidden topic/category space, you can now apply other machine
learning algorithms which will benefit from the smaller number of dimensions.
For example, you could run your documents through LDA, and then hard-cluster
them using DBSCAN."

Written by Evie Wan, Nicholas Mosca, Eric South
--------------------------------------------------------------------------------
'''
from gensim import corpora
from gensim import models
import numpy as np

import html_parser


def tf_idf(corpus_of_text):
    """
    Compare documents by Term Frequency–Inverse Document Frequency (TF-IDF).

    :param corpus_of_text: list of documents, where each document is a sublist
    of tokenized strings.
    :return weights: nested list containing words and their frequency weights.
    """
    # Create dictionary (each words gets a unique ID)
    risk_dict = corpora.Dictionary(corpus_of_text)
    # print(risk_dict.token2id)  # Display words and their unique IDs

    # Create a bag-of-words corpus
    risk_corpus = \
        [risk_dict.doc2bow(doc, allow_update=True) for doc in corpus_of_text]
    # print(risk_corpus)  # Print corpus represented as a dense array

    # Reference dictionary to make corpus human readable
    # word_counts = \
    #     [[(risk_dict[id], count) for id,
    #       count in line] for line in risk_corpus]
    # print(word_counts)  # Print corpus where IDs are replaced with the word

    # Save the dict and corpus to disk
    # risk_dict.save('risk_dict.dict')
    # risk_corpora.MmCorpus.serialize('bow_corpus.mm', bow_corpus)

    # Load them back
    # loaded_dict = corpora.Dictionary.load('risk_dict.dict')
    # risk_corpus = corpora.MmCorpus('bow_corpus.mm')
    # for line in corpus:
    #     print(line)

    # Create the TF-IDF model
    tfidf = models.TfidfModel(risk_corpus, smartirs='ntc')

    # Show the TF-IDF weights
    for doc in tfidf[risk_corpus]:
        weights = [[risk_dict[id],
                    np.around(freq, decimals=2)] for id, freq in doc]

    return weights


def lda(corpus_of_text):
    """
    Compare documents by Latent Dirichlet Allocation (LDA).

    :param corpus_of_text: list of documents, where each document is a sublist
    of tokenized strings.
    :return model: set of words that are most associated with each topic.
    """
    # Create a dictionary and corpus for the LDA model
    lda_dict = corpora.Dictionary(corpus_of_text)
    lda_corpus = [lda_dict.doc2bow(line) for line in corpus_of_text]

    # Train the model
    lda_model = models.LdaMulticore(corpus=lda_corpus,
                                    id2word=lda_dict,
                                    random_state=100,
                                    num_topics=4,
                                    passes=10,
                                    chunksize=1000,
                                    batch=False,
                                    alpha='asymmetric',
                                    decay=0.5,
                                    offset=64,
                                    eta=None,
                                    eval_every=0,
                                    iterations=100,
                                    gamma_threshold=0.001,
                                    per_word_topics=True)

    # Save the model
    # lda_model.save('lda_model.model')

    return lda_model.print_topics(-1)  # See the topics


def main():
    all_text = html_parser.main()  # Import a nested list of tokenized words
    tf_idf_weights = tf_idf(all_text)  # Run TF-IDF model and return weights
    topic_mixtures = lda(all_text)

    print(tf_idf_weights)
    print(topic_mixtures)


if __name__ == '__main__':
    main()
