from flask import Flask, render_template
import yaml
app = Flask(__name__)


@app.route('/')
def cook():
  with open('recipe.yaml','r') as f:
    recipe = yaml.safe_load(f)
  
  return render_template('index.html', data=recipe)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
