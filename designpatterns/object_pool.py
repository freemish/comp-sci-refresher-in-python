# Demonstrates object pool pattern.

import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from typing import Any, List, Optional
from uuid import uuid4


class NoResourceAvailable(Exception):
    def __init__(self, msg: Optional[str] = None):
        self.message = "Cannot pull resource when no resource available in resource pool"
        if msg:
            self.message += ": {}".format(msg)
        super().__init__(self.message)


class ResourceTypeMismatchesPool(Exception):
    def __init__(self, msg: Optional[str] = None):
        self.message = msg or "Cannot add resource to resource pool when class mismatches pool class"
        super().__init__(self.message)


class LimitedResourcePool:
    def __init__(self, resource_cls, resource_cls_count: int):
        self._resource_cls = resource_cls
        self._pool = [resource_cls() for _ in range(resource_cls_count)]

    def acquire_resource(self) -> object:
        try:
            return self._pool.pop(0)
        except IndexError:
            raise NoResourceAvailable()
    
    def add_resource_to_pool(self, resource: object) -> None:
        if not isinstance(resource, self._resource_cls):
            raise ResourceTypeMismatchesPool()
        self._pool.append(resource)

    def peek_pool_uuids(self) -> List[str]:
        return [x.uuid_str for x in self._pool]


class ExpensiveResource:
    def __init__(self):
        self._uuid = uuid4().hex
        sleep(0.1)

    @property
    def uuid_str(self) -> str:
        return self._uuid


def thread_function(thread_id: Any, resource_pool: LimitedResourcePool) -> None:
    print("Thread {}: starting...".format(thread_id))
    resource = None
    while resource is None:
        try:
            resource = resource_pool.acquire_resource()
            print("Thread {}: acquired resource; peeking at pool: {}".format(thread_id, resource_pool.peek_pool_uuids()))
        except NoResourceAvailable:
            print("Thread {}: Thread failed to acquire resource. Sleeping...".format(thread_id))
            sleep(0.01)

    sleep(0.01)
    print("Thread {}: Resource ID: {}".format(thread_id, resource.uuid_str))
    resource_pool.add_resource_to_pool(resource)
    print("Thread {}: all done".format(thread_id))


def main() -> None:
    print("Demonstrating the object pool pattern...")

    print("When we initialize the limited resource pool, it will create a specified number of objects for us.")
    expensive_resources_pool = LimitedResourcePool(ExpensiveResource, 2)

    print("Available pool uuids:", expensive_resources_pool.peek_pool_uuids())
    
    resource1 = expensive_resources_pool.acquire_resource()
    print("Acquired resource:", resource1.uuid_str)
    print("Available pool uuids:", expensive_resources_pool.peek_pool_uuids())

    resource2 = expensive_resources_pool.acquire_resource()
    print("Acquired resource:", resource2.uuid_str)
    print("Available pool uuids:", expensive_resources_pool.peek_pool_uuids())

    try:
        expensive_resources_pool.acquire_resource()
    except NoResourceAvailable as nra_exc:
        print("Exception:", nra_exc)
    
    print("Releasing both resources in reverse order...")
    expensive_resources_pool.add_resource_to_pool(resource2)
    expensive_resources_pool.add_resource_to_pool(resource1)
    print("Available pool uuids:", expensive_resources_pool.peek_pool_uuids())

    resource = expensive_resources_pool.acquire_resource()
    print("Acquired resource:", resource.uuid_str)
    print("Available pool uuids:", expensive_resources_pool.peek_pool_uuids())
    expensive_resources_pool.add_resource_to_pool(resource)
    print("Available pool uuids:", expensive_resources_pool.peek_pool_uuids())

    print("---")
    print("Starting demonstration of object pool with multiple threads...")
    
    threads = []
    for i in range(3):
        thread = threading.Thread(target=thread_function, args=(i, expensive_resources_pool))
        threads.append(thread)
        thread.start()
        print("Main: Peeking at pool after starting thread {}: {}".format(i, expensive_resources_pool.peek_pool_uuids()))

    for i, thread in enumerate(threads):
        print("Main: About to join completed thread {} to main...".format(i))
        thread.join()
        print("Main: Joined thread {}".format(i))

    print("All threads done. Object pool:", expensive_resources_pool.peek_pool_uuids())

    print("---")
    print("Starting demonstration of object pool with multiple threads using concurrent.futures...")
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            executor.submit(thread_function, i, expensive_resources_pool)

    print("All threads done. Object pool:", expensive_resources_pool.peek_pool_uuids())
    

