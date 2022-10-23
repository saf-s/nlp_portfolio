# Assignment 6: Web Crawler - Finding/Building a Corpus through Web Scraping
# This program:
#   - acts as a web crawler that uses a starter URL and the Beautiful Soup library to crawl the web for relevant links
#   - scrapes all text off each relevant web page using Beautiful Soup and stores each page's raw text into a new file
#   - cleans the scraped text and stores the processed version of the text into a new file
#   - builds a searchable knowledge base of facts for the top 10 important terms extracted from the processed files

import re, pickle, nltk, requests, urllib
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from urllib import request, error
from bs4 import BeautifulSoup
from collections import Counter

# function that crawls the web from a starter URL
def web_crawler(starter_url):
    r = requests.get(starter_url)
    data = r.text
    soup = BeautifulSoup(data, features='html.parser')
    
    counter = 0
    
    # writes a list of at least 15 relevant URLs, which are pages both within and outside the original domain, to the new file 'urls.txt'
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            if 'super' in link_str or 'mario' in link_str or 'nintendo' in link_str or 'news' in link_str or 'platform' in link_str or 'character' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    #print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str and 'archive' not in link_str and '1up' not in link_str:
                    f.write(link_str + '\n')
                    counter += 1
                    if counter == 30:
                        break
    
    print("\nFinished crawling web from starter URL '" + starter_url + "'")
    print("\nHere are some relevant URLs:")
    
    counter = 1
    
    # outputs list of 30 relevant URLs from file     
    with open('urls.txt', 'r') as f:
        urls = f.read().splitlines()
    url_list = []        # stores the 30 URLs into a list
    for u in urls:
        print(str(counter) + ")", u)
        url_list.append(u)
        counter += 1
    
    # returns list of relevant URLs    
    return url_list

    
# function that determines if an element is visible
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


# function that loops through the URLs and scrapes all text off each page
def scrape_text(url_list):      # accepts list of URLs to scrape text from
    counter = 1
    
    for url in range(len(url_list)):
        try:
            html = urllib.request.urlopen(url_list[url])
        except urllib.error.HTTPError as e:
            response = ''
        except urllib.error.URLError as e:
            response = ''
        soup = BeautifulSoup(html, features='html.parser')
        data = soup.findAll(text=True)
        result = filter(visible, data)
        temp_list = list(result)
        temp_str = ' '.join(temp_list)
        
        # stores each page's scraped text in its own file
        with open('raw_url_page_' + str(counter) + '.txt', 'w') as f:
            f.write(str(temp_str.encode('utf-8')))
    
        counter += 1
         
        # scrapes text for 20 of the 30 URL pages
        if counter == 20:
            break


# function that cleans up text from each of the 20 files by deleting any newlines, tabs, and extra spaces
def process_text():
    counter = 1
    
    for url in range(1, 21):
        with open('raw_url_page_' + str(url) + '.txt', 'r') as f:
            raw_text = f.read()
        text = raw_text.replace('\\n', ' ').replace('\\', '').replace('#', '')
        clean_text = re.sub('\s+', ' ', text)
        clean_text = re.sub("b'", '', clean_text)
    
        # extracts sentences with NLTK’s sentence tokenizer
        sents = sent_tokenize(clean_text)
    
        # writes the sentences for each file to a new file
        with open('clean_url_page_' + str(counter) + '.txt', 'w') as f:
            for s in range(len(sents)):
                f.write(str(sents[s]) + '\n')
        
        counter += 1


# function that extracts n number of important terms from the 20 pages
def get_important_terms(n):
    counter = 0
    
    # creates a dictionary for term frequencies to store all terms from each page
    tf_dict = {}
    
    for url in range(1, 21):
        # converts all text to lowercase alphabets and removes stopwords
        with open('clean_url_page_' + str(url) + '.txt', 'r') as f:
            text = f.read()
        tokens = word_tokenize(text.lower())
        tokens = [w for w in tokens if w.isalpha() and w not in stopwords.words('english')]

        # gets term frequency by extracting important terms using token frequency count
        for token in tokens:
            if token in tf_dict:
                tf_dict[token] += 1
            else:
                tf_dict[token] = 1
        
        counter += 1
        
    # locates the most important terms through sorting
    sorted_counts = sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)
    
    # prints 25-40 important terms
    print("\n\nHere are " + str(n) + " important terms and their frequencies: ")
    for term in range(1, n + 1):
        print(str(term) + ")", sorted_counts[term - 1])
 
        
# function that builds a searchable knowledge base of facts that a chatbot can share related to the list of top 10 terms
def create_knowledge_base(top_10_terms):
    knowledge_base_dict = {}        # stores top 10 terms, and all sentences containing each term, in a dictionary
    knowledge_base_sents = []       # stores sentences, serving as facts of the knowledge base, into a list
    
    # loops through all sentences from the 20 processed files to add sentences matching each of the 10 terms to the dict
    for term in top_10_terms:
        knowledge_base_dict.update({term:[]})       # adds list of sentences for each term into dict values
        for url in range(1, 21):
            with open('clean_url_page_' + str(url) + '.txt', 'r') as f:
                text = f.read()
            sents = sent_tokenize(text.lower())
            for sent in sents:
                if term in sent:
                    knowledge_base_dict[term].append(sent)
    
    # returns the knowledge base of facts as a dict
    return knowledge_base_dict


# main function
def main():
    # sets starter URL representing Super Mario
    starter_url = "https://en.wikipedia.org/wiki/Super_Mario"
    
    # calls function that crawls the web from the starter URL and returns list of 30 relevant links
    url_list = web_crawler(starter_url)
    
    # calls function that scrapes raw text off 20 links in the list returned by web crawler function
    scrape_text(url_list)
    
    # calls function that processes and cleans up text from each file
    process_text()

    # calls function that extracts 40 important terms from the 20 pages
    get_important_terms(40)

    # stores the top 10 terms, determined manually based on domain knowledge, into a list
    top_10_terms = ['mario', 'game', 'nintendo', 'player', 'bowser', 'switch', 'jump', 'peach', 'mushroom', 'wii']
    
    # prints the list of top 10 terms
    print("\n\nHere are the top 10 terms: ")
    for term in range(1, (len(top_10_terms)) + 1):
        print(str(term) + ")", top_10_terms[term - 1])
        
    # calls function that returns the knowledge base for the 10 terms as a dictionary, where key:value pairs are terms:sentences
    knowledge_base_dict = create_knowledge_base(top_10_terms)
    
    # pickles knowledge base dictionary into file using write binary
    pickle.dump(knowledge_base_dict, open("knowledge_base_dict.p", 'wb'))
    
    # prints knowledge base dictionary    
    #print("\n\n", end="")
    #print(knowledge_base_dict)
    
    # stores knowledge base to new file
    #with open('knowledge_base.txt', 'w') as f:
    #    for term, sents in knowledge_base_dict.items():
    #        f.write("'%s':\t%s\n\n\n" % (term, sents))
    
    
# calls main function
if __name__ == '__main__':
    main()