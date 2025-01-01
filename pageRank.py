class Node:
    def __init__(self,name):
        self.name=name
        self.parents=[]
        self.children=[]
        self.auth=1.0
        self.hub=1.0
        self.pagerank=1.0

    def link_child(self, new_child):
        for child in self.children:
            if child.name is new_child.name:
                return
        self.children.append(new_child)

    def link_parent(self, new_parent):
        for parent in self.parents:
            if parent.name is new_parent.name:
                return
        self.parents.append(new_parent)


class Graph:
    def __init__(self):
        self.nodes=[]

    def contains(self,name):
        for node in self.nodes:
            if node.name is name:
                return True
        return False

    def find(self,name):
        if self.contains(name):
            return next(node for node in self.nodes if node.name is name)
        else:
            node=Node(name)
            self.nodes.append(node)
            return node

    def add_edges(self,parent,child):
        parent_node=self.find(parent)
        child_node=self.find(child)

        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    def sort_nodes(self):
        self.nodes.sort(key=lambda x:int(x.name))

import configparser
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
indexes=['html1','html2','html3']
config['DEFAULT']={f"{n}":'index'+i[-1]+'.html' for n,i in enumerate(indexes,1)}
html_links=[]
with open('config.ini','w+') as configfile:
    config.write(configfile)

config.read('config.ini')
for i in range(1,4):
    html_file=config.get('DEFAULT',str(i))

    with open(html_file,'r',encoding='utf-8') as file:
        soup=BeautifulSoup(file,'html.parser')
        for a in soup.findAll('a',href=True):
            html_links+=[(a['href'],html_file)]
            # if i not in html_links:
            #     html_links[i]=[]
            # html_links[i]+=[a['href']]

html_links=[(m.split('.')[0][-1],n.split('.')[0][-1]) for m,n in html_links]

print(html_links)

graph=Graph()
for p,c in html_links:
    graph.add_edges(p,c)

graph.sort_nodes()
print(graph.nodes[1].name)

for node in graph.nodes:
    node.pagerank=sum(p.pagerank/len(p.children) for p in node.parents)

print([node.pagerank for node in graph.nodes])


def sum_timesheet(path):
    all_times=[]
    try:
        with open(path,"r") as sheet:
            # print(sh)
            for line in sheet:
                times=line.strip().split(',')
                print(times)
    #             convert times
                for t in times:
                    io=t.strip().split('-')
                    spent=0
                    if len(io)>1 and all((_).isdigit for _ in io):
                        h1=int(io[1].split(':')[0])
                        h2=int(io[0].split(':')[0])
                        min1=int(io[1].split(':')[1]) if ':' in io[1] else 0
                        min2=int(io[0].split(':')[1]) if ':' in io[0] else 0
                        
        #                 account for pm and millitary times
                        h1=h1 if h1>=h2 else h1+12
                        spent1=h1-h2
                        spent2=min1-min2
                        spent=spent1+(spent2/60)
                    all_times+=[spent]
    except:
        pass
    return sum(all_times)
            
print(sum_timesheet('jan.txt'))