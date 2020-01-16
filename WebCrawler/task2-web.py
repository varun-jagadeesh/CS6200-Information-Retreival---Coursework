from bs4 import BeautifulSoup
import requests
import time
import re

# Declaring variables

# Crawl limit = 1000
links_crawl_limit = 1000

# Maxiumum depth limit to crawl
maximum_depth_limit = 5

# Frontier (Queue)
frontier_queue = []

# List of Visited links
links_visit = []

# Main page
page_wiki = "https://en.wikipedia.org"

#Seed link of the assignment
#karen_seed_wiki_link = 'https://en.wikipedia.org/wiki/Karen_Sparck_Jones'
#keyword = 'retrieval'

def main():
    web_crawler(karen_seed_wiki_link)
    link2_file_name = 'Link_Task_2.txt'
    output_file = open(link2_file_name, 'w')
    ind = 1

    # Output file will be created
    for i in links_visit:
        row_var = str(ind) + " " + str(i) + "\n"
        output_file.write(row_var)
        ind += 1
    output_file.close()

# Define a function called web_crawler that will store URL's and will choose the URL should be crawled in future
def web_crawler(seed):
    frontier_queue.append((seed, 1))
    while len(links_visit) != links_crawl_limit and len(frontier_queue) != 0:
        curr = frontier_queue.pop()
        url_info = curr[0]
        if url_info in links_visit:
            continue
        links_visit.append(url_info)
        web_crawler_page(curr)

    while len(frontier_queue) != 0:
        curr = frontier_queue.pop()
        links_visit.append(curr[0])


# Define a function called Web Crawler Page that crawls page of a particular URL and gets the URL's
def web_crawler_page(curr):
    if curr[1] == maximum_depth_limit or len(links_visit) == links_crawl_limit:
        return
    link_info = ""
    url_info = curr[0]

    # Declaring Sleep time politeness policy
    time.sleep(1)
    depth = curr[1]
    doc = requests.get(url_info)
    content_text = BeautifulSoup(doc.text, 'html.parser').find('div', {'id': 'mw-content-text'})

    # Need to maintain and restore the order of links that is obtained
    temp_frontier = []

    if len(content_text.find('ol', class_='references') or ()) > 1:
        content_text.find('ol', class_='references').decompose()

    for link_new in content_text.find_all('a', {'href': re.compile("^/wiki")}):
        if ':' not in link_new.get('href') and len(frontier_queue) + len(links_visit) != links_crawl_limit:
            try:
                link_info = str(link_new.text)
            except UnicodeEncodeError as e:
                pass
            if (keyword.lower() in str(link_new.get('href')).lower()) or (keyword.lower() in link_info.lower()):
                #print(link_new)
                link_new = page_wiki + link_new.get('href')
                link_new = link_new.split('#')
                link_new = link_new[0]
                if not ((link_new in temp_frontier) or (link_new in links_visit)):
                    #print(depth)
                    temp_frontier.append((link_new, depth + 1))

    # Back to original link restoration
    while len(temp_frontier) != 0:
        #print(temp_frontier)
        frontier_queue.append(temp_frontier.pop())


if __name__ == "__main__":
    karen_seed_wiki_link = input("Enter the seed link: ")
    keyword = input("\nPlease enter keyword retrieval: ")
    main()
