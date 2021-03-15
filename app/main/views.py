from flask import render_template,request,redirect,url_for
from ..requests import get_sources,get_articles
from . import main


#views
@main.route('/')
def index():
    
    #View root page function that returns the index page and its data
    

    general = get_sources('general')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')
    health = get_sources('health')
    technology= get_sources('technology')
    science = get_sources('science')

    title = 'Home - Welcome'
    return render_template('index.html',business = business, health=health, science=science, title=title,sports = sports, technology = technology, entertainment = entertainment, general=general)

@main.route('/news/<id>')
def news(id):
    
    #view page function that returns both the news article and it's data
    
    articles = get_articles(id)
    title = 'Home - Welcome'

    return render_template('news.html', articles=articles, title=title)