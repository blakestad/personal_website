from flask import Blueprint, render_template, request, send_file
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

@views.route('/projects/subject-identifier', methods=['GET','POST'])
def identify_subject():
    if request.method == 'POST':
        input_title=request.form.get('title')
        input_abstract=request.form.get('abstract')

        # Create payload
        payload = {'input_title': input_title, 'input_abstract': input_abstract}

        # The URL of Google Cloud Run service that runs the identification backend
        #identification_service_url = 'http://127.0.0.1:8080'
        identification_service_url = 'https://arxiv-subject-identifier-got5udenaq-uc.a.run.app'

        # Make the POST request
        response = requests.post(identification_service_url, json=payload)

        if response.status_code == 200:
            results = pd.DataFrame(response.json())
            results.sort_values('prob',ascending=False,inplace=True)
            if results['guess'].sum() > 0:
                positive_results = results[results['guess']]
                return render_template('subject_identifier_output.html', title=input_title, abstract=input_abstract, results=positive_results)
            else:
                top_results = results.head(3)
                return render_template('subject_identifier_invalid_output.html', title=input_title, abstract=input_abstract, results=top_results)
        else:
            return 'Failed to get identifications', 500
    return render_template('subject_identifier.html')

@views.route('/blog/arxiv')
def arxiv_blog():
    return render_template('arxiv_blog.html')

@views.route('/software/resume')
def resume():
    return send_file('static/pdfs/blakestad_resume_20240104.pdf', download_name='blakestad_resume.pdf')

@views.route('/math')
def math():
    return render_template('math.html')

@views.route('/software')
def software():
    return render_template('software.html')

@views.route('/sitemap.xml')
def sitemap():
    return send_file('static/sitemap/sitemap.xml', download_name='sitemap.xml')