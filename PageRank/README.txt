README

CS 6200 – Information Retrieval
Assignment – 2
Page Rank

Language used:	Python

Libraries Used:
-numpy
-operator
-math

Input Files:
Task-1 edges.txt, vertices.txt
Task-2 edges-edu.txt, vertices-edu.txt						

Source code:

Task-1 [10 points] 
Implement the iterative PageRank algorithm using the given graph

File Name :   task1-page_rank (task1-page_rank.py)
Execution:  Execute file with command python filename.py



Task-2[20 points] - PageRank algorithm, outputting the perplexity of your PageRank distribution until the change in perplexity is less than 1 for at least four consecutive iterations.
Task 3[20 points] - Sort the collection of web pages 

File Name : task2-page_rank (task2-page_rank.py)
Execution:  Execute each file with command python filename.py


Output Files:

Task-1:		
File Name: task1_output.txt

The file contains a list of the PageRank values that are obtained for each of the six vertices after 1, 10, and 100 iterations of the PageRank algorithm. It has have three values on each line: node id, node name, and PageRank value.



Task-2: 	
File Name : task2_perplexity_file.txt

The above file contains list of the perplexity values that are obtained in each round until convergence


Task-3:
File Name : task3-top_50_pages_page_rank.txt 
-a list of the document ID, website domain name, and PageRank of the top 50 websites as sorted by PageRank	

File Name : task3-top_50_pages_inlinks.txt
-a list of the document ID, website domain name, and in-link count of the top 50 websites by in-link count


File Name : task3-proportion_all
-the proportion of websites with no in-links (sources) - 
-the proportion of websites with no out-links (sinks) - 
-the proportion of websites whose PageRank is less than their initial, uniform values - 