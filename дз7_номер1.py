import os

my_keys = {'my_project': [{'settings':[]},{'mainapp':[]},{'adminapp': []},{'authapp': []}]}

for key, value in my_keys.items ():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys ():
                os.makedirs (os.path.join(key,k))

