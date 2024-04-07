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
        return 1 + self.depth(node.parent)

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
                    
          
    def remove_node(self, value):
        print('Implement a method to remove a node from the tree')

    def find_immediate_common_ancestor(self, value1, value2):
        print('Implement a method to find the immediate common ancestor of two nodes')

    def path_to_node(self, value):
        print('Implement a method to find the path from the root to a specific node')
  

    def depth_of_node(self, value):
        print('Implement a method to calculate the depth of a specific node')

    def height_of_tree(self):
        print('Implement a method to calculate the height of the tree')

    def pre_order_traversal(self):
        print('Implement a method of pre-order traversal')

    def post_order_traversal(self):
        print('Implement a method of post-order traversal')
        
      

    def breadth_first_traversal(self):
        print('Implement a method of breadth_first traversal')

    def count_nodes(self):
        print('Implement a method to count the total number of nodes in the tree')


            
# Example usage:
tree = Tree()
root = tree.add_root("A")
b = tree.add_child(root, "B")
c = tree.add_child(root, "C")
d = tree.add_child(b, "D")
e = tree.add_child(b, "E")
f = tree.add_child(c, "F")
g = tree.add_child(c, "G")
tree.add_children(g,[Node('x'), Node('y'), Node('z')]) 





tree._print_node(tree.root, 0)


