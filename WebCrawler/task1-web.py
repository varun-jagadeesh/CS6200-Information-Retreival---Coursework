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

# Seed link of the assignment
#karen_seed_wiki_link = 'https://en.wikipedia.org/wiki/Karen_Sparck_Jones'


# Main Function
def main():
    web_crawler(karen_seed_wiki_link)
    link1_file_name = 'Link_Task_1.txt'
    output_file = open(link1_file_name, 'w')
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
    while len(links_visit) + len(frontier_queue) != links_crawl_limit and len(frontier_queue) != 0:
        curr = frontier_queue.pop(0)
        if curr[1] == maximum_depth_limit:
            break
        url_info = curr[0]
        links_visit.append(url_info)
        web_crawler_page(curr)
    while len(frontier_queue) != 0:
        curr = frontier_queue.pop(0)
        links_visit.append(curr[0])


# Define a function called Web Crawler Page that crawls page of a particular URL and gets the URL's
def web_crawler_page(curr):
    url_info = curr[0]
    depth = curr[1]

    # Declaring Sleep time politeness policy
    time.sleep(1)

    # Get the URL
    doc = requests.get(url_info)
    content_text = BeautifulSoup(doc.text, 'html.parser').find('div', {'id': 'mw-content-text'})

    if len(content_text.find('ol', class_='references') or ()) > 1:
        content_text.find('ol', class_='references').decompose()

    for link_new in content_text.find_all('a', {'href': re.compile("^/wiki")}):
        if ':' not in link_new.get('href') and len(frontier_queue) + len(links_visit) != links_crawl_limit:
            # print(link_new)
            link_new = page_wiki + link_new.get('href')
            link_new = link_new.split('#')
            link_new = link_new[0]
            if links_unvisited(link_new):
                #print(depth)
                frontier_queue.append((link_new, depth + 1))


# Define a function called links_unvisited to check if link is visited by the crawler or not
def links_unvisited(a):
    # Check if links is visited are not
    if a in links_visit:
        return False
    for url_info, depth in frontier_queue:
        if a == url_info:
            return False
    return True


if __name__ == "__main__":
    karen_seed_wiki_link = input("Enter the seed link: ")
    main()
