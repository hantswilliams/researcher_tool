#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 06:53:08 2021

@author: hantswilliams

ADV search: https://pubmed.ncbi.nlm.nih.gov/advanced/ 

Mining the articles: https://github.com/allenai/scibert

https://arxiv.org/pdf/2010.09190.pdf
https://github.com/Grayming/SummPip
https://github.com/VincentK1991/BERT_summarization_1
https://towardsdatascience.com/summarization-has-gotten-commoditized-thanks-to-bert-9bb73f2d6922
https://ai.googleblog.com/2020/06/pegasus-state-of-art-model-for.html

Updated: May 1 2021 

"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import sys 



## HELPER FUNCTIONS 
## Funciton to determinal size of specific outputs 
## https://goshippo.com/blog/measure-real-size-any-python-object/ 
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size





##
# complex search breakdown: 




# ...SINGLE SEARCH TERM: 

# search: digital health [title]
# contains Numbers+Alpha: 5b, 2f, 5d 
# contains Numbers: none  
# https://pubmed.ncbi.nlm.nih.gov/?term=digital+health%5BTitle%5D&sort=date

# 5b appears to be TITLE 
# 2F appears to be ABSTRACT 
# 5d appears to be ???? comes at the end of each search term /// 



# ...TWO SEARCH TERMS 

# search: digital health [title/abstract] AND cnacer[title/abstract]
# contains Numbers+Alpha: 5b, 2f, 5d  //// FOR EACH INDIVIDUAL SEARCH TERM INSERTED 
# contains Numbers: 28 appears at the beginning ///// 29 appears at the end //// FOR EACH INDIVIDUAL SEARCH TERM INSERTED 

# https://pubmed.ncbi.nlm.nih.gov/?term=%28digital+health%5BTitle%2FAbstract%5D%29+AND
#                                       +%28cancer%5BTitle%2FAbstract%5D%29&sort=date&size=50

# 28(term1)29 
# 28(term2)29 



# ...THREE SEARCH TERMS 

# search: digital [title/abstract] health [title/abstract] cancner [title/abstract]

# https://pubmed.ncbi.nlm.nih.gov/?term=   %28%28digital%5BTitle%2FAbstract%5D%29+
#                                          AND+%28health%5BTitle%2FAbstract%5D%29%29+
#                                          AND+%28cancer%5BTitle%2FAbstract%5D%29&sort=date

# 28 28 (term1) 29 
# 28 (term2) 29 29 
# 28 (term3) 29 


# ...FOUR SEARCH TERMS 
# search: (    (    (digital[Title/Abstract]) AND (health[Title/Abstract])    )   AND (cancer[Title/Abstract])) AND    (device[Title/Abstract])

# https://pubmed.ncbi.nlm.nih.gov/?term=%28%28%28digital%5BTitle%2FAbstract%5D%29
#                                       +AND+%28health%5BTitle%2FAbstract%5D%29%29
#                                       +AND+%28cancer%5BTitle%2FAbstract%5D%29%29
#                                       +AND+%28device%5BTitle%2FAbstract%5D%29&sort=date

# 28 28 28 (term1) 29 
# 28 (term2) 29 29 
# 28 (term3) 29 29 
# 28 (term4) 29 


# ....FIVE SEARCH TERMS 

# https://pubmed.ncbi.nlm.nih.gov/?term=   %28%28%28%28patient%5BTitle%5D%29
#                                          +AND+%28health%5BTitle%5D%29%29
#                                          +AND+%28device%5BTitle%5D%29%29
#                                          +OR+%28treatment%5BTitle%5D%29%29
#                                          +AND+%28monitor%5BTitle%5D%29&sort=date&size=50

# 28 28 28 28 (term1) 29 
# 28 (term2) 29 29 
# 28 (term3) 29 29 
# 28 (term4) 29 29 
# 28 (term5) 29 




# Potential pattern for complex searches: 
# - Each term will contain FIRST 28 and LAST 29 
# - The total number of rows/lines shown above will equal the number of search terms 
# - THE LAST SEARCH TERM will always be a single 28 and a single 29 //// = 28 (lastterm) 29 
# - THE FIRST SEARCH WILL ALWAYS BE: 
#         - 28 count ==== (number of search terms) - 1 
#         - 29 count = will always be one 
# - The middle search terms: 
#         - 28 Term(X) 29 29 
#         - 28 Term(X) 29 29 










##### STEP1: GENERATE DETAILS OF THE SEARCH /// ASSOCIATED META-DETA OF SEARCH 
# Digital health search example 
url = "https://pubmed.ncbi.nlm.nih.gov/?term=%22digital+health%22&sort=date&size=50"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')


## Retrieving general characteristics about the search results 
pubmed_search_details = soup.find_all("div", class_="search-results-chunk results-chunk")
array_details = []

