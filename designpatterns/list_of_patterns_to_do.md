# List of patterns to do

https://en.wikipedia.org/wiki/Software_design_pattern

- [x] strategy: keeps behavior flexible yet reusable for subclasses; imo, in Python, might as well pass functions as objects
- [x] observer: has a publisher change state as needed for multiple other subscriber instances with no action needed for the subscriber classes
- [x] decorator: accrues wrapped changes to a certain class, e.g. adding ingredients to a beverage
    - [ ] Python-specific function decorators
- [x] factory method: an approach of choice for deep if/elif/else methods for creating subclasses/different specific methods to determine more specific behavior rather than defining all of that in one concrete class/method
- [x] abstract factory: uses multiple factories implementing one interface if one factory method is not sufficient to simplify creation logic
- [x] singleton: ensures that only a single instance of a certain class is ever used. can be useful for performance improvement or general global state management
- [x] command: method of separating concerns, like UI layer from business logic
- [x] builder: simplifies construction of objects that take in lots of optional parameters in constructor
- [x] adapter: makes a class give data in a format like another existing class

Others I might do:

- [ ] dependency injection
- [ ] lazy initialization
- [ ] multiton
- [ ] object pool
- [ ] prototype
- [ ] raii
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
- [ ] iterator
- [ ] chain of responsibility
- [ ] iterator
- [ ] mediator
- [ ] memento
- [ ] state
- [ ] template method
- [ ] visitor

