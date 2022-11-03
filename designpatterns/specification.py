"""
Demo of specification pattern.
See: 
    https://en.wikipedia.org/wiki/Specification_pattern
    https://gist.github.com/palankai/f73a18ce06751ab8f245
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: Any) -> bool:
        raise NotImplementedError()

    def __call__(self, candidate: Any) -> bool:
        return self.is_satisfied_by(candidate)

    def __and__(self, other: "BaseSpecification") -> "AndSpecification":
        return AndSpecification(self, other)

    def __or__(self, other: "BaseSpecification") -> "OrSpecification":
        return OrSpecification(self, other)

    def __neg__(self) -> "NotSpecification":
        return NotSpecification(self)

    def __xor__(self, other) -> "XorSpecification":
        return XorSpecification(self, other)


class AndSpecification(BaseSpecification):
    def __init__(self, first: BaseSpecification, second: BaseSpecification):
        self.first = first
        self.second = second

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.first.is_satisfied_by(candidate) and self.second.is_satisfied_by(candidate)


class OrSpecification(BaseSpecification):
    def __init__(self, first: BaseSpecification, second: BaseSpecification):
        self.first = first
        self.second = second

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.first.is_satisfied_by(candidate) or self.second.is_satisfied_by(candidate)


class XorSpecification(BaseSpecification):
    def __init__(self, first: BaseSpecification, second: BaseSpecification):
        self.first = first
        self.second = second

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.first.is_satisfied_by(candidate) ^ self.second.is_satisfied_by(candidate)


class NotSpecification(BaseSpecification):
    def __init__(self, subject: BaseSpecification):
        self.subject = subject

    def is_satisfied_by(self, candidate: Any) -> bool:
        return not self.subject.is_satisfied_by(candidate)


class IsClamSpecification(BaseSpecification):
    def is_satisfied_by(self, candidate: Any) -> bool:
        print("--- in clam spec: candidate", candidate)
        if not isinstance(candidate, str):
            print("--- in clam spec: not string")
            return False
        return 'clam' in candidate


class IsPersonSpecification(BaseSpecification):
    def is_satisfied_by(self, candidate: Any) -> bool:
        print("--- in person spec: candidate", candidate)
        if not isinstance(candidate, str):
            return False
        return 'person' in candidate


class TimelySpecification(BaseSpecification):
    def is_satisfied_by(self, candidate: Any) -> bool:
        print("--- in timely spec: candidate", candidate)
        try:
            return candidate < 30
        except Exception as e:
            print("--- in timely spec: got exception", e)
            return False


def main() -> None:
    candidates = [
        'clam person',
        'person of the clam',
        'clamperson',
        'calm person',
        'clammy',
        92,
        8,
    ]

    is_clam_person = IsClamSpecification() & IsPersonSpecification()
    is_clam_and_not_person = IsClamSpecification() &  -(IsPersonSpecification())
    either_person_or_timely = TimelySpecification() ^ IsPersonSpecification()

    for candidate in candidates:
        print("Checking candidate:", candidate)
        if is_clam_person.is_satisfied_by(candidate):
            print("\"{}\" is a clam person".format(candidate))
        elif either_person_or_timely.is_satisfied_by(candidate):
            print("\"{}\" was timely xor person".format(candidate))
        elif is_clam_and_not_person.is_satisfied_by(candidate):
            print("\"{}\" is a clam and not a person".format(candidate))
        else:
            print("Candidate {} passed none of the requirements".format(candidate))


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/specification.py 
Checking candidate: clam person
--- in clam spec: candidate clam person
--- in person spec: candidate clam person
"clam person" is a clam person
Checking candidate: person of the clam
--- in clam spec: candidate person of the clam
--- in person spec: candidate person of the clam
"person of the clam" is a clam person
Checking candidate: clamperson
--- in clam spec: candidate clamperson
--- in person spec: candidate clamperson
"clamperson" is a clam person
Checking candidate: calm person
--- in clam spec: candidate calm person
--- in timely spec: candidate calm person
--- in timely spec: got exception '<' not supported between instances of 'str' and 'int'
--- in person spec: candidate calm person
"calm person" was timely xor person
Checking candidate: clammy
--- in clam spec: candidate clammy
--- in person spec: candidate clammy
--- in timely spec: candidate clammy
--- in timely spec: got exception '<' not supported between instances of 'str' and 'int'
--- in person spec: candidate clammy
--- in clam spec: candidate clammy
--- in person spec: candidate clammy
"clammy" is a clam and not a person
Checking candidate: 92
--- in clam spec: candidate 92
--- in clam spec: not string
--- in timely spec: candidate 92
--- in person spec: candidate 92
--- in clam spec: candidate 92
--- in clam spec: not string
Candidate 92 passed none of the requirements
Checking candidate: 8
--- in clam spec: candidate 8
--- in clam spec: not string
--- in timely spec: candidate 8
--- in person spec: candidate 8
"8" was timely xor person
"""
