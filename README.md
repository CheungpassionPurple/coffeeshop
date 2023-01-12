# coffeeshop

Collaborators: Zoe Frongillo, Kate Piper, Mara Noskowiak, Obi Ogbonna, Nick Escobar, Justin Cheung 

setup is something like this, but will require finagling based on your machine environment (these instructions should be valid for WSL running at least Python 3.9):

`git clone https://<YOUR GIT USERNAME>:<YOUR GIT PASSWORD>@github.com/CheungpassionPurple/coffeeshop.git`

`cd coffeeshop`

`python3 -m venv flask_venv`

`source flask_venv/bin/activate`

`pip install -r my_coffeeshop/requirements.txt`

`cd my_coffeeshop`

to run the server:
`python3 -m openapi_server`