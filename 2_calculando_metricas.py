#!/usr/bin/env python
# coding: utf-8


import numpy as np
import time

import matplotlib.pyplot as plt

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

def ccdf_subplot(metric_array, metric_name, titulo, dataset, ax):
    new_ar = np.ravel(metric_array) # alguma medidas sao 2d
    sorted_ar = np.sort(new_ar)
    
    y = []

    for i,x in enumerate(sorted_ar):

        if i == 0:
            valor = 1.0
            y.append(valor)
        elif i > 0:
            if x == sorted_ar[i-1]:
                y.append(valor)
            else:
                N = sorted_ar.shape[0]*1.0
                valor = (N - i)/N
                y.append(valor)
        else:
            raise
    
    print("plot")

    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_title(titulo)
    ax.set_xlabel('x')
    ax.set_ylabel("fração de valores >= x")
    ax.plot(sorted_ar, y, marker="+", markersize=5, linestyle='None')
    
    return y

# plotando ccdfs numa só figura
metrics = [
    ["tamanho_cc","Tamanho C.C."],
    ["grau_in", "Grau de entrada"],
    ["grau_out","Grau (de saída - em grafos direcionados)"],
    ["lc", "Clusterização Local"],
    ["pr", "Page Rank (alpha = 0.85)"],
#     ["cl", "Closeness"],
#     ["bt", "Betweenness"],
    ["distancias", "Distâncias"],
]

result = {}
        
linhas_plot = 2
colunas_plot = 3

plt.clf()
fig, axes = plt.subplots(linhas_plot, colunas_plot, figsize=(16, 8), constrained_layout=True)
    
# outra abordagem, loop por metrica e dataset
for i, (metric_name, titulo) in enumerate(metrics):
    result[metric_name] = {}
    idx_linha = int(i/colunas_plot)
    idx_coluna = i % colunas_plot
    ax = axes[idx_linha, idx_coluna]
    for file_name, _ in grafos:

        #print("arquivo lido", file_name)
        dataset_name = file_name[:file_name.find('.')]

        # tamanho componentes conexas
        metric_filename = "_".join([dataset_name,metric_name])
        
        metric_array = np.load(metric_filename+".npy")
        ccdf_subplot(metric_array, metric_name, titulo, dataset_name, ax)
    
fig.suptitle("CCDFs Empíricas" )
fig.legend([file_name[:file_name.find('.')] for file_name, _ in grafos], loc='lower center', ncol=len(grafos))
fig.savefig("ccdfs.png")


metrics = [
    ["tamanho_cc","Tamanho C.C."],
    ["grau_in", "Grau de entrada"],
    ["grau_out","Grau (de saída em grafos direcionados)"],
    ["lc", "Clusterização Local"],
    ["pr", "Page Rank (alpha = 0.85)"],
    ["cl", "Closeness"],
    ["bt", "Betweenness"],
    ["distancias", "Distancias"],
]

result = {}
    
# outra abordagem, loop por metrica e dataset
for i, (metric_name, titulo) in enumerate(metrics):
    result[metric_name] = {}
    
    for file_name, _ in grafos:

        #print("arquivo lido", file_name)
        dataset_name = file_name[:file_name.find('.')]

        # tamanho componentes conexas
        metric_filename = "_".join([dataset_name,metric_name])
        
        metric_array = np.load(metric_filename+".npy")

        result[metric_name][dataset_name] = {}
        
        if metric_name == 'cl':
            # retira valores indefinidos de closeness (correto?)
            metric_array = metric_array[~np.isnan(metric_array)]
        
        result[metric_name][dataset_name]["max"] = np.max(metric_array)
        result[metric_name][dataset_name]["min"] =  np.min(metric_array)
        result[metric_name][dataset_name]["mean"] =  np.mean(metric_array)
        result[metric_name][dataset_name]["median"] =  np.median(metric_array)
        result[metric_name][dataset_name]["std"] =  np.std(metric_array)
        
        # metricas comparativas
        
        if metric_name == 'lc':
            n = metric_array.shape[0]
            print(n)
            m = np.load(dataset_name+"_n_edges.npy")[0]
            print(m)
            result[metric_name][dataset_name]['density'] = 2*m/(n*(n-1))
            
        if metric_name == 'tamanho_cc':
            result[metric_name][dataset_name]["tamanho"] = metric_array.shape[0]
            result[metric_name][dataset_name]["percentual_max_cc"] = np.max(metric_array)/np.sum(metric_array)
        
        if metric_name == 'distancias':
            metric_filename = "_".join([dataset_name,"lc"])
            n = np.load(metric_filename+".npy").shape[0]
            result[metric_name][dataset_name]["n_nos"] = n


        print(result[metric_name])

# gerar tabelas latex
# jinja ou print? print
dic = {
    'max': "Valor Máximo",
    'min': "Valor Mínimo",
    'mean': "Média",
    'median': "Mediana",
    "std": "Desvio Padrão",
    "density": "Densidade",
    "tamanho": "Tamanho da maior c.c.",
    "percentual_max_cc": "Percentual de nós na maior c.c.",
    "n_nos": " \# de nós do grafo"
}

for metric_name, nome_metrica in metrics:
    desc = "c | "+" | ".join(["c" for valor in result[metric_name]['protein']])
    primeira_linha = "\\begin{tabular}{%s}" % (desc)
    print(primeira_linha)
    headers = "Rede & "+ " & ".join([dic[k] for k in result[metric_name]["protein"]])+" \\\\"
    print(headers)
    print("\\hline")
    for k in result[metric_name]:
        linha = k + " & "+" & ".join(["%.4f" % (v) for k,v in result[metric_name][k].items()])+" \\\\"
        print(linha)
    print("\\end{tabular}")
    print("\caption{%s}" % nome_metrica)





# In[ ]:




