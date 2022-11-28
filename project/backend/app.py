"""
This file is serves as our Flask backend
"""
import json
import os
from flask import Flask, request, send_from_directory
from modules.search import cliSearch
import settings


def create_app():
    """ This function is used to implement all our flask endpoints for getting data """

    app = Flask(__name__, static_folder='../frontend/build')
    # pylint: disable=R1710
    # pylint: disable=W0621
    fall_search = None
    winter_search = None
    @app.before_first_request
    def initalize_search():
        # pylint: disable=global-variable-undefined
        # pylint: disable=invalid-name
        global fall_search
        global winter_search
        fall_search = cliSearch(settings.COURSE_OUTPUT_FALL)
        winter_search = cliSearch(settings.COURSE_OUTPUT_WINTER)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        if path != "" and os.path.exists(app.static_folder + '/' + path):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')

    # which ever course the user selects from our frontend,
    # is passed through here and its information is returned
    # pylint: disable=W0511
    @app.route('/courses', methods=["POST"])
    def courses():
        # pylint: disable=global-variable-undefined
        # pylint: disable=global-variable-not-assigned
        # pylint: disable=invalid-name
        global fall_search
        global winter_search
        courses = request.json['courses']
        term = request.json['selectedTerm']
        if term == "Fall":
            return fall_search.getCourseObjectsFromSelected(courses)
        if term == "Winter":
            return winter_search.getCourseObjectsFromSelected(courses)
        return "Invalid term"

    # returns all of the course sections
    @app.route('/allCourseSections', methods=["POST"])
    def selector_data():
        # pylint: disable=global-variable-undefined
        # pylint: disable=global-variable-not-assigned
        # pylint: disable=invalid-name
        global fall_search
        global winter_search
        term = request.json['selectedTerm'].lower()
        course_names = None
        if term == "fall":
            course_names = fall_search.processSelectorData()
        if term == "winter":
            course_names = winter_search.processSelectorData()
        response = json.dumps(course_names)
        return response

    # returns courses based on the filter selected by the user
    @app.route('/pickForMe', methods=["POST"])
    def pickForMe():
        # pylint: disable=global-variable-undefined
        # pylint: disable=global-variable-not-assigned
        # pylint: disable=invalid-name
        # pylint: disable=too-many-branches
        # pylint: disable=too-many-return-statements
        # pylint: disable=inconsistent-return-statements
        global fall_search
        global winter_search
        # the below three lines are used to get data about what the user selected in our frontend
        term = request.json['selectedTerm']
        courses = request.json['selectedCourses']
        courseFilter = request.json['filterOption']
        # If the user only wants CIS only courses
        if courseFilter == '1':
            if term == "Fall":
                # pylint: disable=line-too-long
                return fall_search.cisRandomCourses(fall_search.getCourseObjectsFromSelected(courses))
            if term == "Winter":
                # pylint: disable=line-too-long
                return winter_search.cisRandomCourses(winter_search.getCourseObjectsFromSelected(courses))
            return "Invalid term"
        # if the user wants afternoon-only courses
        if courseFilter == '2':
            if term == "Fall":
                # pylint: disable=line-too-long
                return fall_search.afternoonRandomCourses(fall_search.getCourseObjectsFromSelected(courses))
            if term == "Winter":
                # pylint: disable=line-too-long
                return winter_search.afternoonRandomCourses(winter_search.getCourseObjectsFromSelected(courses))
            return "Invalid term"
        # if the user wants morning-only courses
        if courseFilter == '3':
            if term == "Fall":
                # pylint: disable=line-too-long
                return fall_search.morningRandomCourses(fall_search.getCourseObjectsFromSelected(courses))
            if term == "Winter":
                # pylint: disable=line-too-long
                return winter_search.morningRandomCourses(winter_search.getCourseObjectsFromSelected(courses))
            return "Invalid term"
        # if the user wants Tues/Thurs Off
        if courseFilter == '4':
            if term == "Fall":
                # pylint: disable=line-too-long
                return fall_search.getTuesThursOffRandomCourses(fall_search.getCourseObjectsFromSelected(courses))
            if term == "Winter":
                # pylint: disable=line-too-long
                return winter_search.getTuesThursOffRandomCourses(winter_search.getCourseObjectsFromSelected(courses))
            return "Invalid term"
        # If the user wants only randomly chosen courses
        if courseFilter == '5':
            if term == "Fall":
                # pylint: disable=line-too-long
                return fall_search.getRandomCourses(fall_search.getCourseObjectsFromSelected(courses))
            if term == "Winter":
                # pylint: disable=line-too-long
                return winter_search.getRandomCourses(winter_search.getCourseObjectsFromSelected(courses))
            return "Invalid term"
    return app
