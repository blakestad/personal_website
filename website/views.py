from flask import Blueprint, render_template, request
import requests
import pandas as pd

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/projects/recommend', methods=['GET','POST'])
def recommend():
    if request.method == 'POST':
        input_title=request.form.get('title')
        input_abstract=request.form.get('abstract')

        # Create payload
        payload = {'input_title': input_title, 'input_abstract': input_abstract}

        # The URL of Google Cloud Run service that runs the recommendation backend
        #recommendation_service_url = 'http://127.0.0.1:8080'
        recommendation_service_url = 'https://arxiv-recommender-got5udenaq-uc.a.run.app'

        # Make the POST request
        response = requests.post(recommendation_service_url, json=payload)

        if response.status_code == 200:
            results = pd.DataFrame(response.json())
            return render_template('recommend_output.html', title=input_title, abstract=input_abstract, results=results)
        else:
            return 'Failed to get recommendations', 500
    return render_template('recommend.html')

@views.route('/projects/blog/arxiv')
def recommend_blog():
    return render_template('arxiv_blog.html')

@views.route('/math')
def math():
    return render_template('math.html')

@views.route('/data_science')
def data_science():
    return render_template('datascience.html')