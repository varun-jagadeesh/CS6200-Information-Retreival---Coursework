import numpy as np

#Global variables

S = []  #S is the set of sink nodes
edges_in_links = dict() #Incoming links - dictionary page as key and all its inlinks as val
node_vertices = dict() #All vertices
edges_out_links = dict()  #Outgoing links dictionary with page as key and all its outlinks as val
no_outlinks = dict() #Outlinks number
page_rank = dict() #Page Rank - dictionary
page_rank_temp = dict() #Temporary page ranks dictionary
edges_pair_in = open('edges.txt', 'r') #Read edges file
vertices = open('vertices.txt', 'r') #Read vertices file
edges_pair_out = open('edges.txt', 'r') #Read edges file


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
            edges_out_links[split_txt[0]].append(split_txt[1])
        else:
            edges_out_links[split_txt[0]] = [split_txt[1]]

    for each in edges_out_links:
        no_outlinks[each] = len(edges_out_links[each])


def calculate_page_rank():
    out_first_file = open("task1_output.txt", "w")
    for p in node_vertices:
        page_rank[p] = 1 / N

    for l in node_vertices:
        if l not in edges_out_links.keys():
            S.append(l)

    i = 1
    num = 0
    while num == 0:
        sink_page_rank = 0
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
        if i == 1:
            print("Iteration 1")
            out_first_file.write("Iteration - 1"+"\n")
            out_first_file.write("Node Name  "+"Node ID  "+"Page Rank"+"\n")
            for a in node_vertices:
                print(node_vertices[a], a, page_rank_temp[a])
                out_first_file.write(str(node_vertices[a])+"            "+ str(a)  + "      " + str(page_rank_temp[a]) + "\n")

        elif i == 10:
            print("Iteration 10")
            out_first_file.write("Iteration - 10"+"\n")
            out_first_file.write("Node Name  "+"Node ID  "+"Page Rank"+"\n")
            for a in node_vertices:
                print(node_vertices[a], a, page_rank_temp[a])
                out_first_file.write(str(node_vertices[a])+"            "+ str(a)  + "      " + str(page_rank_temp[a]) + "\n")

        elif i == 100:
            print("Iteration 100")
            out_first_file.write("Iteration - 100"+"\n")
            out_first_file.write("Node Name  "+"Node ID  "+"Page Rank"+"\n")
            for a in node_vertices:
                print(node_vertices[a], a, page_rank_temp[a])
                out_first_file.write(str(node_vertices[a])+"            "+ str(a)  + "      " + str(page_rank_temp[a]) + "\n")

        elif i > 100:
            for find in node_vertices:
                if np.abs(page_rank_temp[find] - page_rank[find]) < 0.1:
                    num = num + 1

        for page in node_vertices:
            page_rank[page] = page_rank_temp[page]

        i = i + 1
    out_first_file.close()


def main():
    load_incoming_links(edges_pair_in)
    load_nodes(vertices)
    load_outgoing_links(edges_pair_out)
    calculate_page_rank()


if __name__ == "__main__":
    main()
