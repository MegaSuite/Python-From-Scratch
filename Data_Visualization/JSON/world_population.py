import json
from countries import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS


filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

cc_populations={}

for pop_dict in pop_data:

    if pop_dict['Year']=='2010':

        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))

        code=get_country_code(country_name)

        if code:
            cc_populations[code]=population

cc_pops1,cc_pops2,cc_pops3={},{},{}
for code, population in cc_populations.items():
    if population<10000000:
        cc_pops1[code]=population
    elif population<1000000000:
        cc_pops2[code]=population
    else:
        cc_pops3[code]=population

    
        
wm=pygal_maps_world.maps.World()
wm_style=RS('#336699',base_style=LCS)
wm=pygal_maps_world.maps.World(style=wm_style)
wm.title='World Population in 2010, by Country'
wm.add('0-10m',cc_pops1)
wm.add('10m-1bn',cc_pops2)
wm.add('>1bn',cc_pops3)

wm.render_to_file('world_population.svg')