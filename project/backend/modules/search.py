"""
This file is serves as our course searching module
"""
import json
import re
from collections import defaultdict
from random import randrange
from datetime import datetime
# pylint: disable=C0103
class cliSearch:
    """ This class is used to implement all our searching functionality """
    # pylint: disable=C0301
    # pylint: disable=C0200
    def __init__(self, pathToDataFile):
        """initializes the class"""
        with open(pathToDataFile, "r", encoding="utf-8") as read_file:
            self.courseData = json.load(read_file)

        # is a mapping between each course's uid to it's formatted information
        self.idToCourse = defaultdict(dict)
        # populates the above map
        self.processIdToCourse()

        # is a mapping of each course (key = course code, i.e CIS3760)
        # and its value is the ids of all it's sections
        self.searchByCourseDict = defaultdict(list)
        # populates the above map
        self.processCoreSearch()

        #self.processSelectorData()


    def processIdToCourse(self):
        """ creates a hash map such that:
        the course uid maps to course info
        doing it this way, saves us the processing time to neatly organize info in every search """
        keys = ["Name", "Faculty", "Status", "Available", "Credits",
                "Term", "Academic Level", "Location", "Meeting Information"]
        for i in range(len(self.courseData)):
            for key in keys:
                self.idToCourse[self.courseData[i]["id"]][key] = self.courseData[i][key]

    def processCoreSearch(self):
        """creates a hashmap
        keys are every single course code, and for every code the value are the uids of different sections"""
        for i in range(len(self.courseData)):
            courseInfo = self.courseData[i]["Name"].split()
            courseCode = courseInfo[0].split("*")
            key = courseCode[0]+courseCode[1]
            self.searchByCourseDict[key].append(self.courseData[i]["id"])

    def searchByCourse(self, course):
        """we can do a constant time lookup on all sections of a course
        given course which is the key for the searchbycoursedict
        we simply obtain the course information of all sections and return it"""
        if not self.courseExists(course):
            return []

        courses = []
        for i in self.searchByCourseDict[course]:
            courses.append(self.idToCourse[i])

        return courses


    def courseExists(self, course):
        """function to determine if the course code even exists"""
        if course not in self.searchByCourseDict:
            return False

        return True


    def processSelectorData(self):
        """populate the selector with all of the course names."""
        selectorData = []
        # populate the selector with all of the course names.
        for i in range(len(self.courseData)):

            info = {}
            courseInfo = self.courseData[i]["Name"].split()
            courseCode = courseInfo[0].split("*")
            key = courseCode[0]+courseCode[1]
            info["value"] = key
            info["label"] = self.courseData[i]["Name"]
            selectorData.append(info)

        return selectorData

    def getCourseObjectsFromSelected(self, selected):
        """get the data of the courses selected."""
        courses = []
        for course in selected:
            name = re.sub('[\\W_]+', '', course['value']).upper()
            for section in self.searchByCourse(name):
                if section['Name'] == course['label']:
                    courses.append(section)

        return courses
    def to24HrTime(self, time):
        """ensure that all time data is in 24 hour format for easier frontend parsing"""
        if time == "Times TBA":
            return "0:00"
        in_time = datetime.strptime(time, "%I:%M%p")
        return datetime.strftime(in_time, "%H:%M")

    def meetingInfoToMap(self, meetingInformation):
        """map the meeting information in interval format to check for overlapping courses"""
        time_map = {}
        for info in meetingInformation.values():
            if len(info[1]) == 1:
                info[1].append(info[1][0])
            interval = (self.to24HrTime(info[1][0]), self.to24HrTime(info[1][1]))
            for day in info[0]:
                if day not in time_map:
                    time_map[day] = [interval]
                else:
                    time_map[day].append(interval)

        return time_map
    def addToMap(self, curr, toAdd):
        """ simple function to add to the interval map."""
        for day, intervals in toAdd.items():
            if day not in curr:
                curr[day] = intervals
            else:
                curr[day].extend(intervals)
    def getRandomViableCourse(self, courses, timeMap):
        """pull a random course by id and check if it does not overlap with any other courses"""
        randomId = randrange(len(self.idToCourse.keys()))
        candidateCourse = self.idToCourse[randomId]

        for course in courses:
            if course["Name"].split("*")[0] == candidateCourse["Name"].split("*")[0]:
                return {}

        courseTimeMap = self.meetingInfoToMap(candidateCourse["Meeting Information"])

        for day, intervals in courseTimeMap.items():
            if day not in timeMap:
                continue
            for candidateInterval in intervals:
                for currInterval in timeMap[day]:
                    if candidateInterval[0] <= currInterval[0]:
                        if candidateInterval[1] > currInterval[0]:
                            return {}
                    elif candidateInterval[1] >= currInterval[1]:
                        if candidateInterval[0] < currInterval[1]:
                            return {}
                    elif candidateInterval[0] >= currInterval[0] and candidateInterval[1] <= currInterval[1]:
                        return {}
        return {
            'timeMap': courseTimeMap,
            'course': candidateCourse
        }
    def getRandomViableCISOnlyCourse(self, courses, timeMap):
        """same function as above, except for the CIS filter."""
        randomId = randrange(len(self.idToCourse.keys()))
        candidateCourse = self.idToCourse[randomId]

        # if the randomly picked course is not CIS, we keep randomly picking until it is
        while "CIS" not in candidateCourse["Name"].split("*")[0]:
            randomId = randrange(len(self.idToCourse.keys()))
            candidateCourse = self.idToCourse[randomId]

        # making sure the courses are not the same by checking their names
        for course in courses:
            if course["Name"].split("*")[2] == candidateCourse["Name"].split("*")[2]:
                return {}

        courseTimeMap = self.meetingInfoToMap(
            candidateCourse["Meeting Information"])

        for day, intervals in courseTimeMap.items():
            if day not in timeMap:
                continue
            for candidateInterval in intervals:
                for currInterval in timeMap[day]:
                    if candidateInterval[0] <= currInterval[0]:
                        if candidateInterval[1] > currInterval[0]:
                            return {}
                    elif candidateInterval[1] >= currInterval[1]:
                        if candidateInterval[0] < currInterval[1]:
                            return {}
                    elif candidateInterval[0] >= currInterval[0] and candidateInterval[1] <= currInterval[1]:
                        return {}
        return {
            'timeMap': courseTimeMap,
            'course': candidateCourse
        }
    def getRandomCourses(self, courses):
        """ generate a list of 5 random courses (inclusive of those already selected) within 100 tries."""
        timeMap = {}

        for course in courses:
            self.addToMap(timeMap, self.meetingInfoToMap(course["Meeting Information"]))
        attempts = 0
        while len(courses) <= 4 or attempts > 100:
            courseInfo = self.getRandomViableCourse(courses, timeMap)
            if courseInfo and "Days" not in courseInfo["timeMap"]:
                courses.append(courseInfo["course"])
                self.addToMap(timeMap, courseInfo["timeMap"])
            attempts += 1

        return courses
    def cisRandomCourses(self, courses):
        """same as above, but for the cis filter."""
        timeMap = {}

        for course in courses:
            self.addToMap(timeMap, self.meetingInfoToMap(
                course["Meeting Information"]))
        attempts = 0
        while len(courses) <= 4 or attempts > 100:
            courseInfo = self.getRandomViableCISOnlyCourse(courses, timeMap)
            if courseInfo and "Days" not in courseInfo["timeMap"]:
                courses.append(courseInfo["course"])
                self.addToMap(timeMap, courseInfo["timeMap"])
            attempts += 1

        return courses
    def afternoonRandomCourses(self, courses):
        """same as the default get random courses function, but only select afternoon courses."""
        timeMap = {}
        timeList = []
        endTime = "12:00"
        for course in courses:
            self.addToMap(timeMap, self.meetingInfoToMap(
                course["Meeting Information"]))
        attempts = 0

        while len(courses) <= 4 or attempts > 100:
            timeTracker = 0
            courseInfo = self.getRandomViableCourse(courses, timeMap)
            if courseInfo and "Days" not in courseInfo["timeMap"]:
                for val in courseInfo["timeMap"].values():
                    # subtracting the time values from end time (12) to see if its afternoon-only course
                    timeList.append(datetime.strptime((val[0][0]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
                    timeList.append(datetime.strptime((val[0][1]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
                    # we enter this if statement if the course has a lab or seminar (along with lecture)
                    if len(val) > 1:
                        timeList.append(datetime.strptime((val[1][0]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
                        timeList.append(datetime.strptime((val[1][1]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
            for x in timeList:
                # we use the .days to check if the time falls in the morning (0) or afternoon (-1)
                if x.days !=0:
                    timeTracker = 1
            if courseInfo and "Days" not in courseInfo["timeMap"] and timeTracker == 0:
                courses.append(courseInfo["course"])
                self.addToMap(timeMap, courseInfo["timeMap"])
                attempts += 1
            # lastly, clear our list for the next iteration
            timeList.clear()
        return courses
    def morningRandomCourses(self, courses):
        """same as the default get random courses function, but only select morning courses."""
        timeMap = {}
        timeList = []
        endTime = "12:00"
        for course in courses:
            self.addToMap(timeMap, self.meetingInfoToMap(
                course["Meeting Information"]))
        attempts = 0

        while len(courses) <= 4 or attempts > 100:
            timeTracker = 0
            courseInfo = self.getRandomViableCourse(courses, timeMap)
            if courseInfo and "Days" not in courseInfo["timeMap"]:
                for val in courseInfo["timeMap"].values():
                    # subtracting the time values from end time (12) to see if its afternoon-only course
                    timeList.append(datetime.strptime((val[0][0]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
                    timeList.append(datetime.strptime((val[0][1]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
                    # we enter this if statement if the course has a lab or seminar (along with lecture)
                    if len(val) > 1:
                        timeList.append(datetime.strptime((val[1][0]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
                        timeList.append(datetime.strptime((val[1][1]), "%H:%M") - datetime.strptime(endTime, "%H:%M"))
            for x in timeList:
                # we use the .days to check if the time falls in the morning (0) or afternoon (-1)
                if x.days !=-1:
                    timeTracker = 1
            if courseInfo and "Days" not in courseInfo["timeMap"] and timeTracker == 0:
                courses.append(courseInfo["course"])
                self.addToMap(timeMap, courseInfo["timeMap"])
                attempts += 1
            # lastly, clear our list for the next iteration
            timeList.clear()
        return courses
    def getTuesThursOffRandomCourses(self, courses):
        """ same as the default get random courses function, but only select courses that are Mon, Wed, and Fri."""
        timeMap = {}
        for course in courses:
            self.addToMap(timeMap, self.meetingInfoToMap(course["Meeting Information"]))
        attempts = 0

        while len(courses) <= 4 or attempts > 100:
            courseInfo = self.getRandomViableCourse(courses, timeMap)
            if courseInfo and "Days" not in courseInfo["timeMap"]:
                # here we check if the course only has Tuesday or Thursday times
                if 'Wed' not in courseInfo["timeMap"]:
                    if 'Mon' not in courseInfo["timeMap"]:
                        if 'Fri' not in courseInfo["timeMap"]:
                            courses.append(courseInfo["course"])
                            self.addToMap(timeMap, courseInfo["timeMap"])
                            attempts += 1
        return courses
