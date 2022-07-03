"""Concrete demonstration of the strategy pattern."""

import abc
from types import FunctionType

# --- This example is about a "robotic influencer" swapping different text speech styles for a given statement. ---

class TextSpeechStrategy(abc.ABC):
    @abc.abstractmethod
    def get_text_in_text_speech_style(self, text: str) -> str:
        raise NotImplementedError


class RoboticInfluencer:
    """Represents an entity that adopts a style of text speech."""
    def __init__(self, name: str, text_speech_strategy: TextSpeechStrategy):
        self.name = name
        self.text_speech_strategy = text_speech_strategy

    def narrator_mode(self, final_text: str) -> str:
        return '{} says: "{}"'.format(self.name, final_text)
    
    def speak_in_style(self, raw_text: str) -> str:
        return self.text_speech_strategy.get_text_in_text_speech_style(raw_text)

    def narrator_mode_speak_in_style(self, raw_text: str) -> str:
        return self.narrator_mode(self.speak_in_style(raw_text))

    def speak_via_lambda(self, raw_text: str, text_transform_func: FunctionType) -> str:
        return text_transform_func(raw_text)


class NormalTextSpeechStrategy(TextSpeechStrategy):
    def get_text_in_text_speech_style(self, text: str) -> str:
        return text


class AllCapsTextSpeechStrategy(TextSpeechStrategy):
    def get_text_in_text_speech_style(self, text: str) -> str:
        return text.upper()


class PreachSisterSentencesTextSpeechStrategy(TextSpeechStrategy):
    def get_text_in_text_speech_style(self, text: str) -> str:
        return '. PREACH, SISTER.'.join(text.split('.'))


class ShyAllOneWordTextSpeechStrategy(TextSpeechStrategy):
    def get_text_in_text_speech_style(self, text: str) -> str:
        return text.lower().replace(' ', '')


def main():
    print('Starting strategy pattern demonstration.')

    sally_robot = RoboticInfluencer('Sally', NormalTextSpeechStrategy())
    goober_robot = RoboticInfluencer('Goober', AllCapsTextSpeechStrategy())

    print(sally_robot.narrator_mode_speak_in_style('Hello. I am Sally. I am happy to meet you.'))
    print(goober_robot.narrator_mode_speak_in_style('Hello. I am Goober. Right now I speak differently. Nice to meet you.'))

    print('Now: Sally can be made to talk like Goober.')
    sally_robot.text_speech_strategy = goober_robot.text_speech_strategy
    print(sally_robot.narrator_mode_speak_in_style('Now I am speaking like Goober.'))
    goober_robot.text_speech_strategy = ShyAllOneWordTextSpeechStrategy()
    print(goober_robot.narrator_mode_speak_in_style('That was very weird. I feel uncomfortable.'))

    print("It may be a bit silly to use the strategy pattern in Python when you have the option to pass around functions instead, though.")

    print(sally_robot.narrator_mode(
        sally_robot.speak_via_lambda(
            'Now this one is even a little bit more dynamic, I reckon.',
            PreachSisterSentencesTextSpeechStrategy().get_text_in_text_speech_style)
        )
    )

    print(sally_robot.narrator_mode(
        sally_robot.speak_via_lambda(
            'See? It doesn\'t even have to come from a Strategy object.',
            lambda x: x + ' ' + x
        )
    ))

    print(goober_robot.narrator_mode(
        goober_robot.speak_via_lambda(
            'I can do it too!',
            lambda x: '! '.join(x.split(' '))
        )
    ))


if __name__ == "__main__":
    main()

"""
$ python3 designpatterns/strategy.py
Starting strategy pattern demonstration.
Sally says: "Hello. I am Sally. I am happy to meet you."
Goober says: "HELLO. I AM GOOBER. RIGHT NOW I SPEAK DIFFERENTLY. NICE TO MEET YOU."
Now: Sally can be made to talk like Goober.
Sally says: "NOW I AM SPEAKING LIKE GOOBER."
Goober says: "thatwasveryweird.ifeeluncomfortable."
It may be a bit silly to use the strategy pattern in Python when you have the option to pass around functions instead, though.
Sally says: "Now this one is even a little bit more dynamic, I reckon. PREACH, SISTER."
Sally says: "See? It doesn't even have to come from a Strategy object. See? It doesn't even have to come from a Strategy object."
Goober says: "I! can! do! it! too!"
"""
