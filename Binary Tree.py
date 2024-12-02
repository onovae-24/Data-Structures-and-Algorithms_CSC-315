#Binary Tree Node Definition
# Definition of a Node class for a binary tree in Python
class Node:
    def __init__(self, data):
        self.data = data           # Store the node's value
        self.leftChild = None      # Pointer to the left child node
        self.rightChild = None     # Pointer to the right child node

#Insert Operation
# Function to insert a new node into the binary tree
def insert(root, data):
    # Create a new node with the provided data
    new_node = Node(data)
    
    # If the tree is empty, the new node becomes the root
    if root is None:
        return new_node

    current = root  # Start at the root of the tree

    while True:
        parent = current
        # Navigate to the left if data is less than the current node's data
        if data < current.data:
            if current.leftChild is None:
                current.leftChild = new_node  # Insert as the left child
                return root
            current = current.leftChild
        # Navigate to the right if data is greater than or equal to current node's data
        else:
            if current.rightChild is None:
                current.rightChild = new_node  # Insert as the right child
                return root
            current = current.rightChild

#Search Operation
# Function to search for a node with specified data in a binary tree
def search(root, data):
    current = root  # Start from the root of the tree
    print("Visiting elements:", end=" ")

    while current is not None:
        print(current.data, end=" ")  # Print the current node's data
        
        # If data is found, return the current node
        if current.data == data:
            return current
        # Navigate to the left if data is less than the current node's data
        elif data < current.data:
            current = current.leftChild
        # Navigate to the right if data is greater than the current node's data
        else:
            current = current.rightChild

    return None  # Return None if data is not found in the tree

#Tree Traversal (Preorder, Inorder, Postorder)
# Preorder traversal of a binary tree: Root, Left, Right
def pre_order_traversal(root):
    if root is not None:
        print(root.data, end=" ")           # Visit the root node
        pre_order_traversal(root.leftChild)  # Traverse the left subtree
        pre_order_traversal(root.rightChild) # Traverse the right subtree

# Inorder traversal: Left, Root, Right
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.leftChild)    # Traverse the left subtree
        print(root.data, end=" ")            # Visit the root node
        inorder_traversal(root.rightChild)   # Traverse the right subtree

# Postorder traversal: Left, Right, Root
def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.leftChild) # Traverse the left subtree
        post_order_traversal(root.rightChild) # Traverse the right subtree
        print(root.data, end=" ")             # Visit the root node

#Main Execution and Example Usage
# Sample data array to insert into the tree
array = [27, 14, 35, 10, 19, 31, 42]

# Create the root of the tree and insert each element
root = None
for data in array:
    root = insert(root, data)

# Perform traversals and display results
print("\nPreorder traversal: ", end="")
pre_order_traversal(root)
print("\nInorder traversal: ", end="")
inorder_traversal(root)
print("\nPostorder traversal: ", end="")
post_order_traversal(root)