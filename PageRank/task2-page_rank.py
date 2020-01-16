from math import log
import operator

S = []  # S is the set of sink nodes
perplexity = []  # Perplexity
edges_in_links = dict()  # Incoming links - dictionary page as key and all its inlinks as val
node_vertices = dict()  # All vertices
edges_out_links = dict()  # Outgoing links dictionary with page as key and all its outlinks as val
no_outlinks = dict()  # Outlinks number
page_rank = dict()  # Page Rank - dictionary
page_rank_temp = dict()  # Temporary page ranks dictionary
edges_pair_in = open('edges-edu.txt', 'r')  # Read edges file
vertices = open('vertices-edu.txt', 'r')  # Read vertices file
edges_pair_out = open('edges-edu.txt', 'r')  # Read edges file
uniform_val = dict()


def load_incoming_links(edges_pair_in):
    for each_line in edges_pair_in:
        split_txt = each_line.split()
        if split_txt[1] in edges_in_links:
            edges_in_links[split_txt[1]].append(split_txt[0])
        else:
            edges_in_links[split_txt[1]] = [split_txt[0]]


def load_nodes(vertices):
    global d, N
    for each_line in vertices:
        node_vertex = each_line.split()
        node_vertices[node_vertex[0]] = node_vertex[1]

    for i in node_vertices:
        page_rank[i] = 0
        page_rank_temp[i] = 0
    d = 0.85
    N = len(node_vertices)


def load_outgoing_links(edges_pair_out):
    for each_line in edges_pair_out:
        split_txt = each_line.split()
        if split_txt[0] in edges_out_links:
            # M[each_line[0]] = each_line[1:]
            edges_out_links[split_txt[0]].append(split_txt[1])
        else:
            edges_out_links[split_txt[0]] = [split_txt[1]]

    for each in edges_out_links:
        no_outlinks[each] = len(edges_out_links[each])


def calculate_perplexity():
    entropy = 0
    for page in page_rank.keys():
        entropy += page_rank[page] * log(page_rank[page],2)
    return 2 ** (-entropy)


def calculate_convergence(j):
    perplexityvalue = calculate_perplexity()
    perplexity.append(perplexityvalue)

    if len(perplexity) > 4:
        if (int(perplexity[j])) == (int(perplexity[j - 1])) == (int(perplexity[j - 2])) == (int(perplexity[j - 3])):
            return False
        else:
            return True
    else:
        return True


def calculate_page_rank():
    for p in node_vertices:
        page_rank[p] = 1 / N
        uniform_val[p] = 1 / N

    for l in node_vertices:
        if l not in no_outlinks.keys():
            S.append(l)

    i = 0
    while calculate_convergence(i):
        sink_page_rank = 0
        per_value = calculate_perplexity()
        print(i + 1, per_value)
        out_perplexity_file = open("task2_perplexity_file.txt", "a")
        out_perplexity_file.write(str(i + 1) + " " + str(per_value) + "\n")
        out_perplexity_file.close()
        if not S:
            sink_page_rank = sink_page_rank
        else:
            for each in S:
                sink_page_rank = sink_page_rank + page_rank[each]
        for page in node_vertices:
            page_rank_temp[page] = (1 - d) / N
            page_rank_temp[page] = page_rank_temp[page] + (d * sink_page_rank / N)
            if page in edges_in_links.keys():
                if not edges_in_links[page]:
                    page_rank_temp[page] = page_rank_temp[page]
                else:
                    for q in edges_in_links[page]:
                        page_rank_temp[page] = page_rank_temp[page] + d * page_rank[q] / no_outlinks[q]

        print(sum(page_rank_temp.values()))

        for page in node_vertices:
            page_rank[page] = page_rank_temp[page]

        i = i + 1


def find_top_50_pages():
    sort_dict = sorted(page_rank.items(), key=operator.itemgetter(1), reverse=True)
    outfile = open("task3-top_50_pages_page_rank.txt", "w")
    outfile.write("NO " + "Document ID  " + "Website domain name           " + "Page Rank" + "\n")
    count = 1
    for sp in range(len(sort_dict)):
        if count == 51:
            break
        outfile.write(str(count) + "   " + str(sort_dict[sp][0]) + "             " + str(
            node_vertices[sort_dict[sp][0]]) + "          " + str(sort_dict[sp][1]) + "\n")
        count += 1
    outfile.close()


def find_top_50_inlinks():
    sort_link = sorted(edges_in_links.items(), key=operator.itemgetter(1), reverse=True)
    out_file_2 = open("task3-top_50_pages_inlinks.txt", "w")
    out_file_2.write("NO " + "Document ID  " + "Website domain name           " + "Link Count" + "\n")
    count = 1
    for ilc in range(len(sort_link)):
        if count == 51:
            break
        link_a = node_vertices[sort_link[ilc][0]]
        out_file_2.write(str(count) + " " + str(sort_link[ilc][0]) + "  " + str(link_a) + " " + str(sort_link[ilc][1]) + "\n")
        count += 1
    out_file_2.close()


def find_prop_source():
    temp_source = []
    for sol1 in node_vertices:
        if sol1 not in edges_in_links.keys():
            temp_source.append(sol1)
    prop_s = str(float(len(temp_source)) / float(N))
    out_proportion_file = open("task3-proportion_all.txt", "a")
    out_proportion_file.write("\n The proportion of websites with no in-links (Sources)" + "\n" + str(prop_s))
    out_proportion_file.close()


def find_prop_sink():
    prop_si = str(float(len(S)) / float(N))
    out_proportion_file = open("task3-proportion_all.txt", "a")
    out_proportion_file.write("\n The proportion of websites with no out-links (Sinks)" + "\n" + str(prop_si))
    out_proportion_file.close()


def find_proportion_page_rank():
    t_c = 0
    for pr in node_vertices:
        if page_rank_temp[pr] < uniform_val[pr]:
            t_c = t_c + 1
    t_c = t_c / float(len(node_vertices))
    out_proportion_file = open("task3-proportion_all.txt", "a")
    out_proportion_file.write("\n The proportion of websites whose PageRank is less than their initial" + "\n" + str(t_c))
    out_proportion_file.close()


def main():
    load_incoming_links(edges_pair_in)
    load_nodes(vertices)
    load_outgoing_links(edges_pair_out)

    out_perplexity_file = open("task2_perplexity_file.txt", "w")
    out_perplexity_file.write("List of perplexity values obtained in each round until convergence" + "\n")
    out_perplexity_file.close()

    calculate_page_rank()
    find_top_50_pages()
    find_top_50_inlinks()
    find_prop_source()
    find_prop_sink()
    find_proportion_page_rank()


if __name__ == "__main__":
    main()
