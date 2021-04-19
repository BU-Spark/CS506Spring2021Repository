
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
from gensim.utils import simple_preprocess


# Internal packages
import html_parser_modified

#reading in data
# Upload table containing list of companies and their corresponding risk text
data = pd.read_csv("data/10k_2019_original.csv")



# Specify list of stop words
stop_words = stopwords.words('english')
more_stops_words = ['may', 'us', 'could', 'product', 'products', 'clinical', 
                    'development', 'regulatory', 'including', 'nk', 'business']
#combinding stopwords
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





''' Building a subset model to experiment with parameters''' 

#all text 2020
ss_processed_text = processed_text


#helper functions 


def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))


def make_bigrams(texts):
    
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return [bigram_mod[doc] for doc in texts]




data_words = list(sent_to_words(ss_processed_text))

bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)

#creating word counter function to find new financial based stop words
def word_counter(l, min):
    '''Finds words in list that appear more than the min 
    l = List of words as strings 
    min = minimum number threshold for words to how in new list
    '''
    top_words = []
    rare_words =[]
    l_set = set(l)
    for word in l:
        print(word,l.count(word))
        if l.count(word) > min:
            top_words.append((word,l.count(word)))
        else:
            rare_words.append(word)
    import pdb; pdb.set_trace()
    top_words = sorted(top_words, key=lambda x: x[1],reverse = True)

    return top_words



''' Second Layer of Preprocessing 2020'''

#chaining words 
ss_all_words = list(chain.from_iterable(ss_processed_text))

#removing potential new stop words
test_stop_words = ['company','december']

#removing stop words without bigram
ss_all_words= [ele for ele in ss_all_words if ele not in test_stop_words]

#replacing trials with 
ss_all_words = [word if word != 'trials' else 'trial' for word in ss_all_words]
ss_all_words = [word if word != 'patent' else 'patents' for word in ss_all_words]
ss_all_words = [word if word != 'result' else 'results' for word in ss_all_words]








''' not required'''
# Form Bigrams with bigram
ss_all_words_with_Bigram = make_bigrams(data_words)




# 2020
ss_lda_dict = corpora.Dictionary([ss_all_words])
#corpus
ss_corpus = [ss_lda_dict.doc2bow(text) for text in ss_processed_text]



#new model for subset
test_model = gensim.models.LdaModel(corpus = ss_corpus, id2word = ss_lda_dict,
                                    num_topics = 3,
                                    random_state = 100,
                                    iterations = 250,
                                    passes = 50, 
                                    per_word_topics = True,
                                    minimum_probability = 0.03,)

###############################################

''' post processing'''

topics_test = test_model.show_topics(formatted=False,num_words=20)

''' Format = list--> tuple---> list--->tuple'''

#v1

def extract_weights(lda_sub_topic):
    ''' example = topic_test
    input = individual topic for lda model with multiple topics'''
    topics =[]
    weights = []
    topic_words = []
    topic_values =[]
    for x in range(len(lda_sub_topic)):
        topics.append(lda_sub_topic[x][1])

        for sub in range(len(topics[x])):
            weights.append(topics[x][sub])

    clean_topics = []
    for word, value in weights:
        topic_words.append(word)
        topic_values.append(value)
        
    for i in range(len(topic_words)):
        if topic_words.count(topic_words[i]) == 1:
            clean_topics.append((topic_words[i],topic_values[i]))
    
    return clean_topics


#v2 compare repats and keep with highest weight 

def clean_model_topics(lda_sub_topic):
    ''' example = topic_test
    input = individual topic for lda model with multiple topics'''
    topics =[]
    weights = []

   #breaking down format of .show_topics()
    for x in range(len(lda_sub_topic)):
        topics.append(lda_sub_topic[x][1])
        for sub in range(len(topics[x])):
            weights.append(topics[x][sub])

    # splitting topics
    #converting dictionaries
    split = len(weights) / 3

    t1_weights = weights[:int(split)]
    t1_dict = dict( (k[0], k[1]) for k in t1_weights)

    t2_weights = weights[int(split):int(split * 2)]
    t2_dict = dict( (k[0], k[1]) for k in t2_weights)
    

    t3_weights = weights[int(split * 2):]
    t3_dict = dict( (k[0], k[1]) for k in t3_weights)
    
    list_of_dicts = [t1_dict, t2_dict, t3_dict]

    index_dictionary = {}
    deletes = []
    for index,dictionary in enumerate(list_of_dicts):
        for key,value in dictionary.items():
            if key not in index_dictionary:
                index_dictionary[key] = (index, value)
            else:
                if value > index_dictionary[key][1]:
                    del list_of_dicts[index_dictionary[key][0]][key]
                    index_dictionary[key] = (index, value)
                else:
                    deletes.append((index, key))
    for dels in deletes:
        del list_of_dicts[dels[0]][dels[1]]
        
    return ([(0,list_of_dicts[0]),(1,list_of_dicts[1]),(2,list_of_dicts[2])])


#restructuring topics

#2019
clean_topics = clean_model_topics(topics_test)

#############################################

''' creating wordcloud for test model 2019'''

# Create wordclouds of top n words in each topic
cols_test = [color for name, color in mcolors.XKCD_COLORS.items()]

cloud_test = WordCloud(background_color='white',
                  width=2500,
                  height=1800,
                  max_words=15,
                  colormap='tab10',
                  color_func=lambda *args, **kwargs: cols_test[i],
                  prefer_horizontal=1.0)


fig2, axes2 = plt.subplots(1, len(clean_topics) , figsize=(10,10), sharex=True, sharey=True)
''' formatted_clean_topics = distinct topics post processed_text
    topics_test = test model outputs
'''

for i, ax in enumerate(axes2.flatten()):

   
    fig2.add_subplot(ax)
    #test_topic_words = dict(formatted_clean_topics[i][1]) 
    test_topic_words = dict(clean_topics[i][1]) # error here
    #import pdb; pdb.set_trace()
    # becomes out od range??
    cloud_test.generate_from_frequencies(test_topic_words, max_font_size=300)
    #import pdb; pdb.set_trace()
    plt.gca().imshow(cloud_test)
    plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
    plt.gca().axis('off')


plt.subplots_adjust(wspace=0, hspace=0)
plt.axis('off')
plt.margins(x=0, y=0)
plt.tight_layout()
plt.show()

###################################################################
