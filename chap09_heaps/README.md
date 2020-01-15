### Terms
- *Binary Tree*
    > Simply put, a tree data structure in which each node has at most *two* children.
- *Complete Binary Tree*
    > Simply put, a *Binary Tree* with all levels are completely filled <small>(wtf? well, *filled* means it has *something* aka. *child node*</small> **except** the last level, and the last level has all keys *as left as possible* <small>(it means the *leaf node* are **mostly** *left child*)</small>.
- Difference between *Binary Tree* and *Binary Search Tree*
    > Binary Tree: not many rules in comparison to the latter.<br>
    > Binary Search Tree: the <u>*left*|*right*</u> child node is always <u>*smaller*|*larger*</u> than the parent node.

### About *heap*
- *Heap* <small>(data structure)</small>
    > A *Heap* is a special tree-based data structure in which the tree is a *complete binary tree*. What we're gonna implement is called *Binary Heap*. Generally, it can be of two types: *Min Heap* & *Max Heap*.
    >> The rules? Well, think of it as *the ages in your family*, the top|root is your *parents* <small>(treat it as one for now)</small>, the level two is you and your *sisters or brothers*, then the level three is the *child* part. That's basically it.<br>

    > Another way of putting it
    >> The rules in the *Binary Search Tree* is <u>[PARENT => L: smaller, R: larger]</u>, as for the *Heap*, it has two parts, <u>first</u>, all the *"root" node* <small>(not just the top)</small> must be larger <small>(Max-Heap)</small> or smaller <small>(Min-Heap)</small> than all of its *child*<small>(ren)</small>, <u>second</u>, the first rule must be **recursively true**.

    > Lastly
    >> ![Max-Heap and Min-Heap](./images/min_heap_and_max_heap.png)

- Characteristics
    1. *Heaps* are useful when it is necessary to *repeatedly* <u>remove</u> the *object with the highest/lowest priority*.
        > *Heaps* guarantee *the top element would be either the biggest or smalllest* element.
    2. *Heaps* are **not** good for *looking up values*, it would be no better than *linear search* <small>(aka. *slow*)</small>.
        > This is because there is *no ordering* of the elements within a heap *except* that *the largest or the smallest* value is on *top*. So you cannot determine where in a *heap* a value is located without searching the entire *heap*.
    3. *Heaps* could be used to implement *priority queue*.
        > Both of the *inserts* and *removals* only take `O(log N)` time.
    4. *Heaps* could be seen as *priority queue*, or being *referred to*.
        > It's because *heap* is one *maximally efficient* implementation of an *abstract data type* called a <q>priority queue</q>, regardless of how they're actually implemented.
    5. *Heaps* are commonly implemented as a *binary heap* **in** an *array*.
        > It requires a lot of index computations (an array VS tree-like data structure).

### References
- Terms
    - [Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)
    - [Binary Tree - Types of Binary Tree](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees) <small>(wikipedia)</small>
    - [Binary Tree - Types of Binary Tree](https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/) <small>(geekforgeeks)</small>
    - [Difference between Binary Tree and Binary Search Tree](https://www.geeksforgeeks.org/difference-between-binary-tree-and-binary-search-tree/)
    - [Difference between “Complete binary tree”, “strict binary tree”,“full binary Tree”?](https://stackoverflow.com/questions/12359660/difference-between-complete-binary-tree-strict-binary-tree-full-binary-tre)
- About *heap*
    - [Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)
