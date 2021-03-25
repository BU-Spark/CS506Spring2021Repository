## Deliverable 2
Weekly meetings: Tuesdays, 4:30pm (with Yifu); Thursdays, 3:15-4:00 pm (internal--progress updates/discussion)

Since our last deliverable, we've connected our web scraping module (10K_extraction.py) to our HTML parsing module (html_parser.py). We can now scan and extract hundreds of 'Risk Sections' (i.e. paragraphs of strings found between Item 1A. and Item 1B.) from SEC 10-K filings. Currently, we can query the SEC EDGAR database, upload a slew of financial documents onto our local machines, parse these files, and produce a CSV which contains 1) company ID and 2) cleaned risk text. Obtaining this CSV is a mile stone, as it'll enable downstream topic modelling and EDA (see below).

#### Improved Plumbing between Modules
We've developed a function for bulk downloading of all 10-k financial documents from the IBB index (2019 & 2020). We've also written supporting modules (path_mover.py and structuring_data.py), which generate lists of directory paths (and help plumb all our local HTML files to our HTML parser). 

### Evaluating Performance of our HTML Parser 
We've found that our HTML parser is fairly generalizable (i.e. can successfully extract risk sections from a heterogenous mix of html data). Although 10-K filings are proportedly standardized, the underlying HTML tree can vary, and thus developing a scalable method for isolating specific text sections is non-trivial. We've found that our current html_parser.py returns nan values for a proportion of 10-K filings-- indicating unbeknownst bugs in our scraping algorithm. Despite these issues, our web scrapper can return over 200 Risk Sections for companies between 2019 and 2020 (which we're satisfied with, as it'll provide an inital corpus for our topic modeling efforts).

#### Implementing Latent Dirichlet Allocation (LDA)
Given our initial corpus of text (i.e. 200 risk sections--paragraphs containing self-prescribed vulnerabilities by companies executives), we have developed topic_model.py, which learns and extracts topics across a collection of documents. The module converts our company CSV file (see above) into 1) a corpus dictionary (i.e. unique set of words) and 2) corpus of text (i.e. term-frequencies for each risk document). This corpus of text feeds into an LDA model, where we specify the number of components (topics) a priori. As a starting point, we've selected 5 topics based on the literature surrounding business risk theory. According to Investopedia, business risks can be categorized as either: market, liquidity, credit, or operational. We've processed our preliminary risk corpus with LDA and produced word clouds, which visualize the top 15 words in each topic. Our output topics have considerable overlap, which tells us we need to either 1) tune our model or 2) refine preprocessing steps (e.g. adding stopwords or improving upstream string cleaning).

#### Checklist
- [x] Collect and pre-process a secondary batch of data (*we have aggregated over 200 10-K risk sections!*)
- [x] Refine the preliminary analysis of the data performed in PD1 (*we have developed a preliminary LDA model which categorizes documents!*)
- [x] Answer another key question (*we have generated word clouds for our five topics (see above)--we see little differences in topics between 2019 and 2020*)
- [x] Refine project scope and list of limitations with data and potential risks of achieving project goal (*see below*)
- [x] Submit a PR with the above report and modifications to original proposal (*here it is*)
 
#### Current Scope and Limitations
Although we're excited that our LDA model works, we're slightly concerned that our compiled risk sections will not form distinct 'topic groups'. Upon initial analysis, many of the top words among topics groups were standard biotech business words (e.g., 'product', 'develop', 'regulatory', 'clinical'). We need to refine our model to form more differentiable groupings. If we cannot do this, we'll need to focus less finding differences among documents and more on exploring trends among our risk corpus. Either way, the next phase of our project will predominantly focus of exploratory data analysis.
  
#### Next steps
- Fix any lingering bugs in html_parser.py (to make the HTML scrapper more generalizable to abnormal 10-K filings)
- Post-LDA, explore additional ways to visualize top words among 'topic groups' (beyond word clouds)
- General exploratory data analysis-- what does our corpus look like? How can we tie in all the financial performance metrics we gathered into our LDA categorizations?

- Eric South

