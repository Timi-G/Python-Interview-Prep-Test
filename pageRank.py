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
            if child.name == new_child.name:
                return
        self.children.append(new_child)

    def link_parent(self, new_parent):
        for parent in self.parents:
            if parent.name == new_parent.name:
                return
        self.parents.append(new_parent)


class Graph:
    def __init__(self):
        self.nodes=[]

    def contains(self,name):
        for node in self.nodes:
            if node.name == name:
                return True
        return False

    def find(self,name):
        if self.contains(name):
            return next(node for node in self.nodes if node.name==name)
        else:
            node=Node(name)
            self.nodes.append(node)
            return node

    def add_edges(self,parent,child):
        parent_node=self.find(parent)
        child_node=self.find(child)

        parent_node.link_parent(parent_node)
        child_node.link_child(child_node)
