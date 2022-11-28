from html.parser import HTMLParser
from os.path import exists
import json


class CourseParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.course = {
            "id": None,
            "Meeting Information": {}
        }
        self.coursedata = []
        self.counter = 0

        # Keep track of the last type of HTML tag
        self.lasttype = None
        self.meetingInfo = -1

    def handle_starttag(self, tag, attrs):
        # Loop through attributes of tag in the format of <name> = "<info>"
        if tag == 'p':
            for name, info in attrs:
                if name == 'id':
                    if info.startswith('WSS_COURSE_SECTIONS'):
                        self.lasttype = 'term'
                    if info.startswith('LIST_VAR1'):
                        self.lasttype = 'status'
                    if info.startswith('SEC_LOCATION'):
                        self.lasttype = 'location'
                    if info.startswith('SEC_FACULTY_INFO'):
                        self.lasttype = 'faculty'
                    if info.startswith('LIST_VAR5'):
                        self.lasttype = 'availability'
                    if info.startswith('SEC_MIN_CRED'):
                        self.lasttype = 'credit'
                    if info.startswith('SEC_ACAD_LEVEL'):
                        self.lasttype = 'level'

        elif tag == 'a':
            for name, info in attrs:
                if name == 'id' and info.startswith('SEC_SHORT_TITLE'):
                    self.lasttype = 'name'
        
        elif tag == "div":
            if len(attrs) > 0 and attrs[0][1] == "meet LEC":
                self.key = "lec"
                self.meetingInfo = 0

            if len(attrs) > 0 and attrs[0][1] == "meet LAB":
                self.key = "lab"
                self.meetingInfo = 0
            
            if len(attrs) > 0 and attrs[0][1] == "meet SEM":
                self.key = "seminar"
                self.meetingInfo = 0
            
            if len(attrs) > 0 and attrs[0][1] == "meet EXAM":
                self.key = "exam"
                self.meetingInfo = 0
        

    def handle_data(self, data):
        
        #we are on the div class = meet LAB et
        # process days
        if self.meetingInfo == 0:
            data = data.replace(",", "")
            data = data.split()
            data.pop(0)
            self.course["Meeting Information"][self.key] = [data]
            self.meetingInfo+=1
        # process time
        elif self.meetingInfo == 1:
            data = data.split("-")
            for i in range(len(data)):
                data[i] = data[i].strip()
            
            if self.key == "exam":
                aux = data[-1].split()
                data.pop()
                data.extend(aux)


            self.course["Meeting Information"][self.key].append(data)
            self.meetingInfo+=1
        # # process room
        elif self.meetingInfo == 2:
            self.course["Meeting Information"][self.key].append(data)
            self.meetingInfo+=1
        # we are processing the final div
        elif self.meetingInfo == 3:
            data = data.replace(", ", "")
            self.course["Meeting Information"][self.key].append(data)
            self.meetingInfo = -1
        
        # If type of data is relevant we store them in the object as key value pairs
        if self.lasttype:
            if self.lasttype == 'term':
                self.course["Term"] = (data)
            if self.lasttype == 'status':
                self.course["Status"] = (data)
            if self.lasttype == 'name':
                self.course["Name"] = (data)
            if self.lasttype == 'location':
                self.course["Location"] = (data)
            if self.lasttype == 'faculty':
                self.course["Faculty"] = (data)
            if self.lasttype == 'availability':
                self.course["Available"] = (data)
            if self.lasttype == 'credit':
                self.course["Credits"] = (data)
            
            if self.lasttype == 'level':
                self.course["Academic Level"] = (data)

                self.course["id"] = self.counter  # Add current ID
                self.counter += 1

                # Append current course object to list
                self.coursedata.append(self.course)
                self.course = {  # Re-initialize course object
                    "id": None,
                    "Meeting Information": {}
                }
            

            self.lasttype = None  # Reset last type


def parseHTML() -> None:
    # initialize the CourseParser class to handle Fall courses
    parser_fall = CourseParser()
    # parse fall courses
    html_fall = open("../../../assets/fall_courses.html", "r")

    parser_fall.feed(html_fall.read())
    # write the JSON data into another file
    with open("../../../assets/coursesFall.json", "w") as write_file:
        json.dump(parser_fall.coursedata, write_file)

    html_fall.close()
    parser_fall.close()
    
    # another parser class to handle winter courses
    parser_winter = CourseParser()

    # parse winter courses
    html_winter = open("../../../assets/winter_courses.html", "r")

    parser_winter.feed(html_winter.read())
    with open("../../../assets/coursesWinter.json", "w") as write_file:
        json.dump(parser_winter.coursedata, write_file)

    html_winter.close()
    parser_winter.close()


parseHTML()
