"""Concrete demonstration of the observer pattern."""


class Subscriber:
    """Someone who receives a newsletter when it's ready to be sent out."""

    def __init__(self, id: str):
        self.inbox = []
        self.id = id
    
    def receive_newsletter(self, headline: str) -> None:
        self.inbox.append(headline)
        print('ID {} receives newsletter with headline "{}" in inbox.'.format(self.id, headline))
    
    def read_most_recent_newsletter_from_inbox(self) -> None:
        try:
            last_headline = self.inbox.pop()
            print('ID {} reads newsletter with headline: "{}"'.format(self.id, last_headline))
        except IndexError:
            print('ID {} checked for new headlines, but they had no new newsletters.'.format(self.id))


class Publisher:
    """Publisher of newsletters. Maintains a list of subscribers."""

    def __init__(self):
        self.subscribers = {}
        self.archive = []

    def add_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers[subscriber.id] = subscriber
        print('Added subscriber {} to publisher list.'.format(subscriber.id))

    def remove_subscriber(self, id: str) -> None:
        try:
            self.subscribers.pop(id)
            print('Removed subscriber with ID {}'.format(id))
        except KeyError:
            print('Tried to remove subscriber with ID {}, but did not exist.'.format(id))

    def send_newsletters(self, headline: str) -> None:
        print('Sending headline: "{}"'.format(headline))
        self.archive.append(headline)
        for sub in self.subscribers.values():
            sub.receive_newsletter(headline)


def main():
    print('Starting demonstration of observer pattern.')

    publisher = Publisher()
    subscriber1 = Subscriber('molly')
    subscriber2 = Subscriber('nathan')
    subscriber3 = Subscriber('pupper')

    print(':The publisher publishes their first headline, but no one has subscribed.')
    publisher.send_newsletters('Hello world')

    print(':Molly joins the newsletter. This is a list that the publisher worries about, not Molly.')
    publisher.add_subscriber(subscriber1)
    publisher.send_newsletters('We got our first subscriber wow')
    print(':Inbox:', subscriber1.inbox)

    print(':Now Nathan joins.')
    publisher.add_subscriber(subscriber2)
    publisher.send_newsletters('Gadgets prove useless for the 5th quarter this year')

    print(':Pupper thinks they are subscribed, but they are not.')
    publisher.remove_subscriber(subscriber3.id)

    subscriber1.read_most_recent_newsletter_from_inbox()
    publisher.send_newsletters('More news from overseas that makes you cry')

    print(':Nathan is just not keeping up with his newsletters like he expected to, so he requests to unsubscribe from the publisher.')
    publisher.remove_subscriber(subscriber2.id)

    publisher.send_newsletters('Another thing is said')
    publisher.send_newsletters('The glass is not empty, not full, not even real')
    subscriber2.read_most_recent_newsletter_from_inbox()
    subscriber2.read_most_recent_newsletter_from_inbox()
    subscriber2.read_most_recent_newsletter_from_inbox()

    print(':Now Nathan has caught up a bit and resubscribes.')

    publisher.add_subscriber(subscriber2)
    publisher.send_newsletters('People return from the dead')

    print("Molly's inbox:", subscriber1.inbox)
    print("Nathan's inbox:", subscriber2.inbox)
    print("Pupper's inbox:", subscriber3.inbox)
    print('Full archive:', publisher.archive)

if __name__ == "__main__":
    main()

"""
$ python3 designpatterns/observer.py
Starting demonstration of observer pattern.
:The publisher publishes their first headline, but no one has subscribed.
Sending headline: "Hello world"
:Molly joins the newsletter. This is a list that the publisher worries about, not Molly.
Added subscriber molly to publisher list.
Sending headine: "We got our first subscriber wow"
ID molly receives newsletter with headline "We got our first subscriber wow" in inbox.
:Inbox: ['We got our first subscriber wow']
:Now Nathan joins.
Added subscriber nathan to publisher list.
Sending headine: "Gadgets prove useless for the 5th quarter this year"
ID molly receives newsletter with headline "Gadgets prove useless for the 5th quarter this year" in inbox.
ID nathan receives newsletter with headline "Gadgets prove useless for the 5th quarter this year" in inbox.
:Pupper thinks they are subscribed, but they are not.
Tried to remove subscriber with ID pupper, but did not exist.
ID molly reads newsletter with headline: "Gadgets prove useless for the 5th quarter this year"
Sending headine: "More news from overseas that makes you cry"
ID molly receives newsletter with headline "More news from overseas that makes you cry" in inbox.
ID nathan receives newsletter with headline "More news from overseas that makes you cry" in inbox.
:Nathan is just not keeping up with his newsletters like he expected to, so he requests to unsubscribe from the publisher.
Removed subscriber with ID nathan
Sending headine: "Another thing is said"
ID molly receives newsletter with headline "Another thing is said" in inbox.
Sending headine: "The glass is not empty, not full, not even real"
ID molly receives newsletter with headline "The glass is not empty, not full, not even real" in inbox.
ID nathan reads newsletter with headline: "More news from overseas that makes you cry"
ID nathan reads newsletter with headline: "Gadgets prove useless for the 5th quarter this year"
ID nathan checked for new headlines, but they had no new newsletters.
:Now Nathan has caught up a bit and resubscribes.
Added subscriber nathan to publisher list.
Sending headine: "People return from the dead"
ID molly receives newsletter with headline "People return from the dead" in inbox.
ID nathan receives newsletter with headline "People return from the dead" in inbox.
Molly's inbox: ['We got our first subscriber wow', 'More news from overseas that makes you cry', 'Another thing is said', 'The glass is not empty, not full, not even real', 'People return from the dead']
Nathan's inbox: ['People return from the dead']
Pupper's inbox: []
Full archive: ['Hello world', 'We got our first subscriber wow', 'Gadgets prove useless for the 5th quarter this year', 'More news from overseas that makes you cry', 'Another thing is said', 'The glass is not empty, not full, not even real', 'People return from the dead']
"""
