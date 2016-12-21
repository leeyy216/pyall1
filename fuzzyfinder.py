#模糊匹配20161214

import re
def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
#append() 方法用于在列表末尾添加新的对象
            
    return [x for _, _, x in sorted(suggestions)]


collection=[ 'django_migrations.py',
                'django_admin_log.py',
                'main_generator.py',
                'migrations.py',
                'api_user.doc',
                'user_group.doc',
                'accounts.txt',
             '上海大学'
             ]
a=input('please input the keyword： \n')
print(fuzzyfinder(a,collection))
