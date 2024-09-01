# Data Structures: Linked List and Stack Implementations

This repository contains Python implementations of two fundamental data structures: Linked List and Stack. Each implementation includes detailed comments explaining the functionality of the code.

## Table of Contents
1. [Linked List Implementation](#linked-list-implementation)
2. [Stack Implementation](#stack-implementation)
3. [Assignments](#assignments)

## Linked List Implementation

The `LinkedList` class provides a basic implementation of a singly linked list. It includes the following methods:

- `append(data)`: Add a new node with the given data to the end of the list
- `remove(data)`: Remove the first occurrence of a node with the specified data
- `display()`: Print the contents of the list

### Usage Example

```python
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print(linked_list.display())

linked_list.remove(2)
print("\nAfter removing 2:")
linked_list.display()
```

## Stack Implementation

The `Stack` class provides a basic implementation of a stack data structure using a linked list. It includes the following methods:

- `empty()`: Check if the stack is empty
- `size()`: Get the current size of the stack
- `push(data)`: Add an element to the top of the stack
- `top()`: Return the top element of the stack without removing it
- `pop()`: Remove and return the top element from the stack

### Usage Example

```python
stack = Stack()

print(f'Stack is empty: {stack.empty()}')
print(f'Stack size: {stack.size()}')

stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)

print(f'Stack is empty: {stack.empty()}')
print(f'Stack size: {stack.size()}')

print(stack.pop())
print(f'Stack size: {stack.size()}')
print(stack.pop())
print(f'Stack size: {stack.size()}')
```

## Assignments

### Assignment 1: Code Comments

The provided code for both the Linked List and Stack implementations already includes detailed comments explaining the functionality of each section. These comments provide insight into the purpose and operation of the code.

### Assignment 2: Value Deletion in Linked Lists

The `remove(data)` method in the `LinkedList` class already implements the logic for deleting a node with a specific value from the linked list. This method:

1. Searches for the first occurrence of the specified value in the list
2. If found, removes the node containing that value from the list
3. Updates the necessary pointers to maintain the integrity of the list
4. Handles edge cases, such as deleting the head node or when the value is not found in the list

## Contributing

Feel free to submit pull requests or open issues to improve the implementations or assignments.

## License

[Mit]