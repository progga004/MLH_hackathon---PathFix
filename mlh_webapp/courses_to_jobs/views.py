from django.shortcuts import render, redirect
from django.http import HttpResponse
from sklearn.feature_extraction.text import CountVectorizer

# Create your views here.
def index(request):
    return render(request, "courses_to_jobs/index.html")

def predictJobs(request):
	courseSelected = [request.post.get('course')]

