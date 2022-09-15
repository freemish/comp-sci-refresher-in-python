# Demonstrates proxy pattern.

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class RemoteVideoServiceInterface(ABC):
    @abstractmethod
    def list_videos(self, **filters) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_video_info(self, id: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def download_video(self, id: Any) -> bytearray:
        pass


class ExistingYouTubeAPI(RemoteVideoServiceInterface):
    def list_videos(self, **filters) -> List[Dict[str, Any]]:
        print('Listing videos with existing API class')
        return [
            {'id': 1, 'name': 'Running Your Mouth Is a Bad Idea', 'duration': '1:34'},
            {'id': 2, 'name': 'You\'ll NEVER believe me', 'duration': '0:07'},
            {'id': 3, 'name': 'Mister Kitty makes a weird meow', 'duration': '9:49'},
            {'id': 4, 'name': 'What up punk', 'duration': '6:54'},
        ]
    
    def get_video_info(self, id: int) -> Dict[str, Any]:
        print('Getting video info from existing API class')
        ltod = {x['id']: x for x in self.list_videos()}
        return ltod.get(id, {})
    
    def download_video(self, id: Any) -> bytearray:
        print('Downloading video data from existing API class')
        return 'fakedata{}'.format(id).encode('utf8')


class RemoteVideoServiceProxy(RemoteVideoServiceInterface):
    def __init__(self, rvs: Optional[RemoteVideoServiceInterface] = None):
        self._rvs = rvs or ExistingYouTubeAPI()
    
    def list_videos(self, **filters) -> List[Dict[str, Any]]:
        print('(Passing through proxy to list videos)')
        return self._rvs.list_videos(**filters)

    def get_video_info(self, id: Any) -> Dict[str, Any]:
        print('(Passing through proxy to get video info)')
        return self._rvs.get_video_info(id)

    def download_video(self, id: Any) -> bytearray:
        print('(Passing through proxy to download video)')
        return self._rvs.download_video(id)


class RemoteVideoRenderer:
    def __init__(self, rvs: RemoteVideoServiceInterface):
        self.rvs = rvs

    def render_list_of_videos(self):
        print('Rendered video list:', self.rvs.list_videos())
    
    def render_video_info(self, id: Any):
        print('Rendered video info:', self.rvs.get_video_info(id))

    def download_video(self, id: Any):
        print('Downloaded video:', self.rvs.download_video(id))


def main() -> None:
    print('Demonstrating proxy pattern...')
    print("Remote video renderer has the same output when the proxy is first installed,")
    print("but now other clients can easily be inserted to use the same interface and subtle behavior changes can be inserted into the proxy as needed.")

    print("Just using the concrete service directly:")
    rvr = RemoteVideoRenderer(ExistingYouTubeAPI())
    rvr.render_list_of_videos()
    rvr.render_video_info(1)
    rvr.download_video(2)

    print("Now using the proxy, output should be the same:")
    rvr.rvs = RemoteVideoServiceProxy(rvr.rvs)
    rvr.render_list_of_videos()
    rvr.render_video_info(1)
    rvr.download_video(2)

if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/proxy.py
Demonstrating proxy pattern...
Remote video renderer has the same output when the proxy is first installed,
but now other clients can easily be inserted to use the same interface and subtle behavior changes can be inserted into the proxy as needed.
Just using the concrete service directly:
Listing videos with existing API class
Rendered video list: [{'id': 1, 'name': 'Running Your Mouth Is a Bad Idea', 'duration': '1:34'}, {'id': 2, 'name': "You'll NEVER believe me", 'duration': '0:07'}, {'id': 3, 'name': 'Mister Kitty makes a weird meow', 'duration': '9:49'}, {'id': 4, 'name': 'What up punk', 'duration': '6:54'}]
Getting video info from existing API class
Listing videos with existing API class
Rendered video info: {'id': 1, 'name': 'Running Your Mouth Is a Bad Idea', 'duration': '1:34'}
Downloading video data from existing API class
Downloaded video: b'fakedata2'
Now using the proxy, output should be the same:
(Passing through proxy to list videos)
Listing videos with existing API class
Rendered video list: [{'id': 1, 'name': 'Running Your Mouth Is a Bad Idea', 'duration': '1:34'}, {'id': 2, 'name': "You'll NEVER believe me", 'duration': '0:07'}, {'id': 3, 'name': 'Mister Kitty makes a weird meow', 'duration': '9:49'}, {'id': 4, 'name': 'What up punk', 'duration': '6:54'}]
(Passing through proxy to get video info)
Getting video info from existing API class
Listing videos with existing API class
Rendered video info: {'id': 1, 'name': 'Running Your Mouth Is a Bad Idea', 'duration': '1:34'}
(Passing through proxy to download video)
Downloading video data from existing API class
Downloaded video: b'fakedata2'
"""
