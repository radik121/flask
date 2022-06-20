import requests

# res = requests.post(
#     'http://127.0.0.1:5000/advert/',
#     json={'name': 'advert_2',
#           'description': 'description_2',
#           'owner_name': 'owner_2'}
# )
# print(res.text)


res = requests.get(
    'http://127.0.0.1:5000/advert/1')
print(res.text)


# res = requests.put(
#     'http://127.0.0.1:5000/advert/3',
#     json={'name': 'advert_5',
#           'description': 'description_5',
#           'owner_name': 'owner_2'}
# )
# print(res.text)

# res = requests.delete(
#     'http://127.0.0.1:5000/advert/3')
# print(res.text)
