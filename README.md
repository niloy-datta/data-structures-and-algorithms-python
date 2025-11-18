# Data Structures & Algorithms (DSA) in Python

Complete, clean, and topic-wise implementation of fundamental Data Structures and Algorithms in Python.

---

## 📁 Directory Structure

```
dsa/
└── python/
    ├── 01_Time_and_Space_Complexity/
    ├── 02_Vector_Dynamic_Array/
    ├── 03_Prefix_Sum_and_Binary_Search/
    ├── 04_Singly_Linked_List_Basics/
    ├── 05_Singly_Linked_List_Operations/
    ├── 06_Singly_Linked_List_Deletion_and_Sorting/
    ├── 07_Doubly_Linked_List/
    ├── 08_STL_List_and_Cycle_Detection/
    ├── 09_Linked_List_LeetCode_Problems/
    ├── 10_Stack_Implementation/
    ├── 11_Queue_Implementation/
    ├── 12_Stack_and_Queue_Problems/
    ├── 13_Binary_Tree_Traversals/
    ├── 14_Binary_Tree_Operations/
    ├── 15_Binary_Tree_Problems/
    ├── 16_Binary_Search_Tree_BST/
    ├── 17_Heap_Implementation/
    └── 18_Set_Map_Priority_Queue/
```

---

## 📑 Topics & Modules

| No. | Topic Name | Directory | Description |
| :---: | :--- | :--- | :--- |
| **01** | **Time & Space Complexity** | [`python/01_Time_and_Space_Complexity`](python/01_Time_and_Space_Complexity) | $O(1)$, $O(N)$, $O(\log N)$, $O(N \log N)$, $O(N^2)$, $O(\sqrt{N})$ analysis |
| **02** | **Dynamic Array & Vector** | [`python/02_Vector_Dynamic_Array`](python/02_Vector_Dynamic_Array) | Dynamic sizing, capacity growth, modifiers, and string vectors |
| **03** | **Prefix Sum & Binary Search** | [`python/03_Prefix_Sum_and_Binary_Search`](python/03_Prefix_Sum_and_Binary_Search) | Cumulative prefix sum arrays and iterative binary search |
| **04** | **Singly Linked List Basics** | [`python/04_Singly_Linked_List_Basics`](python/04_Singly_Linked_List_Basics) | Node class creation, dynamic chaining, and sequential traversal |
| **05** | **Singly Linked List Operations** | [`python/05_Singly_Linked_List_Operations`](python/05_Singly_Linked_List_Operations) | Insert at head, insert at tail (optimized), insert at arbitrary index, reverse print |
| **06** | **Linked List Deletion & Sorting** | [`python/06_Singly_Linked_List_Deletion_and_Sorting`](python/06_Singly_Linked_List_Deletion_and_Sorting) | Delete head, delete tail, delete at index, stream input, bubble sort on list |
| **07** | **Doubly Linked List** | [`python/07_Doubly_Linked_List`](python/07_Doubly_Linked_List) | Bidirectional nodes (`prev`, `next`), insertion, and deletion |
| **08** | **List & Cycle Detection** | [`python/08_STL_List_and_Cycle_Detection`](python/08_STL_List_and_Cycle_Detection) | Floyd's Cycle-Finding Algorithm (Tortoise and Hare), list reversing |
| **09** | **Linked List Problem Solutions** | [`python/09_Linked_List_LeetCode_Problems`](python/09_Linked_List_LeetCode_Problems) | Middle node, palindrome linked list, remove duplicates, reverse linked list |
| **10** | **Stack Implementation** | [`python/10_Stack_Implementation`](python/10_Stack_Implementation) | LIFO implementations using dynamic array, doubly linked list, and collections |
| **11** | **Queue Implementation** | [`python/11_Queue_Implementation`](python/11_Queue_Implementation) | FIFO implementations using singly/doubly linked list, queue using stacks, stack using queues |
| **12** | **Stack & Queue Problems** | [`python/12_Stack_and_Queue_Problems`](python/12_Stack_and_Queue_Problems) | Valid parentheses, min stack, backspace string compare, insert at bottom |
| **13** | **Binary Tree Traversals** | [`python/13_Binary_Tree_Traversals`](python/13_Binary_Tree_Traversals) | Pre-order, In-order, and Post-order depth-first traversals |
| **14** | **Binary Tree Operations** | [`python/14_Binary_Tree_Operations`](python/14_Binary_Tree_Operations) | Level-order BFS traversal, tree input parser, max height, node & leaf counting |
| **15** | **Binary Tree Problems** | [`python/15_Binary_Tree_Problems`](python/15_Binary_Tree_Problems) | Diameter of tree, reverse level order, left view, node level search |
| **16** | **Binary Search Tree (BST)** | [`python/16_Binary_Search_Tree_BST`](python/16_Binary_Search_Tree_BST) | BST insertion, search in $O(\log N)$, sorted array to balanced BST |
| **17** | **Heap Implementation** | [`python/17_Heap_Implementation`](python/17_Heap_Implementation) | Max-heap & min-heap insert and delete with array heapify |
| **18** | **Set, Map & Priority Queue** | [`python/18_Set_Map_Priority_Queue`](python/18_Set_Map_Priority_Queue) | Hash maps, frequency counter, sorted set, priority queue with custom comparators |

---

## ⚡ How to Run

Run any Python script directly with:

```powershell
python "python/01_Time_and_Space_Complexity/sum.py"
```

For programs expecting standard input, provide inputs interactively or via terminal pipe:

```powershell
"10" | python "python/01_Time_and_Space_Complexity/sum.py"
```

Example for Binary Tree / BST input:

```powershell
"10 5 15 2 6 -1 -1 -1 -1 -1 -1 6" | python "python/16_Binary_Search_Tree_BST/search_in_BST.py"
```
