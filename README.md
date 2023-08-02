# DataStructure
Data Structure Learning Materials

My DATASTRUCTURE FILES FROM PERSONAL LEARNING

Big o notation looks at the wort case scenairo.
Binary search works in logarithimic time.

A static array is a fixed Length container containing n elements indexable from the range [0, n-1]

When and where is a static array used:
1- Storing and accesing sequentioal data
2 - Temprarily storing objects
3 - used by IO routines as buffers
4 - Lookup tables and inverse lookup tables
5 - Can be used to return multiple values from a function
6 - Used in dynamic programming to cache answers to subproblems
Dynamc array can grow and shrink in size.
A Linked List is a sequential list of nodes that hold data which point to other nodes also containing data.

Where are Linked Lists used:

1 - Used in many List, Queue and Stack implementations.
2- Great for creating circular Lists (Making pointer of the last node points to the first node, Circular list are used to model repeating event circles.
3 -  Can easily model real world objects such as trains.
4 - Used in seperate chaining which is present certain Hashtable implementations to deal with hashing collisions
5 - Often used in the implementation of adjacency Lists for graphs. 

Terminologies in Linked List:
Head : The first node in a Linked List.
Tail: The last node in a Linked List.
Pointer: Reference to another node.
Node: AN object containing data and pointer(s)

Single vs double Linked List:
Single linked lists only hold a reference to teh next node while double linked list holds a reference to the next and previos node.

A stack is a one-ended linear data structure which models a real world stack by having two primary operations namely push and pop. Stack uses the Last in First out (LIFO)

When and where is a stack used:
1 -  Used by undo mechanisms in text editors
2 - Used in compiler syntax checking for matchinf brackets and braces.
3 - Can be used to model a pile of books or plates.
4 - Used behind the scenes to support recursion by keeping track of previous function calls.
5 - Can be used to do a Depth First Search on a gaph.
6 - Used in browsers to navigate forward and backward.

A Queue is a linear data structure which models real world queues by having two primary operations namely enqueue and dequeue.
Adding element from the back is called enqueuing while and removing element from the front is Dequeuing. Enqueue = Adding = Offering while dequeue = Polling.

When and where is a Queue used? :
1 - Any waiting line models a queue, for example a lineup at a movie theatre.

2 - Can be used to efficiently keep track of the x most recently added elements.

3 - Web server request management where you want first come first serve.

4 - Breadth first search (BFS) graphs traversal

Queue uses the First in First out (FIFO)

A Priority Queue is an Abstract data type that operates similar to a normal queue except that 
each element has a certain priority. The priority of the elements in the priority queue determine the order in which elements are removed from the Priority Queue (PQ). Note: Priority Queue only supports comparable data, meaning the data inserted into the priority queue must be able to be ordered in some way eitheir from least to greatest or greatest to least. This is so that we are able to assign relative priorities to each element. Priority Queue uses a heap.

A heap is a tree based Data Structure that satisfies the heap invariant (also called property): If A is a parent node of B then A is ordered with respect to B for all nodes A, B in the heap. 


When and where is a priority Queu used

1 - Used in certain implementation of Dijkstra's Shortest Path algorithm

2 - ANytime you need the dynamically fetch the 'next best' or 'next worst' element.

3 - Used in Hiffman coding (which is often used for lossless data compression). 

4 - Best First Search (BFS) algorithms such as A*  use PQS to continuosly grab the next most promising node

5 - Used by Minimum Spanning Tree (MST) algoithms

When we remove the root in binary heap it is called polling 

Union Find is a data structure that keeps track of elements which are split into one or more disjoint sets. It has two primary operations: find and union. 

WHere and when is a Union Find used? 

Kruskal's minimum spanning tree algorithim.
Grid Percolation
Network connectivity
Least common ancestor in tress
Image Processing .

A tree is an undirected graph which satisfies any of the following definitions:
- An acyclic connected graph ( Acyclic means there are no cycles)
- A connected graph with N nodes and N-1 edges
- A graph in which any two vertices are connected by exactly one path.

A leaf node is a node with no childern.

A child is a node extending from another node. A parent is the inverse of this .

A subtree is a tree entirely contained within another tree. They are usually denoted using triangles.

A binary tree is a tree for which every node has at most two child nodes.

A binary search tree is a bainary tree that satisfies the BST invariant: left subtree has smaller element and right subtree has larger elements. 

When and wehre are Biary Trees used:

- Binary search trees (BST):
	- implementation of some map and set ADT
	- Red Black Trees
	- AVL Trees
	- Splay Trees
 
-  used in the implementation of binary heaps .
Syntac trees ( used by compulers and calculator).

- Treap - a probabilistic DS (uses a randomized BST)

There are three types of traversal they are  preorder, inorder and postorder.

Level order traversal: In a level order traversal we want to print the node as they appear one layer at a time. 