if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/object_pool.py
Demonstrating the object pool pattern...
When we initialize the limited resource pool, it will create a specified number of objects for us.
Available pool uuids: ['8f7705d69a2c4253b6cf86ff79b1f484', '065cc7a8b23147f1af75dec721903bd1']
Acquired resource: 8f7705d69a2c4253b6cf86ff79b1f484
Available pool uuids: ['065cc7a8b23147f1af75dec721903bd1']
Acquired resource: 065cc7a8b23147f1af75dec721903bd1
Available pool uuids: []
Exception: Cannot pull resource when no resource available in resource pool
Releasing both resources in reverse order...
Available pool uuids: ['065cc7a8b23147f1af75dec721903bd1', '8f7705d69a2c4253b6cf86ff79b1f484']
Acquired resource: 065cc7a8b23147f1af75dec721903bd1
Available pool uuids: ['8f7705d69a2c4253b6cf86ff79b1f484']
Available pool uuids: ['8f7705d69a2c4253b6cf86ff79b1f484', '065cc7a8b23147f1af75dec721903bd1']
---
Starting demonstration of object pool with multiple threads...
Thread 0: starting...
Thread 0: acquired resource; peeking at pool: ['065cc7a8b23147f1af75dec721903bd1']
Main: Peeking at pool after starting thread 0: ['065cc7a8b23147f1af75dec721903bd1']
Thread 1: starting...
Thread 1: acquired resource; peeking at pool: []
Main: Peeking at pool after starting thread 1: []
Thread 2: starting...
Thread 2: Thread failed to acquire resource. Sleeping...
Main: Peeking at pool after starting thread 2: []
Main: About to join completed thread 0 to main...
Thread 0: Resource ID: 8f7705d69a2c4253b6cf86ff79b1f484
Thread 0: all done
Main: Joined thread 0
Main: About to join completed thread 1 to main...
Thread 1: Resource ID: 065cc7a8b23147f1af75dec721903bd1
Thread 1: all done
Main: Joined thread 1
Main: About to join completed thread 2 to main...
Thread 2: acquired resource; peeking at pool: ['065cc7a8b23147f1af75dec721903bd1']
Thread 2: Resource ID: 8f7705d69a2c4253b6cf86ff79b1f484
Thread 2: all done
Main: Joined thread 2
All threads done. Object pool: ['065cc7a8b23147f1af75dec721903bd1', '8f7705d69a2c4253b6cf86ff79b1f484']
---
Starting demonstration of object pool with multiple threads using concurrent.futures...
Thread 0: starting...
Thread 0: acquired resource; peeking at pool: ['8f7705d69a2c4253b6cf86ff79b1f484']
Thread 1: starting...
Thread 1: acquired resource; peeking at pool: []
Thread 2: starting...
Thread 2: Thread failed to acquire resource. Sleeping...
Thread 0: Resource ID: 065cc7a8b23147f1af75dec721903bd1
Thread 0: all done
Thread 1: Resource ID: 8f7705d69a2c4253b6cf86ff79b1f484
Thread 1: all done
Thread 2: acquired resource; peeking at pool: ['8f7705d69a2c4253b6cf86ff79b1f484']
Thread 2: Resource ID: 065cc7a8b23147f1af75dec721903bd1
Thread 2: all done
All threads done. Object pool: ['8f7705d69a2c4253b6cf86ff79b1f484', '065cc7a8b23147f1af75dec721903bd1']
"""