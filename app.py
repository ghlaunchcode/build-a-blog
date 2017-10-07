#! /usr/bin/python3

# app.py
# Build A Blog
# 2017, polarysekt

# imports
from flask import Flask, Markup,request, render_template
from flask_sqlalchemy import SQLAlchemy

# init Flask w/ Debugging
g_app = Flask( __name__ )
g_app.config['DEBUG'] = True

# TODO: update to easier way
# init Template directory for jinja env / set autoescaping to true


# ROUTES

@g_app.route( "/" ) #no post
def index( ):
    return render_template('boilerplate.html',ghSite_Name="Build-A-BLog", ghPage_Title="home", ghFlop=Markup("K&spades;A&hearts;3&clubs;8&diams;J&spades;") )

@g_app.route( "/blog" )
def blog():
    return render_template('blog.html',ghSite_Name="Build-A-BLog", ghPage_Title="BLog" )

@g_app.route( "/newpost" )
def newpost():
    return render_template('newpost.html',ghSite_Name="Build-A-Blog", ghPage_Title="New Post" )



def main():
    #print( "begin main()")
    g_app.run()
    #print( "leaving main()")

if __name__ == "__main__":
    main()
