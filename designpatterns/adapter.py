"""Demonstrates adapter pattern."""

from typing import List, Dict


class CompanyADataMillClient:
    def get_raw_data(self, a: str) -> Dict:
        return {'user': a, 'all_time_usages': 139, 'recent_usages': 3, 'reports': 2}


class CompanyBDataMillClient:
    def get_usage_reports(self, a: str) -> List[str]:
        return ['a', 'b']
    
    def get_user_statistics(self, a: str)  -> Dict:
        return {'last_week_usages': 3, 'last_month_usages': 123, 'all_time_usages': 139}


class CompanyBDataMillAdapter(CompanyADataMillClient, CompanyBDataMillClient):
    def get_raw_data(self, a: str) -> Dict:
        user_stats = self.get_user_statistics(a)
        reports = self.get_usage_reports(a)
        return {
            'user': a,
            'all_time_usages': user_stats['all_time_usages'],
            'recent_usages': user_stats['last_week_usages'],
            'reports': len(reports)
        }


def main():
    print('Demonstrating adapter pattern...')

    print('\nThe application has always been using one company that has a specific data format,')
    print('but now it wants to get user usage statistics from a second company.')

    print('Output from raw request to Company A data mill client:', CompanyADataMillClient().get_raw_data('user1'))
    print('Output from adapter method for Company B:', CompanyBDataMillAdapter().get_raw_data('user2'))
    print('Without adapting, the data from Company B looks like this:', CompanyBDataMillClient().get_user_statistics('user3'), CompanyBDataMillClient().get_usage_reports('user3'))

    print('It\'s a little funky to subclass off of the Company A client, but this could be made more elegant by having one interface for both clients.')

if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/adapter.py
Demonstrating adapter pattern...

The application has always been using one company that has a specific data format,
but now it wants to get user usage statistics from a second company.
Output from raw request to Company A data mill client: {'user': 'user1', 'all_time_usages': 139, 'recent_usages': 3, 'reports': 2}
Output from adapter method for Company B: {'user': 'user2', 'all_time_usages': 139, 'recent_usages': 3, 'reports': 2}
Without adapting, the data from Company B looks like this: {'last_week_usages': 3, 'last_month_usages': 123, 'all_time_usages': 139} ['a', 'b']
It's a little funky to subclass off of the Company A client, but this could be made more elegant by having one interface for both clients.
"""
