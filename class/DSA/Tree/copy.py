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

     
     #-------------------------------------------------------------------------------------------------               
          
    def remove_node(self, value):
        node_to_remove = self.find_node_by_value(self.root, value)
        if node_to_remove is None:
            print("Node with value '{}' not found in the tree".format(value))
            return

        parent = node_to_remove.parent
        if parent is None:  # Node to remove is the root
            self.clear_tree()
            return

        parent.children.remove(node_to_remove)
        node_to_remove.parent = None
        print("Node with value '{}' removed from the tree".format(value))

    def find_immediate_common_ancestor(self, value1, value2):
        node1 = self.find_node_by_value(self.root, value1)
        node2 = self.find_node_by_value(self.root, value2)
        if node1 is None or node2 is None:
            print("One or both of the nodes not found in the tree")
            return None

        ancestors1 = set()
        while node1 is not None:
            ancestors1.add(node1)
            node1 = node1.parent

        while node2 is not None:
            if node2 in ancestors1:
                return node2
            node2 = node2.parent
        return None

    def path_to_node(self, value):
        node = self.find_node_by_value(self.root, value)
        if node is None:
            print("Node with value '{}' not found in the tree".format(value))
            return []

        path = []
        while node is not None:
            path.append(node.value)
            node = node.parent
        return path[::-1]

    def depth_of_node(self, value):
        node = self.find_node_by_value(self.root, value)
        if node is None:
            print("Node with value '{}' not found in the tree".format(value))
            return -1  # Indicates node not found
        return self.depth(node)

    def height_of_tree(self):
        if self.is_empty():
            return 0
        return self.height(self.root)

    def pre_order_traversal(self):
        def traverse(node):
            if node is None:
                return
            print(node.value, end=" ")
            for child in node.children:
                traverse(child)

        traverse(self.root)
        print()

    def post_order_traversal(self):
        def traverse(node):
            if node is None:
                return
            for child in node.children:
                traverse(child)
            print(node.value, end=" ")

        traverse(self.root)
        print()

    def breadth_first_traversal(self):
        if self.is_empty():
            return ""
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")
            queue.extend(node.children)
        print()

    def count_nodes(self):
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
tree.add_children(g,[Node('x'), Node('y'), Node('z')]) 





tree._print_node(tree.root, 0)
print(tree.count_nodes())
print(tree.breadth_first_traversal())
print(tree.post_order_traversal())
print(tree.pre_order_traversal())
print(tree.height_of_tree())
print(tree.depth_of_node("A"))

print(tree.find_node_by_value(root,"x").value)