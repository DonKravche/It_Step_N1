# Binary Tree Implementation

This project implements a binary tree data structure in Python, with a focus on printing leaf nodes and counting edges.

## Features

- Binary tree creation and insertion
- Printing parent-child relationships
- Printing leaf nodes
- Counting edges in the tree

## Usage

To use this binary tree implementation:

1. Create a `BinaryTree` object:
   ```python
   binary_tree = BinaryTree()
   ```

2. Insert nodes into the tree:
   ```python
   binary_tree.insert(10)
   binary_tree.insert(15)
   binary_tree.insert(9)
   # ... insert more nodes as needed
   ```

3. Print the children of each node:
   ```python
   binary_tree.printChildren()
   ```

4. Print the leaf nodes:
   ```python
   binary_tree.printLeadNode()
   ```

5. Count the edges in the tree:
   ```python
   binary_tree.countEdges()
   ```

## Key Functions

### `printLeadNode()`

This function prints all the leaf nodes in the binary tree. A leaf node is a node that has no children (no left or right child).

#### Implementation Details:
- It uses a depth-first traversal to visit all nodes in the tree.
- When a node with no children is encountered, its key is printed.

### `countEdges()`

This function counts and prints the total number of edges in the binary tree.

#### Implementation Details:
- It counts the total number of nodes in the tree using a recursive helper function `_countNodes()`.
- The number of edges in a tree is always one less than the number of nodes (except for an empty tree).
- It prints and returns the count of edges.

## Note

The `printLeadNode()` function name seems to be a typo and should be `printLeafNode()` to accurately describe its functionality.

## Example Output

```
The Children Of Each Node Are
10 -> 9 15 
9 ->
15 -> 12 16 
12 ->
16 -> 17 
17 ->
The Leading Node Of Each Node Are: 
9 12 17 
The number of Edges in the tree is: 5
```

This output shows the children of each node, the leaf nodes (9, 12, and 17), and the total number of edges in the tree (5).