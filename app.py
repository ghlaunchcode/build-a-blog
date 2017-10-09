#! /usr/bin/python3

# app.py
# Build A Blog
# 2017, polarysekt

# imports
from flask import Flask, Markup, request, redirect, url_for, render_template

from flask_sqlalchemy import SQLAlchemy

from random import randint

from gh_slogan import *
from gh_poker import *

# init Flask w/ Debugging
g_app = Flask( __name__ )
g_app.config['DEBUG'] = True

#g_app.add_url_rule('/favicon.ico', redirect_to=url_for('static',filename='favicon.ico'))


# ROUTE "/" ==> REDIRECT to '/blog'
@g_app.route( "/" )
def index( ):
    return redirect( url_for('blog'), 302 )

# ROUTE "/flop" is EASTER EGG
@g_app.route( "/flop" )
def flop():
    return render_template('flop.html', ghSite_Name="Easter Egg", ghSlogan=getSlogan(), ghPokerFlop=Markup(getHandHTML()),ghPage_Title="Community" )

# ROUTE "/blog" :: Landing Page / Posts Overview
@g_app.route( "/blog" )
def blog():
    return render_template('blog.html',ghSite_Name="Build-A-BLog", ghSlogan=getSlogan(),ghPage_Title="BLog" )

# ROUTE "/newpost" :: New Blog Post Form [ Get | Post ]
@g_app.route( "/newpost" )
def newpost():
	# TODO: determine if GET or POST
	# GET ==> FORM
	# POST ==> FORM on FAIL
	#      ==> ADD POST on SUCCESS
    return render_template('newpost.html',ghSite_Name="Build-A-Blog", ghSlogan=getSlogan(),ghPage_Title="New Post" )


def main():
    g_app.run()

if __name__ == "__main__":
    main()
