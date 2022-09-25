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
		coureskillset = set()
		if form.is_valid():
			temp = form.cleaned_data['current_courses']
			temp = temp.split(",")
			courses = []
			for c in temp:
				courses.append(c.strip())

			fin_list = CoursesTable.objects.filter(course__in = courses)
			
			for m in fin_list:
				coureskillset.add(m.courseskills)

			return render(request, "courses_to_jobs/results.html", context={"results": fin_list, "coureskillset": coureskillset})
	else:
		return render(request, "courses_to_jobs/SearchPath.html")

def redirectAboutPage(request):
	return render(request, "courses_to_jobs/aboutPage.html")

def predictJobs(request):
	courseSelected = [request.post.get('course')]

