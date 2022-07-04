"""
Concrete implementation of factory method and abstract factory patterns.
"""

import abc


class Friend:
    @abc.abstractstaticmethod
    def get_supportive_comment() -> str:
        raise NotImplementedError


class AbstractFriendFactory:
    @abc.abstractclassmethod
    def get_friend(cls, description: str) -> Friend:
        raise NotImplementedError


class FriendFactory(AbstractFriendFactory):
    @classmethod
    def get_friend(cls, description: str) -> Friend:
        return friend_factory_method(description)()


class BadFriendFactory(AbstractFriendFactory):
    @classmethod
    def get_friend(cls, description: str) -> Friend:
        return {
            'happy': SadFriend,
            'sassy': SweetFriend,
            'sweet': SassyFriend,
            'default': SassyFriend,
        }.get(description, DefaultFriend)()


class SassyFriend(Friend):
    @staticmethod
    def get_supportive_comment() -> str:
        return 'You *know* you\'re gonna be just fine - don\'t mess around with me like that.'


class SweetFriend(Friend):
    @staticmethod
    def get_supportive_comment() -> str:
        return 'I\'ve known you for a while, and I really think you can do whatever you set your mind to.'


class SadFriend(Friend):
    @staticmethod
    def get_supportive_comment() -> str:
        return 'I know you\'re going through a rough patch, but... hey, it can\'t be as bad as what I just told you about, right? If I can do it, so can you.'


class DefaultFriend(Friend):
    @staticmethod
    def get_supportive_comment() -> str:
        return 'It\'s okay, just do your best.'


def friend_factory_method(description: str) -> Friend:
    return {
        'sassy': SassyFriend,
        'sweet': SweetFriend,
        'sad': SadFriend,
    }.get(description, DefaultFriend)


def main():
    print("Starting demonstration of factory pattern.")

    print('Right now, I know I need a sassy friend. But what if the friend I need changes during runtime?')
    friends_i_need = ["sweet", "sassy", "simple", "happy"]

    print('I can use a simple factory method to choose among a bunch of concrete classes; that method can be on a concrete factory class as well:\n')
    for friend_desc in friends_i_need:
        friend_obj = FriendFactory.get_friend(friend_desc)
        print('\tInput: {}\n\tFriend type: {}\n\tComment: {}\n'.format(
            friend_desc, type(friend_obj).__name__, friend_obj.get_supportive_comment()
        ))

    print('These could be the results with a different factory class:')
    for friend_desc in friends_i_need:
        friend_obj = BadFriendFactory.get_friend(friend_desc)
        print('\tInput: {}\n\tFriend type: {}\n\tComment: {}\n'.format(
            friend_desc, type(friend_obj).__name__, friend_obj.get_supportive_comment()
        ))

    print('But, in general, don\'t treat people like objects :P')


if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/factory.py
Starting demonstration of factory pattern.
Right now, I know I need a sassy friend. But what if the friend I need changes during runtime?
I can use a simple factory method to choose among a bunch of concrete classes; that method can be on a concrete factory class as well:

        Input: sweet
        Friend type: SweetFriend
        Comment: I've known you for a while, and I really think you can do whatever you set your mind to.

        Input: sassy
        Friend type: SassyFriend
        Comment: You *know* you're gonna be just fine - don't mess around with me like that.

        Input: simple
        Friend type: DefaultFriend
        Comment: It's okay, just do your best.

        Input: happy
        Friend type: DefaultFriend
        Comment: It's okay, just do your best.

These could be the results with a different factory class:
        Input: sweet
        Friend type: SassyFriend
        Comment: You *know* you're gonna be just fine - don't mess around with me like that.

        Input: sassy
        Friend type: SweetFriend
        Comment: I've known you for a while, and I really think you can do whatever you set your mind to.

        Input: simple
        Friend type: DefaultFriend
        Comment: It's okay, just do your best.

        Input: happy
        Friend type: SadFriend
        Comment: I know you're going through a rough patch, but... hey, it can't be as bad as what I just told you about, right? If I can do it, so can you.

But, in general, don't treat people like objects :P
"""
