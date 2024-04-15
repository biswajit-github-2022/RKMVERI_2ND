class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None

    def add_root(self, value):
        if self.root is not None:
            raise ValueError("Root already exists")
        self.root = Node(value)
        return self.root

    def add_child(self, parent_node, value):
        
        if parent_node is None:
            raise ValueError("Parent node is invalid")
        child = Node(value)
        child.parent = parent_node
        parent_node.children.append(child)
        return child

    def add_children(self, parent_node, children):
        
        if parent_node is None:
            raise ValueError("Parent node is invalid")
        parent_node.children.extend(children) 
        for i in children:
            i.parent=parent_node       

    
    def find_node_by_value(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found_node = self.find_node_by_value(child, value)
            if found_node:
                return found_node
        return None

    def is_empty(self):
        return self.root is None

    def depth(self, node):
        if node is None:
            return 0
        # if node.parent is None:
        #     return 0
        return 1+ self.depth(node.parent)

    def height(self, node):
        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(self.height(child) for child in node.children)

    def is_leaf(self, node):
        return not node.children



    def clear_tree(self):
        self.root = None
        
        

    def _print_node(self, node, level):
        print("  " * level + str(node.value))
        for child in node.children:
            self._print_node(child, level + 1)

     
#//////////////////////////////////////////////////////////////////////////////////////////      
          
    def remove_node(self, value):
        "Removes a node from the tree and returns the `value`"
        node_to_remove = self.find_node_by_value(self.root, value)
        if node_to_remove is None:
            raise Exception(f"Node with value '{value}' not found in the tree")
        parent = node_to_remove.parent
        if parent is None: 
            self.clear_tree()
            return "Node (root) is removed"
        parent.children.remove(node_to_remove)
        node_to_remove.parent = None
        return value

    def find_immediate_common_ancestor(self, value1, value2):
        "Returns `node1 & node2 , ancestor`"
        node1 = self.find_node_by_value(self.root, value1)
        node2 = self.find_node_by_value(self.root, value2)
        if node1 is None or node2 is None:
            raise Exception(f"One or both nodes are not found in the tree")
        ancestors1 = set()
        while node1 is not None:
            ancestors1.add(node1)
            node1 = node1.parent
        while node2 is not None:
            if node2 in ancestors1:
                return value1+" & "+value2, node2.value
            node2 = node2.parent
        return None

    def path_to_node(self, value):
        node = self.find_node_by_value(self.root, value)
        if node is None:
            raise Exception(f"Node with value '{value}' not found in the tree")
        path = []
        while node is not None:
            path.append(node.value)
            node = node.parent
        return path[::-1]

    def depth_of_node(self, value):
        "Returns `Value , Depth` of the node"
        node = self.find_node_by_value(self.root, value)
        if node is None:
            raise Exception(f"Node with value '{value}' not found in the tree")
        return value,self.depth(node)

    def height_of_tree(self):
        if self.is_empty():
            return 0
        return self.height(self.root)

    def pre_order_traversal(self):
        "Returns the `Pre order traversal` "
        traversal_result = []
        def traverse(node):
            if node is None:
                return
            if node.value is not None:
                traversal_result.append(node.value)
            for child in node.children:
                traverse(child)
        traverse(self.root)
        return ' '.join(traversal_result)


    def post_order_traversal(self):
        "Returns the `Post order traversal` "
        traversal_result = []
        def traverse(node):
            if node is None:
                return
            for child in node.children:
                traverse(child)
            if node.value is not None:
                traversal_result.append(node.value)
        traverse(self.root)
        return ' '.join(traversal_result)



    def breadth_first_traversal(self):
        "Returns a generator that yields the values in the tree in breadth-first order"
        if self.is_empty():
            return ""
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value is not None:
                yield node.value
            for child in node.children:
                if child.value is not None:
                    queue.append(child)

    def count_nodes(self):
        "Returns the `number of nodes` in the tree"
        def count(node):
            if node is None:
                return 0 
            total = 1
            for child in node.children:
                total += count(child)
            return total

        return count(self.root)

            
# Example usage:
tree = Tree()
root = tree.add_root("A")
b = tree.add_child(root, "B")
c = tree.add_child(root, "C")
d = tree.add_child(b, "D")
e = tree.add_child(b, "E")
f = tree.add_child(c, "F")
g = tree.add_child(c, "G")
x=Node("x")
y=Node("y")
z=Node("z")
tree.add_children(g,[x, y, z]) 





tree._print_node(tree.root, 0)

#//////////////////////////////////////////////////////////////////////////////
print("Node Count:")
print(tree.count_nodes())
print()
print("Breath First traversal:")
for node in tree.breadth_first_traversal():
    print(node, end=" ")
print()
print()
print("Post Order Traversal:")
print(tree.post_order_traversal())
print()
print("Pre Order Traversal:")
print(tree.pre_order_traversal())
print()
print("Height of tree:")
print(tree.height_of_tree())
print()
print("Depth of given node:")
print(tree.depth_of_node("x"))
print()
print("Path of a node from root:")
print(tree.path_to_node('x'))
print()
print("Immidiate ancestor of two nodes:")
print(tree.find_immediate_common_ancestor('D',"E"))
print()
print("Removal of Node:")
print(tree.remove_node("x"))
print()
#////////////////////////////////////////////////////////////////////////////