for i in pubmed_search_details:
    value = {}
    value['page_number'] = i['data-page-number']
    value['next_page_url'] = i['data-next-page-url']
    value['total_search_results'] = i['data-results-amount']
    value['example_article_ids'] = i['data-chunk-ids']
    array_details.append(value)

output_details = pd.DataFrame(array_details, columns=['page_number', 'next_page_url', 'total_search_results', 'example_article_ids'])

#Get sizes of objects
get_size(array_details)
get_size(output_details)






##### STEP2: RETRIEVE INDIVIDUAL ARTICLES FROM SEARCH ///// 
## Retrieving Details/Results of each of the articles 
pubmed_results = soup.find_all("article", class_="full-docsum")
array_items = []

for i in pubmed_results:
    value = {}
    value['article_title'] = i.find(["a"], class_="docsum-title").text
    value['article_title'] = ' '.join(value['article_title'].split())
    
    value['authors_full'] = i.find(["span"], class_="docsum-authors full-authors").text
    
    value['journal_full'] = i.find(["span"], class_="docsum-journal-citation full-journal-citation").text
    
    value['article_snippet'] = i.find(["div"], class_="full-view-snippet").text
    value['article_snippet'] = ' '.join(value['article_snippet'].split())
    
    if (i.find(['span'], class_='free-resources spaced-citation-item citation-part')) is not None:
        value['free_full_text'] = i.find(['span'], class_='free-resources spaced-citation-item citation-part').text
    else: 
        value['free_full_text'] = ''
        
    value['article_url'] = i.find(["button"], class_="share-search-result trigger result-action-trigger share-dialog-trigger")['data-permalink-url']
    value['href'] = i.find(["a"], class_="docsum-title")['data-article-id']
    array_items.append(value)
    
output_articles = pd.DataFrame(array_items, columns=['article_title', 'authors_full', 'journal_full', 'article_snippet', 'free_full_text', 'article_url', 'href'])













# ## Retrieving TITLES of each of the articles 
# ## VERSION 1 - SIMPLE 
# pubmed_results = soup.find_all("a", class_="docsum-title")
# print(pubmed_results)
# len(pubmed_results)
# item = pubmed_results[1]
# print(item)
# item.text
# print(item["href"])
# print(item["data-ga-label"])
# print(item["data-article-id"])

# pubmed_items = []

# for i in pubmed_results:
#     value = {}
#     value['title'] = i.text
#     value['article_id'] = i["data-article-id"]
#     pubmed_items.append(value)
    

# df_pubmed_items = pd.DataFrame(pubmed_items, columns=['title', 'article_id'])




# #### TESTING - MANUAL 
# pubmed_results3 = soup.find_all("article", class_="full-docsum")
# item3 = pubmed_results3[1]
# print(item3)
# item3.find(["a"], class_="docsum-title").text
# item3.find(["a"], class_="docsum-title")['href']
# item3.find(["a"], class_="docsum-title")['data-article-id']
# item3.find("span", class_="docsum-pmid").text
# item3.find(["a"], class_="docsum-title").text
# item3.find(["span"], class_="docsum-authors full-authors").text
# item3.find(["span"], class_="docsum-journal-citation full-journal-citation").text
# item3.find(["button"], class_="share-search-result trigger result-action-trigger share-dialog-trigger")['data-permalink-url']
# item3.find(["button"], class_="share-search-result trigger result-action-trigger share-dialog-trigger")['data-twitter-url']
# item3.find(["div"], class_="full-view-snippet").text
# item3.find(["span"], class_="docsum-authors full-authors").text






# ## Retrieving Details/Results of each of the articles 
# pubmed_results3 = soup.find_all("article", class_="full-docsum")
# #item = pubmed_results3[1]
# #item.text
# # print(pubmed_results3)
# # len(pubmed_results3)
# # print(item)
# # print(item["href"])
# # print(item["data-ga-label"])
# # print(item["data-article-id"])
# pubmed_items3 = []
# for i in pubmed_results3:
#     value = {}
#     value['article_title'] = i.find(["a"], class_="docsum-title").text
#     value['authors_full'] = i.find(["span"], class_="docsum-authors full-authors").text
#     value['journal_full'] = i.find(["span"], class_="docsum-journal-citation full-journal-citation").text
#     value['article_snippet'] = i.find(["div"], class_="full-view-snippet").text
#     value['article_url'] = i.find(["button"], class_="share-search-result trigger result-action-trigger share-dialog-trigger")['data-permalink-url']
#     value['href'] = i.find(["a"], class_="docsum-title")['data-article-id']
#     pubmed_items3.append(value)
    
# df_pubmed_items3 = pd.DataFrame(pubmed_items3, columns=['article_title', 'authors_full', 'journal_full', 'article_snippet', 'article_url', 'href'])































