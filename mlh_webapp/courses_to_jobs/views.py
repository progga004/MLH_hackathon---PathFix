from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from sklearn.feature_extraction.text import CountVectorizer
from courses_to_jobs.models import CoursesTable
from .forms import NameForm
from django.shortcuts import HttpResponseRedirect
import logging
from django.db import connection
from courses_to_jobs.query import provide_jobs_for_course
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "courses_to_jobs/index.html")

def redirectCoursesToJobsView(request):
	logger = logging.getLogger(__name__)
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			courses = form.cleaned_data['current_courses']
			courses = courses.strip().split(",")
			fin_list = CoursesTable.objects.filter(course__in = courses)

			# curr_tuple = CoursesTable.objects.filter(Q(course = c))[::-1]
			# 	fin_list.append(curr_tuple)
			return render(request, "courses_to_jobs/results.html", context={"results": fin_list})
	else:
		return render(request, "courses_to_jobs/SearchPath.html")

def predictJobs(request):
	courseSelected = [request.post.get('course')]

