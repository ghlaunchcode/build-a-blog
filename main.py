# main.py
# Build A Blog
# 2017, polarysekt

# imports
from flask import Flask, request
import os
import cgi
import jinja2

# init Flask w/ Debugging
g_app = Flask( __name__ )
g_app.config['DEBUG'] = True

# init Template directory for jinja env / set autoescaping to true
g_template_dir = os.path.join( os.path.dirname(__file__), 'templates' )
g_jinja_env = jinja2.Environment( loader =  jinja2.FileSystemLoader( g_template_dir ), autoescape=True )


# ROUTES

@g_app.route( "/" ) #no post
def index( ):
    # open template
    indexTemplate = g_jinja_env.get_template('index.html')
    return indexTemplate.render(title="New User")


@g_app.route( "/blog" )


@g_app.route( "/newpost" )



def main():
    #print( "begin main()")
    g_app.run()
    #print( "leaving main()")

if __name__ == "__main__":
    main()
