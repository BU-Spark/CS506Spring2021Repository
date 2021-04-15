## Deliverable 4
Weekly meetings: Tuesdays, 4:30pm (with Yifu); Thursdays, 3:15-4:00 pm (internal--progress updates/discussion)

We've added to our draft report! We're polishing our narrative and integrating our recent advances in developing a supervised learning model.

#### Expand Scope - Supervised Learning Model
sentiment_NLP.ipynb : sentiment analysis and fitting logistic regression model
- Financial vocabulary used for calculating sentiment scores was taken from Lougran and McDonald Sentiment Word List. This dictionary was created specifically for financial texual analysis. Sentiment words are organized by category (negative, positive, litigious, strong, weak, constraining).
- revenue: binary, 1.0: increase in revenue; 0.0: decrease in revenue
- link_text: all texts scraped from 10-k files
- clean_text: removed stop words, expanded contractions, removed html tags, removed words less than 4 letters
- word_index: dictionary, tokenized unique words
- sentiment score variables: positive_score, negative_score, litigous_score, modal_strong, modal_weak, polarity_score (calculated using positive and negative scores), complex_words_p (proportion), complex_word_count, word_count, constraining_scores, positive_word_proportion, negative_word_proportion, constraining_word_proportion
- logistic regression model fit all sentiment score variables againt delta in revenue
- model precision (training precision) 0(decrease in revenue): 0.81; 1(increase in revenue): 0.77.
- next step: look at feature ranks

#### Checklist
- [x] All data is collected (*we have aggregated over 200 10-K risk sections!*)
- [x] Refine the preliminary analysis of the data performed in PD1&2 (*we've discovered the limitations of our LDA model (see draft report), and we have ideas for tuning/improving*)
- [x] Answer another key question (*we have combined our numeric, financial data with our LDA output, and have started to compare fold change in revenue 19->20 among topic groups!*)
- [x] Create a draft of your final report (*'CS506_report_v0.pdf' has been provided in our deliverables folder*)
- [x] Refine project scope and list of limitations with data and potential risks of achieveing project goal (* work in progress, we need to unpack our LDA model some more*)
- [x] Submit a PR with the above report and modifications to original proposal (*here it is*)
 
 -- Evie Wan, Nick Mosca, Eric South
 

