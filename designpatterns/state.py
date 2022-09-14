# Demonstrates state design pattern.

from abc import ABC, abstractmethod
from typing import Optional


class AudioPlayer:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    current_song_index: int = 0

    def __init__(self, state: Optional['AudioPlayerState'] = None) -> None:
        self._load_playlist_from_memory()
        self.transition_to(state) if state else self.transition_to(ReadyAudioPlayerState())

    def _load_playlist_from_memory(self) -> None:
        self.playlist = ['song1', 'song2', 'song3', 'song4']

    def get_name_of_current_state(self) -> str:
        return type(self._state).__name__

    def transition_to(self, state: 'AudioPlayerState'):
        print(f"AudioPlayer: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def click_lock(self):
        self._state.click_lock()

    def click_play(self):
        self._state.click_play()

    def click_next(self):
        self._state.click_next()

    def click_previous(self):
        self._state.click_previous()


class AudioPlayerState(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> AudioPlayer:
        return self._context

    @context.setter
    def context(self, context: AudioPlayer) -> None:
        self._context = context

    @abstractmethod
    def click_lock(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def click_play(self) -> None:
        pass

    @abstractmethod
    def click_next(self) -> None:
        pass

    @abstractmethod
    def click_previous(self) -> None:
        pass


class LockedReadyAudioPlayerState(AudioPlayerState):
    def click_lock(self, *args, **kwargs) -> None:
        print('Locked player had lock button clicked; transitioning to ready state')
        self._context.transition_to(ReadyAudioPlayerState())

    def click_play(self) -> None:
        print('Play button was pressed on locked player; doing nothing')

    def click_next(self) -> None:
        print('Next button was pressed on locked player; doing nothing')

    def click_previous(self) -> None:
        print('Previous button was pressed on locked player; doing nothing')


class LockedPlayingAudioPlayerState(LockedReadyAudioPlayerState):
    def click_lock(self, *args, **kwargs) -> None:
        print('Locked playing player had lock button clicked; transitioning to playing state')
        self._context.transition_to(PlayingAudioPlayerState())


class ReadyAudioPlayerState(AudioPlayerState):
    def click_lock(self, *args, **kwargs) -> None:
        print('Ready player had lock button clicked; transitioning to locked state')
        self._context.transition_to(LockedReadyAudioPlayerState())
    
    def click_next(self) -> None:
        if self._context.current_song_index < len(self._context.playlist) - 1:
            self._context.current_song_index += 1
        else:
            self._context.current_song_index = 0
        print('Clicked next. Current song is now', self._context.playlist[self._context.current_song_index])

    def click_previous(self) -> None:
        if self._context.current_song_index > 0:
            self._context.current_song_index -= 1
        else:
            self.context.current_song_index = len(self._context.playlist) - 1
        print('Clicked previous. Current song is now', self._context.playlist[self._context.current_song_index])

    def click_play(self) -> None:
        print('Play button pressed. Playing audio...')
        self._context.transition_to(PlayingAudioPlayerState())


class PlayingAudioPlayerState(ReadyAudioPlayerState):
    def click_lock(self, *args, **kwargs) -> None:
        print('Playing audio player had lock button clicked; transitioning to locked playing state')
        self._context.transition_to(LockedPlayingAudioPlayerState())

    def click_play(self) -> None:
        print('Play button pressed. Pausing...')
        self._context.transition_to(ReadyAudioPlayerState())


def main() -> None:
    print('Demonstrating state design pattern...')
    player = AudioPlayer()
    player.click_play()
    player.click_lock()
    player.click_play()
    player.click_lock()
    player.click_previous()
    player.click_next()
    player.click_play()
    player.click_next()


if __name__ == "__main__":
    main()


"""
$ python3 designpatterns/state.py
Demonstrating state design pattern...
AudioPlayer: Transition to ReadyAudioPlayerState
Play button pressed. Playing audio...
AudioPlayer: Transition to PlayingAudioPlayerState
Playing audio player had lock button clicked; transitioning to locked playing state
AudioPlayer: Transition to LockedPlayingAudioPlayerState
Play button was pressed on locked player; doing nothing
Locked playing player had lock button clicked; transitioning to playing state
AudioPlayer: Transition to PlayingAudioPlayerState
Clicked previous. Current song is now song4
Clicked next. Current song is now song1
Play button pressed. Pausing...
AudioPlayer: Transition to ReadyAudioPlayerState
Clicked next. Current song is now song2
"""
