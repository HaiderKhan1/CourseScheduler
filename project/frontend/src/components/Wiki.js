import React from 'react'
import {
  Box,
  Container,
  Stack,
  Text,
  Heading,
  SimpleGrid,
  StackDivider,
  useColorModeValue,
  List,
  ListItem
} from '@chakra-ui/react'
import '../App.css'
import { Link } from 'react-router-dom'

// This page contains the contents for our Wiki page, this will be updated every sprint as neccessary

const Wiki = () => {
  return (
    <Container maxW={'6xl'}>
      <SimpleGrid
        columns={{ base: 1, lg: 1 }}
        spacing={{ base: 8, md: 10 }}
        py={{ base: 10, md: 10 }}>
        <Stack spacing={{ base: 6, md: 10 }}>
          <Box as={'header'}>
            <Heading
              lineHeight={1.1}
              fontWeight={600}
              color={'green.400'}
              fontSize={{ base: '2xl', sm: '4xl', lg: '5xl' }}>
              Course Scheduler
            </Heading>
          </Box>

          <Stack
            spacing={{ base: 4, sm: 6 }}
            direction={'column'}
            divider={
              <StackDivider
                borderColor={useColorModeValue('gray.200', 'gray.600')}
              />
            }>
            <Text
              color={useColorModeValue('gray.500', 'gray.400')}
              fontSize={'2xl'}
              fontWeight={'300'}>
              A web application that allows University of Guelph students to select courses and see their schedule.
            </Text>

            <Box>
              <Text
                fontSize={{ base: '16px', lg: '18px' }}
                color={useColorModeValue('green.500', 'green.300')}
                fontWeight={'500'}
                textTransform={'uppercase'}
                mb={'4'}>
                External IP Address
              </Text>

              <SimpleGrid columns={{ base: 1, md: 2 }} spacing={10}>
                <List spacing={2}>
                  <ListItem>34.130.250.108</ListItem>
                </List>
              </SimpleGrid>
            </Box>
            <Box>
              <Text
                fontSize={{ base: '16px', lg: '18px' }}
                color={useColorModeValue('green.500', 'green.300')}
                fontWeight={'500'}
                textTransform={'uppercase'}
                mb={'4'}>
                How to make your University course calendar
              </Text>

              <List spacing={2}>
                <ListItem>
                  Navigate to the <Link style={{ color: 'green' }} to="/create-schedule"> Scheduler </Link> page
                </ListItem>
                <ListItem>
                  Select the semester (Fall/Winter) you want to pick courses for
                </ListItem>
                <ListItem>
                  Use the selector to search and select your courses (maximum 5)
                </ListItem>
                <ListItem>
                  Click Draw Schedule
                </ListItem>
              </List>
            </Box>
            <Box>
              <Text
                fontSize={{ base: '16px', lg: '18px' }}
                color={useColorModeValue('green.500', 'green.300')}
                fontWeight={'500'}
                textTransform={'uppercase'}
                mb={'4'}>
                Help! I dont know which course I want to pick
              </Text>

              <Text
                fontSize={{ base: '14px', lg: '16px' }}
                fontWeight={'400'}
                color={useColorModeValue('green.500', 'green.300')}
                mb={'4'}>
               Selecting the Apply Filter option yeilds 5 filters for you to choose from to help you {<br></br>} create a schedule if you are unsure of what to pick!
              </Text>

              <List spacing={2}>
                <ListItem>

                <Text
                fontSize={{ base: '16px', lg: '18px' }}
                color={useColorModeValue('green.500', 'green.300')}
                fontWeight={'500'}
                textTransform={'uppercase'}
                mb={'4'}>
                Filters:
              </Text>

                </ListItem>
                <ListItem>
                  CIS Only - Suggests Only CIS courses
                </ListItem>
                <ListItem>
                  Morning Off - Suggests Only courses which meetings times are in the evenings only.
                </ListItem>
                <ListItem>
                  Afternoons Off - Suggests Only courses which meetings times are in the mornings only.
                </ListItem>
                <ListItem>
                  Tuesday/Thursday Off - Suggests Only courses that are offered on Monday Wednesday Friday.
                </ListItem>
                <ListItem>
                  Random - Suggests Courses at random.
                </ListItem>
                <ListItem>
                  <Text
                  fontSize={{ base: '16px', lg: '18px' }}
                  color={useColorModeValue('green.500', 'green.300')}
                  fontWeight={'500'}
                  textTransform={'uppercase'}
                  mb={'4'}>
                  Pick For Me Button
                  </Text>
                  </ListItem>
                  <ListItem>
                  Firstly select a filter from the above options.
                </ListItem>
                <ListItem>
                  If you have any selected courses, it will pick the remaining number of courses you can schedule based on the filter you provided.
                </ListItem>
                <ListItem>
                  If you did not select any courses, it will pick 5 non-overlapping courses based on the filter you provided.
                </ListItem>
                <ListItem>
                  Navigate to the <Link style={{ color: 'green' }} to="/create-schedule"> Scheduler </Link> page
                </ListItem>
                <ListItem>
                  Select the semester (Fall/Winter) you want to pick courses for
                </ListItem>
                <ListItem>
                  Click Pick For Me
                </ListItem>

              </List>

            </Box>
          </Stack>
        </Stack>
      </SimpleGrid>
    </Container>
  )
}
export default Wiki
