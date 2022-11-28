import * as React from 'react';
import {
  Alert,
  AlertIcon,
  Box,
  Container,
  FormControl,
  FormLabel,
  Button,
  Flex,
  Spacer,
  Spinner,
  Radio,
  RadioGroup,
  Stack,
  ListItem,
  UnorderedList,
} from '@chakra-ui/react';
import { Select as ChakraSelect } from 'chakra-react-select';
import '../App.css';
import axios from 'axios';
import { useState } from 'react';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';
import tippy from 'tippy.js';
/*
This is the scheduler page where we ask the user to select (up to 5) courses and display them elegantly
in a calender
*/

const Scheduler = () => {
  const [selectorData, setSelectorData] = useState({});
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [events, setEvents] = useState([]);
  const [isVisible, setIsVisible] = useState(false);
  const [isCoursesDrawn, setisCoursesDrawn] = useState(false);
  const [courseTerm, setTerm] = useState('');
  const [filterButton, setFilterButtonVisibility] = useState(false);
  const [filterValue, setFilterValue] = useState('');
  const [alert, setAlert] = useState(false);
  const [printCourses, setPrintCourses] = useState([]);
  // function to display the various courses inside the drop-down select
  async function getSelectorData(term) {
    try {
      axios
        .post('/allCourseSections', {
          selectedTerm: term,
        })
        .then(
          (response) => {
            setSelectorData({
              data: response.data,
            });
          },
          (error) => {
            console.log(error);
          }
        );
    } catch (err) {
      console.log(Object.keys(err), err.message);
    }
  }

  const options = [
    { value: 'Fall courses', label: 'Fall' },
    { value: 'Winter courses', label: 'Winter' },
  ];

  // function to tell us what semester the user selected
  function handleInputChange(newValue) {
    setIsVisible(true);
    setSelectorData({
      data: null,
    });
    setSelectedOptions('');
    getSelectorData(newValue.label);
    setTerm(newValue.label);

    console.log(newValue.label);
  }

  const changeVisiblity = () => {
    setFilterButtonVisibility(!filterButton);
    // resetting filter options if the "Apply Filter" button is clicked
    setFilterValue('');
  };
  // our 'main' function which draws the events (courses) into the calender
  function drawSchedule(courses) {
    const days = {};

    days.Mon = 'Mon Nov 07 2022';
    days.Tues = 'Tue Nov 08 2022';
    days.Wed = 'Wed Nov 09 2022';
    days.Thur = 'Thu Nov 10 2022';
    days.Fri = 'Fri Nov 11 2022';

    const eventsTemp = [];
    const courseNames = [];
    // add the course names to a list so they can be printed to the scheduler
    courses.forEach((course) => {
      courseNames.push(course.Name);
    });
    setPrintCourses(courseNames);
    setisCoursesDrawn(true);
    courses.forEach((course) => {
      let temp = {};
      let hour, intTime, stringHour, unslicedtime;
      // this below condition is to check if the course has any lecture times
      if (Object.prototype.hasOwnProperty.call(course['Meeting Information'], 'lec')) {
        course['Meeting Information'].lec[0].forEach((day) => {
          temp.title = course.Name;
          // get the starting time for the course
          temp.start = course['Meeting Information'].lec[1][0];
          unslicedtime = temp.start;
          // remove the AM or PM from the time string
          temp.start = temp.start.slice(0, -2);
          hour = temp.start.slice(0, 2);
          // convert time to military time to make sure our date is formatted correctly
          if (unslicedtime.includes('PM') && !unslicedtime.includes('12')) {
            intTime = parseInt(hour) + 12;
          } else {
            intTime = parseInt(hour);
          }

          stringHour = intTime.toString();
          temp.start = temp.start.slice(2);
          // concat the new time together to get our time in military format
          temp.start = stringHour + temp.start;

          temp.end = course['Meeting Information'].lec[1][1];
          unslicedtime = temp.end;
          temp.end = temp.end.slice(0, -2);
          hour = temp.end.slice(0, 2);
          if (unslicedtime.includes('PM') && !unslicedtime.includes('12')) {
            intTime = parseInt(hour) + 12;
          } else {
            intTime = parseInt(hour);
          }
          stringHour = intTime.toString();
          temp.end = temp.end.slice(2);
          temp.end = stringHour + temp.end;

          temp.start = Date.parse(days[day] + ' ' + temp.start);
          temp.end = Date.parse(days[day] + ' ' + temp.end);
          eventsTemp.push(temp);
          temp = {};
        });
      }
      if (Object.prototype.hasOwnProperty.call(course['Meeting Information'], 'lab')) {
        course['Meeting Information'].lab[0].forEach((day) => {
          temp.title = course.Name;
          // get the starting time for the course
          temp.start = course['Meeting Information'].lab[1][0];
          unslicedtime = temp.start;
          // remove the AM or PM from the time string
          temp.start = temp.start.slice(0, -2);
          hour = temp.start.slice(0, 2);
          // convert time to military time to make sure our date is formatted correctly
          if (unslicedtime.includes('PM') && !unslicedtime.includes('12')) {
            intTime = parseInt(hour) + 12;
          } else {
            intTime = parseInt(hour);
          }

          stringHour = intTime.toString();
          temp.start = temp.start.slice(2);
          // concat the new time together to get our time in military format
          temp.start = stringHour + temp.start;

          temp.end = course['Meeting Information'].lab[1][1];
          unslicedtime = temp.end;
          temp.end = temp.end.slice(0, -2);
          hour = temp.end.slice(0, 2);
          if (unslicedtime.includes('PM') && !unslicedtime.includes('12')) {
            intTime = parseInt(hour) + 12;
          } else {
            intTime = parseInt(hour);
          }
          stringHour = intTime.toString();
          temp.end = temp.end.slice(2);
          temp.end = stringHour + temp.end;

          temp.start = Date.parse(days[day] + ' ' + temp.start);
          temp.end = Date.parse(days[day] + ' ' + temp.end);
          // make labs appear green
          temp.color = 'green';
          eventsTemp.push(temp);
          temp = {};
        });
      }
      if (Object.prototype.hasOwnProperty.call(course['Meeting Information'], 'seminar')) {
        course['Meeting Information'].seminar[0].forEach((day) => {
          temp.title = course.Name;
          // get the starting time for the course
          temp.start = course['Meeting Information'].seminar[1][0];
          unslicedtime = temp.start;
          // remove the AM or PM from the time string
          temp.start = temp.start.slice(0, -2);
          hour = temp.start.slice(0, 2);
          // convert time to military time to make sure our date is formatted correctly
          if (unslicedtime.includes('PM') && !unslicedtime.includes('12')) {
            intTime = parseInt(hour) + 12;
          } else {
            intTime = parseInt(hour);
          }

          stringHour = intTime.toString();
          temp.start = temp.start.slice(2);
          // concat the new time together to get our time in military format
          temp.start = stringHour + temp.start;

          temp.end = course['Meeting Information'].seminar[1][1];
          unslicedtime = temp.end;
          temp.end = temp.end.slice(0, -2);
          hour = temp.end.slice(0, 2);
          if (unslicedtime.includes('PM') && !unslicedtime.includes('12')) {
            intTime = parseInt(hour) + 12;
          } else {
            intTime = parseInt(hour);
          }
          stringHour = intTime.toString();
          temp.end = temp.end.slice(2);
          temp.end = stringHour + temp.end;

          temp.start = Date.parse(days[day] + ' ' + temp.start);
          temp.end = Date.parse(days[day] + ' ' + temp.end);

          // make seminars appear purple
          temp.color = 'purple';
          eventsTemp.push(temp);
          temp = {};
        });
      }
    });
    // use spread operator to set the event in our events object
    setEvents([...eventsTemp]);
  }

  // function to grab the course data based on what course the user selected
  function getSelectedCourseData() {
    // show an alert if the user does not select a course when they click 'Draw Schedule'
    if (selectedOptions.length === 0) {
      setAlert(true);
    } else {
      setAlert(false);
      axios
        .post('/courses', {
          courses: selectedOptions,
          selectedTerm: courseTerm,
        })
        .then(function (response) {
          drawSchedule(response.data);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }

  // function that randomly returns courses (without conflict) based on what the user selected
  function selectCoursesForUser() {
    try {
      // sends the selected course term and selected courses (if any) to backend
      axios
        .post('/pickForMe', {
          selectedTerm: courseTerm,
          selectedCourses: selectedOptions,
          filterOption: filterValue,
        })
        .then(
          (response) => {
            drawSchedule(response.data);
          },
          (error) => {
            console.log(error);
          }
        );
    } catch (err) {
      console.log(Object.keys(err), err.message);
    }
  }
  // adds the names of the courses selected to a list
  function Feature({ value }) {
    return (
      <UnorderedList>
        {value.map((cName) => (
          <ListItem key={cName}>{cName}</ListItem>
        ))}
      </UnorderedList>
    );
  }
  return (
    <Container maxW={'4xl'}>
      <Box py={{ base: 10, md: 18 }}>
        {/* using a JS library to help make our scheduler */}
        <FullCalendar
          plugins={[timeGridPlugin]}
          events={events}
          initialDate={'2022-11-07'}
          headerToolbar={{
            left: 'today',
            center: 'title',
            right: 'timeGridWeek',
          }}
          // pop-up for displaying the full name of the event when hovering
          eventMouseEnter={(arg) => {
            tippy(arg.el, {
              // .slice is used to remove the " " which encompasses the name from the JSON.stringify call
              content: JSON.stringify(arg.event.title).slice(1, -1),
              theme: 'orange',
            });
          }}
        />

        <Box>
          {/* a very minimalistic legend for our calender */}
          <h3 className='legend'>
            {' '}
            Lectures: <span className='lecs'></span> Labs: <span className='labs'></span> Seminars: <span className='sem'></span>{' '}
          </h3>
          {alert && (
            <Alert status='error'>
              <AlertIcon />
              Please select at least one course.
            </Alert>
          )}
          {/* list of courses selected by the user */}
        </Box>
        {isCoursesDrawn && (
          <Box>
            <Feature value={printCourses} />
          </Box>
        )}
        <FormControl marginY={10}>
          <FormLabel>Select semester</FormLabel>
          <Flex w='100%' direction={{ base: 'column', md: 'row' }}>
            <Box w={{ md: '65%' }}>
              <ChakraSelect
                id='semesterSelect'
                onChange={handleInputChange}
                placeholder='Select the semester you want to make a schedule for'
                options={options}
              />
            </Box>
            <Spacer />
            {/* we only want to show the filter option when a semester is picked */}
            {isVisible && (
              <Stack direction={'column'}>
                {!filterButton && (
                  <Button onClick={changeVisiblity} colorScheme='whatsapp'>
                    Apply Filter
                  </Button>
                )}
                {filterButton && (
                  <Container>
                    <Stack align={'center'}>
                      <RadioGroup onChange={setFilterValue} value={filterValue}>
                        <Stack direction='row'>
                          <Radio value='1'>CIS Only</Radio>
                          <Radio value='2'>Mornings Off</Radio>
                          <Radio value='3'>Afternoons Off</Radio>
                          <Radio value='4'>Tues/Thurs Only</Radio>
                          <Radio value='5'>Random</Radio>
                        </Stack>
                      </RadioGroup>
                      <Spacer />
                      <Button colorScheme='whatsapp' marginTop={{ base: 3, md: 0 }} onClick={selectCoursesForUser} size={'sm'} width='110px'>
                        Pick For Me
                      </Button>
                      <Spacer />
                    </Stack>
                  </Container>
                )}
              </Stack>
            )}
          </Flex>
        </FormControl>
        {/* same idea here, we cant let the user select courses without picking a semester */}
        {isVisible && (
          <FormControl marginY={10}>
            <FormLabel>Select up to 5 courses:</FormLabel>
            <Flex w='100%' direction={{ base: 'column', md: 'row' }} justifyContent={'left'}>
              <Box w={{ md: '65%' }}>
                {!selectorData.data ? (
                  <Flex>
                    <Spinner></Spinner>
                    <Box marginLeft={5}>Loading courses...</Box>
                  </Flex>
                ) : (
                  <ChakraSelect
                    isMulti
                    colorScheme='green'
                    options={selectorData.data}
                    value={selectedOptions}
                    onChange={(o) => setSelectedOptions(o)}
                    placeholder='Search for courses'
                    closeMenuOnSelect={false}
                    // limit the max amount of courses the user can pick to 5
                    isOptionDisabled={() => selectedOptions.length >= 5}
                  />
                )}
              </Box>
              <Spacer />
              <Button colorScheme='whatsapp' marginTop={{ base: 3, md: 0 }} onClick={getSelectedCourseData}>
                Draw Schedule
              </Button>
            </Flex>
          </FormControl>
        )}
      </Box>
    </Container>
  );
};

export default Scheduler;
