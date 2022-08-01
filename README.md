# comp-sci-refresher-in-python
Self-review of comp-sci concepts I definitely learned in school. Sometimes details get fuzzy, okay?

Each file should be pretty self-contained and I'm going to try not to use any external libraries. That should mean, for example, that you can just call each file like:

```
python3 path/to/file.py
```

and see something happening.

## List of patterns to do

https://en.wikipedia.org/wiki/Software_design_pattern

Creational:

- [x] factory method: an approach of choice for deep if/elif/else methods for creating subclasses/different specific methods to determine more specific behavior rather than defining all of that in one concrete class/method
- [x] abstract factory: uses multiple factories implementing one interface if one factory method is not sufficient to simplify creation logic
- [x] singleton: ensures that only a single instance of a certain class is ever used. can be useful for performance improvement or general global state management
- [x] builder: simplifies construction of objects that take in lots of optional parameters in constructor
- [ ] prototype
- [ ] dependency injection
- [ ] lazy initialization
- [ ] multiton
- [ ] object pool
- [ ] raii

Structural:

- [x] adapter: makes a class give data in a format like another existing class
- [x] decorator: accrues wrapped changes to a certain class, e.g. adding ingredients to a beverage
    - [ ] Python-specific function decorators
- [ ] composite
- [ ] bridge
- [ ] extension object
- [ ] facade
- [ ] flyweight
- [ ] front controller
- [ ] marker
- [ ] module
- [ ] proxy
- [ ] twin

Behavioral:

- [x] strategy: keeps behavior flexible yet reusable for subclasses; imo, in Python, might as well pass functions as objects
- [x] observer: has a publisher change state as needed for multiple other subscriber instances with no action needed for the subscriber classes
- [x] command: method of separating concerns, like UI layer from business logic
- [ ] iterator
- [ ] chain of responsibility
- [ ] iterator
- [ ] mediator
- [ ] memento
- [ ] state
- [ ] template method
- [ ] visitor

## Data structures to review

https://en.wikipedia.org/wiki/List_of_data_structures#Trees

- [x] queue
- [x] stack
- [x] linked list
    - [ ] circular
    - [x] doubly-linked
- [ ] bst
- [ ] heap/priority queue
- [ ] graph

## Algorithms to review

https://en.wikipedia.org/wiki/List_of_algorithms

- [ ] sorting algorithms (various types)
    - [x] selection sort: swaps min values from right unsorted section to left; left side is fully sorted
    - [x] bubble sort: compares neighbors, switching if order is wrong; right side is fully sorted ("bubbled up")
    - [ ] insertion sort
    - [ ] merge sort
    - [ ] quicksort
    - [ ] heapsort
    - [ ] radix sort
    - [ ] bucket sort
    - [ ] iterative heapsort
    - [ ] counting sort
- [ ] binary search
- [x] tree traversals
    - [x] inorder
    - [x] preorder
    - [x] postorder
- [ ] breadth first search
- [ ] depth first search
- [ ] kruskal minimum spanning tree
- [ ] dijkstra
