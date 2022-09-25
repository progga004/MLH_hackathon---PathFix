from courses_to_jobs.models import CoursesTable
import csv


def run():
    with open('/Users/pruthvirajpatil/Desktop/MLHack/MLH_hackathon/courses_skills_job_data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        CoursesTable.objects.all().delete()
        for row in reader:
            print(row)
            courses = CoursesTable(jobs = row[1], course = row[2], similarity = row[3], jobskills = row[4], courseskills = row[5])
            courses.save()