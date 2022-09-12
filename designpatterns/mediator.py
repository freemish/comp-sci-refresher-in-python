# Demonstrates mediator pattern, AKA controller.

class BaseMediator:
    def notify(self, sender: object, event: str, *sender_method_args, **sender_method_kwargs) -> None:
        pass


class AdminViewMediator(BaseMediator):
    def __init__(self, admin_view_component: 'AdminViewComponent', log_warning_cap: int = 10) -> None:
        self._admin_view_component = admin_view_component
        self._admin_view_component.mediator = self
        self._admin_logger_component = AdminLoggerComponent(self, event_storage_warning_cap=log_warning_cap)

    def notify(self, sender: object, event: str, *args, **kwargs) -> None:
        print("Notified mediator of event {} from sender {}".format(event, type(sender).__name__))
        if isinstance(sender, AdminLoggerComponent) and event == 'write_event_to_file':
            print()
            return

        print('Mediator is triggering actions from admin logger component...')
        if self._admin_logger_component.get_event_storage_percent() >= 0.7:
            print("Admin logger file needs rotation right now!")
            self._admin_logger_component.flush_events_to_remote()
        self._admin_logger_component.write_event_to_file(event, *args, **kwargs)


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: BaseMediator = None) -> None:
        self._mediator = mediator or BaseMediator()

    @property
    def mediator(self) -> BaseMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: BaseMediator) -> None:
        self._mediator = mediator


class AdminViewComponent(BaseComponent):
    def view_user_list(self, **filters) -> None:
        print("Admin view: View user list")
        self.mediator.notify(self, "view_user_list", filters=filters)

    def change_user_permission(self, username: str, new_permission: str) -> None:
        print("Admin view: Change user permission for user", username)
        self.mediator.notify(self, "change_user_permission", username=username, new_permission=new_permission)


class AdminLoggerComponent(BaseComponent):
    def __init__(self, mediator: BaseMediator, event_storage_warning_cap: int = 10):
        super().__init__(mediator)
        self.event_storage_warning_cap = event_storage_warning_cap
        self.events = []

    def write_event_to_file(self, event: str, *args, **kwargs) -> None:
        print("Admin logger component: pretending to write event to file...")
        event_dict = {'event': event, 'event_args': args, 'event_kwargs': kwargs}
        print(event_dict)
        self.events.append(event_dict)
        self.mediator.notify(self, "write_event_to_file")

    def get_event_storage_percent(self) -> float:
        return len(self.events) / self.event_storage_warning_cap

    def flush_events_to_remote(self) -> None:
        print("Admin logger component: pretending to flush logs to remote and rotate log file")
        events = list(self.events)
        self.events = []
        self.mediator.notify(self, "flush_events_to_remote", events=events)
        


def main() -> None:
    print("Demonstrating mediator pattern.")
    print("A mediator is responsible for chaining other component actions once a component action is triggered.")
    print("This example uses a mediator to trigger logging events for a pretend admin UI view.")
    print()
    
    admin_view = AdminViewComponent()
    AdminViewMediator(admin_view, log_warning_cap=2)

    admin_view.view_user_list()
    admin_view.view_user_list(users=['melon-colic'])
    admin_view.change_user_permission('melon-colic', 'r')


if __name__ == "__main__":
    main()


"""
$ python3 designpatterns/mediator.py 
Demonstrating mediator pattern.
A mediator is responsible for chaining other component actions once a component action is triggered.
This example uses a mediator to trigger logging events for a pretend admin UI view.

Admin view: View user list
Notified mediator of event view_user_list from sender AdminViewComponent
Mediator is triggering actions from admin logger component...
Admin logger component: pretending to write event to file...
{'event': 'view_user_list', 'event_args': (), 'event_kwargs': {'filters': {}}}
Notified mediator of event write_event_to_file from sender AdminLoggerComponent

Admin view: View user list
Notified mediator of event view_user_list from sender AdminViewComponent
Mediator is triggering actions from admin logger component...
Admin logger component: pretending to write event to file...
{'event': 'view_user_list', 'event_args': (), 'event_kwargs': {'filters': {'users': ['melon-colic']}}}
Notified mediator of event write_event_to_file from sender AdminLoggerComponent

Admin view: Change user permission for user melon-colic
Notified mediator of event change_user_permission from sender AdminViewComponent
Mediator is triggering actions from admin logger component...
Admin logger file needs rotation right now!
Admin logger component: pretending to flush logs to remote and rotate log file
Notified mediator of event flush_events_to_remote from sender AdminLoggerComponent
Mediator is triggering actions from admin logger component...
Admin logger component: pretending to write event to file...
{'event': 'flush_events_to_remote', 'event_args': (), 'event_kwargs': {'events': [{'event': 'view_user_list', 'event_args': (), 'event_kwargs': {'filters': {}}}, {'event': 'view_user_list', 'event_args': (), 'event_kwargs': {'filters': {'users': ['melon-colic']}}}]}}
Notified mediator of event write_event_to_file from sender AdminLoggerComponent

Admin logger component: pretending to write event to file...
{'event': 'change_user_permission', 'event_args': (), 'event_kwargs': {'username': 'melon-colic', 'new_permission': 'r'}}
Notified mediator of event write_event_to_file from sender AdminLoggerComponent

"""