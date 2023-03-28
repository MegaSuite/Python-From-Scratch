import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Make an API call and store the response.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)
print("Status code:", r.status_code)


# Store API response in a variable.

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])


# Explore information about the repositories.

repo_dicts = response_dict['items']


names,plot_dicts= [],[]

for repo_dict in repo_dicts:

    names.append(repo_dict['name'])

    plot_dict={
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45 # type: ignore
my_config.show_legend = False # type: ignore
my_config.title_font_size = 24 # type: ignore 
my_config.label_font_size = 14 # type: ignore
my_config.major_label_font_size = 18 # type: ignore
my_config.truncate_label = 15 # type: ignore
my_config.show_y_guides = False # type: ignore
my_config.width = 1000 # type: ignore


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')