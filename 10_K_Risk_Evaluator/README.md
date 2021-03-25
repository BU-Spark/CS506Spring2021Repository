# Categorizing Companies By 10-K Filings (i.e., Stated Risk Factors) & Comparing 2019 -> 2020 Performance 

# Project Description
We propose to develop or adapt a web-scraping tool that extracts data from Securities and Exchange Commission (SEC) filings. Publicly traded companies must annually submit 10-K filings (which detail financial performance) to the SEC. 10-K filings contain both forward looking statements and risk factor sections, which each consist of multiple paragraphs. These 10-K subsections may emphasize technical, market, or supply chain risk, among other factors. We plan to use unsupervised learning (e.g., cosine similarity) to cluster and compare companies based on their stated business model risks. 

As a starting point, a subset of companies from the iShares Nasdaq Biotechnology ETF (NASDAQ: IBB) will have ‘Item1A’ (i.e., risk factor section) of their latest 10-K parsed. A combination of K-means clustering and cosine similarity will be applied in search of discrete groupings, or ‘vulnerability classes’. Once companies are grouped into risk categories, financial performance (e.g., net profit, changes in stock, etc.) will be compared pre- and post- COVID-19. Among biotechnology companies, we are interested in the relationship between 1) types of business model risk (as stated in SEC filings) and 2) financial growth during a pandemic.

Our initial pipeline will compare only a handful of companies from IBB. However, we plan to generalize our pipeline to later handle the entire ETF, or other arbitrary sets of companies with SEC filings. Time permitting, we would also extend our cosine similarity efforts to social media data. For example, does the “persona” of a post/tweet among company (or executive) profiles pre-COVID hold any predictive power to the company’s performance mid-COVID?

# Data Sets
EDGAR (the Electronic Data Gathering, Analysis, and Retrieval system)
- Repository of submissions by companies who are required by law to file forms with the U.S. Securities and Exchange Commission (SEC)

Yahoo Finance
- Retrieval of stock performance, net profits, and other financial metrics

# Suggested Steps
Data Collection:  Web-scraping on EDGAR, importing 10-K filings of interest, parsing HTML documents, and isolating (textual) 10-K subsections.

Analysis: Calculating soft cosine similarity within ‘Item1A’ of 10-Ks filings. Once ‘risk groups’ are defined, the performance of each company (e.g., changes in stock, net profits, etc.) will be compared within and between clusters.

# Questions to be answered in Analysis
Among biotechnology companies, we are interested in the relationship between 1) types of business model risk (as stated in SEC filings) and 2) financial growth during a pandemic.

How are companies clustered by risk? Will we find discrete groups that emphasize either technical, market, or supply chain risk? Or, will companies be grouped into non-intuitive risk categories? Will companies cluster at all?

# Tools and Methods
Scraping: beautiful soup, Autoscraper, or EDGAR specific packages will be used to aggregate data from yahoo finance webpages. 
- Scraping EDGAR with Python (https://doi.org/10.1080/08832323.2017.1323720)

Pandas will support cleaning and preprocessing efforts, scikit learn for cosine similarity and clustering, and both Matplotlib and Seaborn for data visualization.

# Installation
# Usage
# Examples
# Contact Information
Eric South; Nicholas Mosca; Evie Wan
esouth@bu.edu; njmosca@bu.edu; ewan212@bu.edu;
571-340-0257; 631-678-7860 ; 424-666-5906; 
