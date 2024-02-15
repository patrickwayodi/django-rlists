"""
Load the fixtures using these commands:
    python manage.py loaddata rating_list_v03.json
"""


print('[')


player_counter = 1


while player_counter < 810:

    print('    {')
    print('        "model": "ratings.player",')
    print('        "pk":', player_counter,',')
    print('        "fields": {')
    print('            "origin_file": "rating_list_v03.json",')
    print('            "name": "Jane Doe",')
    print('            "rating": "1850",')
    print('            "fed": "KEN",')
    print('            "birthday": "2001"')
    print('        }')
    print('    },')

    player_counter = player_counter + 1


print(']')

