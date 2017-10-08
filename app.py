#! /usr/bin/python3

# app.py
# Build A Blog
# 2017, polarysekt

# imports
from flask import Flask, Markup,request, render_template
from flask_sqlalchemy import SQLAlchemy

from random import randint

from gh_poker import *

# init Flask w/ Debugging
g_app = Flask( __name__ )
g_app.config['DEBUG'] = True

g_ghSloganList = [ "DEFAULT SLOGAN", "It's a secret to everyone.", "CTOR BLOGGEN", "Welcome Back" ]


@g_app.route( "/" ) #no post
def index( ):
	#TODO redirect to /blog
    return render_template('boilerplate.html',ghSite_Name="Build-A-BLog", ghSlogan=Markup(getSlogan()), ghPage_Title="home" )

@g_app.route( "/blog" )
def blog():
    return render_template('blog.html',ghSite_Name="Build-A-BLog", ghSlogan=Markup(getSlogan()),ghPage_Title="BLog" )

@g_app.route( "/newpost" )
def newpost():
    return render_template('newpost.html',ghSite_Name="Build-A-Blog", ghSlogan=Markup(getSlogan()),ghPage_Title="New Post" )


def getSlogan():
#    if randint(0,3) == 2:
#        #poker hand
        return "Poker Hand: " + getHandHTML()
#    else:
#        return g_ghSloganList[randint(0,3)]


def main():
    g_app.run()

if __name__ == "__main__":
    main()
