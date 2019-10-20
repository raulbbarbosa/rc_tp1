#!/usr/bin/env python
# coding: utf-8

# In[1]:


from graph_tool.all import *


# In[4]:


import gzip
import numpy as np


# In[8]:


grafos = [
    #["roadNet-TX.txt.gz", False],
    ["protein.edgelist.txt", False],
    ["metabolic.edgelist.txt", True],
    ["powergrid.edgelist.txt", False],
    ["facebook_combined.txt.gz", False],
    #["phonecalls.edgelist.txt", False],
    #["collaboration.edgelist.txt", False],
    #["email.edgelist.txt", False],
    #["internet.edgelist.txt", False],
    #["www.edgelist.txt", True],
]


for file_name, is_directed in grafos:
    
    g = Graph(directed=is_directed)

    node_index_control = {

    }
    
    print("lendo arquivo ", file_name)
    if ".gz" in file_name:
        with gzip.open(file_name, 'r') as f:
            for l in f:
                if not l.startswith(b"#"):
                    a, b = [int(x) for x in l.split()]
                    if a not in node_index_control:
                        va = g.add_vertex()
                        index_va = g.vertex(va)
                        node_index_control[a] = index_va
                    else:
                        va = g.vertex(node_index_control[a])

                    if b not in node_index_control:
                        vb = g.add_vertex()
                        index_vb = g.vertex(vb)
                        node_index_control[b] = index_vb
                    else:
                        vb = g.vertex(node_index_control[b])

                    g.add_edge(va, vb)
    else:
        with open(file_name, 'r') as f:
            for l in f:
                if not l.startswith("#"):
                    a, b = [int(x) for x in l.split()]
                    if a not in node_index_control:
                        va = g.add_vertex()
                        index_va = g.vertex(va)
                        node_index_control[a] = index_va
                    else:
                        va = g.vertex(node_index_control[a])

                    if b not in node_index_control:
                        vb = g.add_vertex()
                        index_vb = g.vertex(vb)
                        node_index_control[b] = index_vb
                    else:
                        vb = g.vertex(node_index_control[b])

                    g.add_edge(va, vb)
    
    print("arquivo lido", file_name)
    dataset_name = file_name[:file_name.find('.')]
    
    print("tamanho componentes conexas ", file_name)
    
    # tamanho componentes conexas
#     comp, hist = label_components(g)
#     contagem_ccs = hist
#     cc_filename = "_".join([dataset_name,"tamanho_cc"])
#     np.save(cc_filename, contagem_ccs)    
    
    print("distance", file_name)
    # distance
#     dists = shortest_distance(g,)
#     dists_filename = "_".join([dataset_name,"distancias"])
#     distances_array = np.array([dist for dist in dists])
#     np.save(dists_filename, distances_array)
    
    print("graus", file_name)
    # graus
#     in_degs = g.get_in_degrees(g.get_vertices())
#     out_degs = g.get_out_degrees(g.get_vertices())

#     in_deg_filename = "_".join([dataset_name,"grau_in"])
#     np.save(in_deg_filename, in_degs)
#     out_deg_filename = "_".join([dataset_name,"grau_out"])
#     np.save(out_deg_filename, out_degs)
    
    print("lc", file_name)
    # lc
#     lc = local_clustering(g)
#     lc_filename = "_".join([dataset_name,"lc"])
#     np.save(lc_filename, lc.a)
    
    print("pr", file_name)
    # pr
#     pr = pagerank(g)
#     pr_filename = "_".join([dataset_name,"pr"])
#     np.save(pr_filename,  pr.a)
    
    print("close", file_name)
    # close
#     cl = closeness(g)
#     cl_filename = "_".join([dataset_name,"cl"])
#     np.save(cl_filename, cl.a)
    
    print("bet", file_name)
    # betweeness
#     v_bn, e_bn = betweenness(g)
#     bt_filename = "_".join([dataset_name,"bt"])
#     np.save(bt_filename, v_bn.a)
    
    # desenhando
#     fig_filename = "_".join([dataset_name, "graph_plot"])
#     graph_draw(g, output=fig_filename+".png")
    
    print("n_edges")
    edge_filename = "_".join([dataset_name, "n_edges"])
    n_edges = np.array([len(g.get_edges())])
    print(n_edges)
    np.save(edge_filename, n_edges)





# In[ ]:




