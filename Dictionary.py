locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia']={'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa']={'Egypt': ['Cairo']}

usa_sorted=sorted(locations['North America']['USA'])
print(1)
for i in usa_sorted:
    print(i)

print(2)
Asia_sorted=[]
for countries,cities in locations['Asia'].items():
    city_country=cities[0]+' - '+countries
    Asia_sorted.append(city_country)
Asia_sorted=sorted(Asia_sorted)
for i in Asia_sorted:
    print(i)
    
          
