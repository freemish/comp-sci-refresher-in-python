# comp-sci-refresher-in-python

Self-review of comp-sci concepts I definitely learned in school. Sometimes details get fuzzy, okay?

This repository uses no external dependencies other than Python itself. You can run each file like:

```
python3 path/to/file.py
```

## List of patterns to do

https://en.wikipedia.org/wiki/Software_design_pattern

Creational:

- [x] factory method: an approach of choice for deep if/elif/else methods for creating subclasses/different specific methods to determine more specific behavior rather than defining all of that in one concrete class/method
- [x] abstract factory: uses multiple factories implementing one interface if one factory method is not sufficient to simplify creation logic
- [x] singleton: ensures that only a single instance of a certain class is ever used. can be useful for performance improvement or general global state management
- [x] builder: simplifies construction of objects that take in lots of optional parameters in constructor
- [x] prototype: simplifies constructing objects via copying existing "prototypes"
- [x] dependency injection: objects no longer are responsible for creating dependencies; all dependencies of a class are "injected" (provided as arguments) upon initialization
- [x] lazy initialization: don't calculate value of an object property until it is accessed
- [x] multiton: like the singleton except that it may manage creating multiple instances of the class in certain conditions, like if providing some special argument when initializing
- [x] object pool: initializes a limited number of expensive objects to be loaned out and reused; works well for performance with multiple threads so that no two threads are using the same object at the same time
- [x] raii (resource acquisition is initialization): see object pool thread function; the code that locks the resource must include the logic that the lock will be released when execution leaves the scope of the RAII object

Structural:

- [x] adapter: makes a class give data in a format like another existing class
- [x] decorator: accrues wrapped changes to a certain class, e.g. adding ingredients to a beverage
- [x] composite: for cases when whether an object is a simple object or is a container for simple objects (composite object), it needs to be treated the same way
- [x] bridge: separates a portion of a complicated class into a "has-a" relationship to another class
- [x] extension object: plan for some functionality in an object to be extended dynamically
- [x] facade: encapsulates more complex logic in one or more classes with multiple methods; provides a convenient interface at the cost of obscuring potential complex uses of subsystems
- [x] flyweight: reuse a few heavyweight objects to generate many unique objects that share those properties
- [x] proxy: provide an interface over an existing concrete API class and implement that interface with a proxy class that has an instance of the concrete API class; allows for simplicity of introducing changes to how the API class works or using alternative API classes with minimized code rewrite

Behavioral:

- [x] strategy: keeps behavior flexible yet reusable for subclasses; imo, in Python, might as well pass functions as objects
- [x] observer: has a publisher change state as needed for multiple other subscriber instances with no action needed for the subscriber classes
- [x] command: method of separating concerns, like UI layer from business logic
- [x] iterator: encapsulates any specific implementation of iterable (e.g. queue, list, tuple, dict, tree, etc.)
- [x] chain of responsibility: builds a linked list of handler objects that process a request; handling of the request only needs to be invoked once
- [x] mediator: trigger other components of a system without their being tightly coupled to each other (best for when there are many components to manage)
- [x] memento: allows creation and restoration of save states
- [x] state: delegates state-specific branching logic within the context of a complex class to reduce nested if-elses
- [x] template method: specify a method on a base class that links multiple abstract methods in a desired order; implement abstract methods in subclasses
- [x] visitor: have classes implement a method that accepts a different "visitor" class that contains more specific branching logic in multiple methods

Other:

- [ ] front controller
- [ ] marker
- [ ] module
- [ ] data access object
- [ ] model-view-controller
- [ ] business delegate
- [ ] filter
- [ ] interpreter
- [ ] service locator

## Data structures to review

https://en.wikipedia.org/wiki/List_of_data_structures#Trees

- [x] queue
- [x] stack
- [x] linked list
    - [x] circular
    - [x] doubly-linked
- [x] bst
- [x] heap/priority queue
- [x] graph

## Algorithms to review

https://en.wikipedia.org/wiki/List_of_algorithms

- [ ] sorting algorithms (various types)
    - [x] selection sort: swaps min values from right unsorted section to left; left side is fully sorted
    - [x] bubble sort: compares neighbors, switching if order is wrong; right side is fully sorted ("bubbled up")
    - [x] insertion sort: iterating rightward, treats left side as fully sorted and inserts unsorted value into sorted list on left
    - [x] tree sort: done as part of binary search tree demo
    - [ ] merge sort
    - [ ] quicksort
    - [ ] heapsort
    - [ ] radix sort
    - [ ] bucket sort
    - [ ] iterative heapsort
    - [ ] counting sort
- [x] binary search
- [ ] breadth first search
- [ ] depth first search
- [x] tree traversals
    - [x] inorder
    - [x] preorder
    - [x] postorder
- [ ] kruskal minimum spanning tree
- [ ] dijkstra

## Bonus stuff

- [x] monads
- [x] closures
- [ ] Python-specific function decorators
- [x] threading; see object pool exercise
- [x] udp demo
- [x] english words passphrase generator
- [x] Python namespace importing
