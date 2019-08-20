import requests
import sys
import time

sys.path.append("C:/Users/Tag Livros/python-libs/functions")

from requests_retry_session import requests_retry_session # This from must be after "sys.path.append"

# Teste 1
print("Teste 1")
response = requests_retry_session().get('https://www.peterbe.com/')
print(response.status_code)

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

response = requests_retry_session(session=s).get(
    'https://www.peterbe.com'
)


# Teste 2
print("\nTeste 2")
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://localhost:9999',
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')


# Teste 3
print("\nTeste 3")
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/delay/10',
        timeout=2
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')


# Teste 4
print("\nTeste 4")
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/status/500',
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')
