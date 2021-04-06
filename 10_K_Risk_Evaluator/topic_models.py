'''
--------------------------------------------------------------------------------
<CS506 Project: 10-K Risk Evaluator>

The process of learning, recognizing, and extracting these topics across a
collection of documents is called topic modeling.

Implementing Latent Dirichlet Allocation (LDA)
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
# Supporting Libaries
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from wordcloud import WordCloud, STOPWORDS

# Pre-processing; string cleaning
from nltk.corpus import stopwords

# Pre-processing; feature engineering
import gensim
from gensim import corpora
from gensim import models

# Internal packages
import html_parser


# Upload table containing list of companies and their corresponding risk text
data = pd.read_csv("data/10k_2020.csv")

# Specify list of stop words
stop_words = stopwords.words('english')
more_stops_words = ['may', 'us', 'could', 'product', 'products', 'clinical', 
                    'development', 'regulatory', 'including', 'nk', 'business']

stop_words = stop_words + more_stops_words


# Combine all words from csv to create a total corpus of terms
processed_text = []
for i in range(len(data)):
    text = data.iloc[i, 1]
    try:
        text = gensim.utils.simple_preprocess(text, deacc=True)  # Clean string
    except:
        text = ['missing']  # Empty risk sections (i.e. nan values)

    temp_list = []
    for j in range(len(text)):  # Remove stop_words from risk section text
        if text[j] not in stop_words:
            temp_list.append(text[j])
    try:
        processed_text.append(temp_list)
    except:
        processed_text.append(['missing'])


# Create dictionary
# Reformat all_words before feeding into gensim's Dictionary method
all_words = list(chain.from_iterable(processed_text))  # Flattening nested list
lda_dict = corpora.Dictionary([all_words])

# Create corpus
corpus = [lda_dict.doc2bow(text) for text in processed_text]

# Build a Latent Dirichlet Allocation (LDA) model
lda_model = models.LdaMulticore(corpus=corpus,
                                id2word=lda_dict,
                                random_state=100,
                                num_topics=5,
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
lda_model.print_topics(-1)  # See the topics


# Identify the dominant topic (& its percentage contribution) for each document
def format_topics_sentences(ldamodel=None, corpus=corpus, texts=data):
    """
    Extract the dominant topics from a list of risk texts.

    :param ldamodel: LDA model pre-fitted with corpus and dictionary.
    :param corpus: list of tuples containing words & their occurance in corpus.
    :param texts: list of strings--should specify the lower boundary.
    :return section_text: nested list of tokenize strings (for each risk text).

    """
    # Initialize output DataFrame
    topics = pd.DataFrame()

    # Grab the main topic in each document
    for i, rows in enumerate(ldamodel[corpus]):
        row = rows[0] if ldamodel.per_word_topics else rows
        print(row)

        row = sorted(row, key=lambda x: (x[1]), reverse=True)

        # Get the dominant topic, % contribution and keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # Dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                topics = \
                    topics.append(pd.Series([int(topic_num),
                                             round(prop_topic, 4),
                                             topic_keywords]),
                                  ignore_index=True)
            else:
                break
    topics.columns = \
        ['DominantTopic', 'PercentContribution', 'TopicKeywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    topics = pd.concat([topics, contents], axis=1)
    return(topics)


df_topic_sents_keywords = \
    format_topics_sentences(ldamodel=lda_model,
                            corpus=corpus,
                            texts=processed_text)

# Format
dominant_topics = df_topic_sents_keywords.reset_index()
dominant_topics.columns = ['DocumentNum',
                           'DominantTopic',
                           'TopicPercentContribution',
                           'Keywords',
                           'Text']
dominant_topics.head(10)







# Create wordclouds of top n words in each topic
cols = [color for name, color in mcolors.XKCD_COLORS.items()]

cloud = WordCloud(background_color='white',
                  width=2500,
                  height=1800,
                  max_words=15,
                  colormap='tab10',
                  color_func=lambda *args, **kwargs: cols[i],
                  prefer_horizontal=1.0)

topics = lda_model.show_topics(formatted=False)

fig, axes = plt.subplots(1, 5, figsize=(10,10), sharex=True, sharey=True)

for i, ax in enumerate(axes.flatten()):
    fig.add_subplot(ax)
    topic_words = dict(topics[i][1])
    cloud.generate_from_frequencies(topic_words, max_font_size=300)
    plt.gca().imshow(cloud)
    plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
    plt.gca().axis('off')


plt.subplots_adjust(wspace=0, hspace=0)
plt.axis('off')
plt.margins(x=0, y=0)
plt.tight_layout()
plt.show()


def main():
    all_text = html_parser.main()  # Import a nested list of tokenized words
    print(topic_mixtures)


if __name__ == '__main__':
    main()
