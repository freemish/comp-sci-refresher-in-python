# Demonstrates composite pattern.

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class AbstractEntity(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute_identity_verification(self) -> List['AbstractEntity']:
        raise NotImplementedError

    def __str__(self) -> str:
        return "{}< {} >".format(type(self).__name__, self.name)


class Organization(AbstractEntity):
    def __init__(self, name: str, members_to_roles: Optional[Dict] = None):
        super().__init__(name)
        self.members_to_roles = members_to_roles or {}

    def execute_identity_verification(self) -> List['AbstractEntity']:
        individuals = []
        print("Verifying organization and associated members:", self.name)
        for member, role in self.members_to_roles.items():
            print("Executing verification for member {} in role {}...".format(member.name, role))
            individuals.extend(member.execute_identity_verification())
        return individuals

    def add_member(self, member: AbstractEntity, role: str) -> None:
        self.members_to_roles[member] = role


class Individual(AbstractEntity):
    def __init__(self, name: str):
        super().__init__(name)
    
    def execute_identity_verification(self) -> List['AbstractEntity']:
        print("Verifying individual {}...".format(self.name))
        return [self]


def main() -> None:
    print("Demonstrating composite pattern...")

    print("The problem: we have an entity we need to verify.", end=' ')
    print("The entity can be an organization or an individual.", end=' ')
    print("Orgs can have members that are individuals or other orgs.", end=' ')
    print("When the entity is an organization, all members also need to be verified.")
    print()

    print("---")
    just_a_person = Individual("Felicia Grapes")
    indies = just_a_person.execute_identity_verification()
    print([str(x) for x in indies])

    print("---")
    single_level_org = Organization(
        "Mom and Pop's Shoppe",
        members_to_roles={
            Individual("Frank Sonata"): "CEO",
            Individual("Lady Coffingham"): "VP of Deceit",
        }
    )
    indies = single_level_org.execute_identity_verification()
    print([str(x) for x in indies])

    print("---")
    multilevel_org = Organization(
        "Totally Aboveboard Inc.",
        members_to_roles={
            Organization(
                "Advisory Board on Apples",
                members_to_roles={
                    Individual("Your Granny"): "Chief Judger",
                    Organization(
                        "Team Backup Granny",
                        members_to_roles={
                            Individual("Dr. James Buchanan"): "Clone Scientist",
                            Individual("Mom"): "Granny's Apple Feeder",
                        }
                    ): "The Board",
                }
            ): "Apple Committee",
            Individual("Serious Xavier McFeathers"): "Chief Elementalist",
        }
    )
    indies = multilevel_org.execute_identity_verification()
    print([str(x) for x in indies])


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/composite.py
Demonstrating composite pattern...
The problem: we have an entity we need to verify. The entity can be an organization or an individual. Orgs can have members that are individuals or other orgs. When the entity is an organization, all members also need to be verified.

---
Verifying individual Felicia Grapes...
['Individual< Felicia Grapes >']
---
Verifying organization and associated members: Mom and Pop's Shoppe
Executing verification for member Frank Sonata in role CEO...
Verifying individual Frank Sonata...
Executing verification for member Lady Coffingham in role VP of Deceit...
Verifying individual Lady Coffingham...
['Individual< Frank Sonata >', 'Individual< Lady Coffingham >']
---
Verifying organization and associated members: Totally Aboveboard Inc.
Executing verification for member Advisory Board on Apples in role Apple Committee...
Verifying organization and associated members: Advisory Board on Apples
Executing verification for member Your Granny in role Chief Judger...
Verifying individual Your Granny...
Executing verification for member Team Backup Granny in role The Board...
Verifying organization and associated members: Team Backup Granny
Executing verification for member Dr. James Buchanan in role Clone Scientist...
Verifying individual Dr. James Buchanan...
Executing verification for member Mom in role Granny's Apple Feeder...
Verifying individual Mom...
Executing verification for member Serious Xavier McFeathers in role Chief Elementalist...
Verifying individual Serious Xavier McFeathers...
['Individual< Your Granny >', 'Individual< Dr. James Buchanan >', 'Individual< Mom >', 'Individual< Serious Xavier McFeathers >']
"""
