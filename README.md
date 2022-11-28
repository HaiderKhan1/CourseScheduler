# Cource Scheduler
A tool made for the University of Guelph students to help them visualize there course schedules and to detect potential course conflicts in a visually appealing way, as opposed to the less then visually appealing tool offered by the University 😅

## Access the Project on: https://cis3760team105.live/
## Project Demo Video:

[screen-capture.webm](https://user-images.githubusercontent.com/47333610/204354222-9b619d4e-0960-40e0-978a-0e1c07005305.webm)

## Technologies Used:
The Course Scheduler is a full stack web application. 
## Backend:
- The webserver and the API endpoints are developed using Python and Flask.
- The core logic is encapsulated in the Search module developed in Python.
  - Search Module is an object which houses all course information and the functions to operate on the data.
  - Sorts and stores data in dictionaries for O(1) data retrival
  - Has functions and algorithms to select courses for the filters.
- The web app obtains it's course information from a file which contains the information for all course offereings for each semester, that file is then parsed by the HTMLParse module and used in the backend to serve data to the front end.

## Frontend:
- Developed using React, and JavaScript. 
- Leverged ChakraUI to get custom made web components
- Utilized the React-Selector componenet to feed names of all courses to it
  - The react-selector componenet uses a Trie to suggest courses as the user inputs something
- Use the React-Calender API to create the calender component to render the courses

## Hosting Solution
- The project is served using NginX, on a VM in the Google Cloud Platform
- The web app has a SSL certificate, and it's accessed over https
- The project has a custom domain name: cis3760team105
