locations = {'North America': {'USA': ['Mountain View']}}

locations['North America']['USA'].append('Atlanta')
locations['Asia']={'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt':['Cairo']}

print(1)
for city in sorted(locations['North America']['USA']):
    print(city)

print(2)
keys = sorted(list(locations['Asia'].keys()))
for key in keys:
    for city in sorted(locations['Asia'][key]):
        print(key, '-', city)

        