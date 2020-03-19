# -*- coding: utf-8 -*-
"""
Showing how to reuse a blueprint for several subdomain
"""
from flask import Flask, Blueprint

app = Flask(__name__)
"""
Note that for subdomains to work reliably, the SERVER_NAME config
variable has to be set. The full syntax is host:port
for example, here we are using localhost:5000.
Something like yoursite.com will be your value, if you are not on localhost
"""
app.config['SERVER_NAME'] = 'localhost:5000'

# The main homepage
@app.route('/')
def app_index():
    return 'Hello, this is the main homepage'

# To replicate the same blueprint for multiple subdomains, the blueprint could
# be created dynamically and returned through a function as defined below.
def subdomain(name, import_name, subdomain, **kwargs):
    '''This function accepts all the arguments as you will normally 
    pass when calling Blueprint, just that subdomain is now required
    '''
    # formulate the Blueprint with the supplied parameters
    subdomain_bp = Blueprint(name, import_name, subdomain=subdomain, **kwargs)
    
    # All the routes goes here
    # The simplest index page can be as stated below
    @subdomain_bp.route('/')
    def subdomain_index():
        return f'''This is subdomain for {name}'''
    return subdomain_bp

# Registering the blueprint multiple times:
# Lets' assign different subdomains to different portions or users of our app
app.register_blueprint(subdomain('firstuser','firstuser','firstuser'))
app.register_blueprint(subdomain('seconduser','seconduser','seconduser'))
app.register_blueprint(subdomain('thirduser','thirduser','thirduser'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)