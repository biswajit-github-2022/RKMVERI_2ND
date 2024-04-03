from anytree import Node, RenderTree

# Creating nodes
root = Node("A")
b = Node("B", parent=root)
c = Node("C", parent=root)
d = Node("D", parent=b)
e = Node("E", parent=b)
f = Node("F", parent=c)

# Rendering the tree
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
