### Chapter Goals
> This chapter introduces trees and some algorithms that use trees. By the end of the chapter you should be able to answer these questions.
- How are trees constructed?
- How can we traverse a tree?
- How are expressions and trees related?
- What is a binary search tree?
- Under what conditions is a binary search tree useful?
- What is depth first search and how does it relate to trees and search problems? - What are the three types of tree traversals we can do on binary trees?
- What is a grammar and what can we do with a grammar?

### Confusions
- [*Pre-order traversal* versus *Depth-first search*](https://softwareengineering.stackexchange.com/questions/227779/is-pre-order-traversal-same-as-depth-first-search)

### Terminology summary <small>([*ref*](https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/))</small>
- *Root* is the topmost `node` of the tree
- *Edge* is the link between two `nodes`
- *Child* is a `node` that has a `parent node`
- *Parent* is a `node` that has an `edge` to a `child node`
- *Leaf* is a `node` that does not have a child node in the `tree`
- *Height* is the length of the longest path to a `leaf`
- *Depth* is the length of the path to its `root`

### Types of *search*
- *Depth-First* Search <small>(aka. DFS)</small>
    - It is an algorithm for *traversing* or *searching* <u>tree data structure</u>
        > 1) one starts at the root & explores AFAP along each branch before backtracking<br>
        > 2) the process is the *same* as the <u>pre-order traversal</u>
    - Types of *tree traversals*
        - `pre-order`
            > TOP -> LEFT -> LEFT .. THE_REST -> RIGHT -> LEFT .. THE_REST

        - `in-order`
            > BOTTOM -> LEFT|MIDDLE|RIGHT -> .. TOP .. -> LEFT|MIDDLE|RIGHT

        - `post-order`
            > BOTTOM -> LEFT|RIGHT|MIDDLE -> LEFT|MIDDLE|RIGHT -> .. TOP

- *Breadth-First* Search <small>(aka. BFS)</small>
    - It is an algorithm for *traversing* or *searching* <u>tree data structure</u>
        > <q>it starts at the tree root & explores explores the neighbor nodes first, before
        moving to the next level neighbours</q>
        >> ![Example of DFS and BFS](./images/example_of_DFS_BFS.jpg)
