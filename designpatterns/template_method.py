# Demonstrates template method pattern.

import json
from abc import abstractmethod
from typing import Any, Dict, Optional


class ServerlessFunction:
    def handler(self, event: Any, context: Any) -> Any:
        print('Running handler for', type(self).__name__)
        parsed_event = self.parse_event(event, context)
        return self.service(parsed_event, context)

    @abstractmethod
    def service(self, parsed_event_input: Any, context: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def parse_event(self, event: Any, context: Optional[Any] = None) -> Any:
        raise NotImplementedError()


class QueueTriggerServerlessFunction(ServerlessFunction):
    def parse_event(self, event: Dict[str, Any], _: Optional[Any] = None) -> Any:
        assert len(event.get('Records', [])) == 1
        return json.loads(event['Records'][0]['body'])


class StorageTriggerServerlessFunction(ServerlessFunction):
    def parse_event(self, event: str, _: Optional[Any] = None) -> Any:
        return json.loads(event)


class ProcessUploadedFileServerlessFunction(StorageTriggerServerlessFunction):
    def service(self, parsed_event_input: Dict[str, Any], _: Any) -> Dict[str, Any]:
        print("Processing uploaded file:", parsed_event_input)
        return {'success': True, 'file': parsed_event_input.get('file_key')}


class UploadFileServerlessFunction(QueueTriggerServerlessFunction):
    def service(self, parsed_event_input: Any, context: Any) -> Dict:
        if context == 'LOCALDEV':
            print('Mocking file upload because function is being run for local dev environment')
        else:
            print('Uploading file from parsed event:', parsed_event_input)
        return {'success': True, 'file': parsed_event_input.get('file_key')}


def main() -> None:
    print("Demonstrating template method pattern...")

    upload_svrls = UploadFileServerlessFunction()
    process_svrls = ProcessUploadedFileServerlessFunction()

    upload_event = {
        'Records': [
            {
                'body': json.dumps({
                    'file_key': 'jupiter.jpeg',
                    'file_data': 'abc123def456',
                }),
            },
        ],
    }

    process_file_event = upload_event['Records'][0]['body']

    upload_svrls.handler(upload_event, 'LOCALDEV')
    upload_svrls.handler(upload_event, 'PROD')
    process_svrls.handler(process_file_event, None)


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/template_method.py
Demonstrating template method pattern...
Running handler for UploadFileServerlessFunction
Mocking file upload because function is being run for local dev environment
Running handler for UploadFileServerlessFunction
Uploading file from parsed event: {'file_key': 'jupiter.jpeg', 'file_data': 'abc123def456'}
Running handler for ProcessUploadedFileServerlessFunction
Processing uploaded file: {'file_key': 'jupiter.jpeg', 'file_data': 'abc123def456'}
"""
