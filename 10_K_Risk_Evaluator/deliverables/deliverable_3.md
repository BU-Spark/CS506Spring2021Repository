## Deliverable 3
Weekly meetings: Tuesdays, 4:30pm (with Yifu); Thursdays, 3:15-4:00 pm (internal--progress updates/discussion)

#### Troubleshooting latent dirichlet allocation (LDA)
Despite specifying 5 distinct topics in the LDA, only 3 topic groups (groups 0, 2, or 3) were ever dominant in a document. Oddly, LDA results led to extreme data skew towards one dominant topic (document’s often had one topic predominant, opposed to an even distribution of ‘dominant topics’ across the entire corpus of documents. The problem is that uneven labelling of topics makes revenue comparison difficult. Our next steps are to tweak (and read more background literature about) the LDA model to achieve more ‘even’ outcomes.

#### What each label/feature in your dataset represents
LDA_and_revenue_v0.csv : preliminary dataset which contains LDA output, topic assignments, and financial metrics for biotech companies.
 - DominantTopic: numeric value which classifies the assigned distribution the LDA model assigned to that particular document
 - Topic Percentage: Details the mixure percentage of the dominant topic for a document (e.g., DominantTopic was '2', which encompasses 90% of document A)
 - Keywords: Top words the LDA decided best represented that particular document
 - Text: Tokenized list of risk text for a document
 - TCKR/company: ticker symbol or name of company
 - old_revenue: revenue for 2019
 - new_revenue: revenue for 2020
 - fc: fold change in revenue between 2019 and 2020 [(new_revenue - old_revenue) / old_revenue)]
 - delta: whether fold change was postive or negative

#### Checklist
- [x] All data is collected (*we have aggregated over 200 10-K risk sections!*)
- [x] Refine the preliminary analysis of the data performed in PD1&2 (*we've discovered the limitations of our LDA model (see draft report), and we have ideas for tuning/improving*)
- [x] Answer another key question (*we have combined our numeric, financial data with our LDA output, and have started to compare fold change in revenue 19->20 among topic groups!*)
- [x] Create a draft of your final report (*'CS506_report_v0.pdf' has been provided in our deliverables folder*)
- [x] Refine project scope and list of limitations with data and potential risks of achieveing project goal (* work in progress, we need to unpack our LDA model some more*)
- [x] Submit a PR with the above report and modifications to original proposal (*here it is*)
 
 -- Evie Wan, Nick Mosca, Eric South

