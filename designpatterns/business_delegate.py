"""Demo of business delegate pattern."""


import abc
from typing import Optional


class IBusinessService(abc.ABC):
    @abc.abstractmethod
    def do_processing(self) -> None:
        pass


class ConcreteBusinessService1(IBusinessService):
    def do_processing(self) -> None:
        print("Doing processing in Concrete Service 1")


class ConcreteBusinessService2(IBusinessService):
    def do_processing(self) -> None:
        print("Doing processing in Concrete Service 2")


class BusinessServiceLookup:
    def get_business_service(self, service_code: str) -> IBusinessService:
        service_map = {
            "1": ConcreteBusinessService1,
            "2": ConcreteBusinessService2,
        }
        return service_map.get(service_code, ConcreteBusinessService1)


class BusinessDelegate:
    def __init__(self, service_type: str, lookup_obj: Optional[BusinessServiceLookup] = None):
        self.service_type = service_type
        self.lookup_obj = lookup_obj if lookup_obj else BusinessServiceLookup()

    def set_service_type(self, service_type: str) -> None:
        self.service_type = service_type

    def do_task(self) -> None:
        return self.lookup_obj.get_business_service(self.service_type)().do_processing()


def main() -> None:
    delegate = BusinessDelegate("1")
    delegate.do_task()
    delegate.set_service_type("2")
    delegate.do_task()
    delegate.set_service_type("3")
    delegate.do_task()


if __name__ == '__main__':
    main()


"""
$ python3 designpatterns/business_delegate.py 
Doing processing in Concrete Service 1
Doing processing in Concrete Service 2
Doing processing in Concrete Service 1
"""
