def provide_jobs_for_course(course):
    return """SELECT * FROM CoursesTable where course = {} ORDER BY course DESC LIMIT 10;""".format(course)