import yaml
import jinja2
import os
import shutil
import time

  
data="""
# {{recipe['name']}}
## Ingredients
{% for compo in recipe['composants'] %}
- {{compo['name']}}: {{compo['size']}}
{% endfor %}
## Recette
{% for recipe in recipe['recipe'] %}
- {{recipe}}
{% endfor %}
"""

tm = jinja2.Template(data)

def generate_markdown():
  if os.path.exists('/md'):
    os.system('rm -rf /md')
  if not os.path.exists('/md'):
    os.mkdir('/md')
  if not os.path.exists('/md/docs'):
    os.mkdir('/md/docs')
  shutil.copyfile('/src/mkdocs.yml','/md/mkdocs.yml')
  with open('recipe.yaml','r') as f:
    recipes = yaml.safe_load(f)
    i = 0
    for recipe in recipes:
      if i == 0:
        filename = '/md/docs/index.md'
        i += 1
      else:
        filename = '/md/docs/' + recipe['name'].replace(' ','_') + '.md'
      with open(filename, 'w') as f:
        f.write(tm.render(recipe=recipe))
  os.system('mkdocs build -f /md/mkdocs.yml -d /app')

# main
mtime = 0
while True:
  if mtime != os.path.getmtime('recipe.yaml'):
    mtime = os.path.getmtime('recipe.yaml')
    generate_markdown()
  time.sleep(60)
