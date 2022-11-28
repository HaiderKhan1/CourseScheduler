import {
  Box,
  Heading,
  Container,
  Text,
  Button,
  Stack
} from '@chakra-ui/react'
import { Link } from 'react-router-dom'
import React from 'react'

// This is the page that renders content for our landing page, which is our homepage

export default function HomePage () {
  return (
        <>
            <Container maxW={'3xl'}>
                <Stack
                    as={Box}
                    textAlign={'center'}
                    spacing={{ base: 8, md: 14 }}
                    py={{ base: 20, md: 36 }}
                >
                    <Heading
                        fontWeight={600}
                        fontSize={{ base: '2xl', sm: '4xl', md: '6xl' }}
                        lineHeight={'110%'}
                    >
                        University of Guelph
                        <br />
                        <Text as={'span'} color={'green.400'}>
                            Scheduling Made Easy
                        </Text>
                    </Heading>
                    <Text fontSize='xl' color={'gray.500'}>
                        Have you ever wanted to create your University schedule in a way which was simple yet effective? Look no further! our state-of-the-art scheduler will map out courses for you, all you have to do is tell us what courses you want. Or, use our Pick For Me functionality to have us pick for you!
                    </Text>
                    <Stack
                        direction={'column'}
                        spacing={3}
                        align={'center'}
                        alignSelf={'center'}
                        position={'relative'}
                    >
                        <Link to="/create-schedule">

                            <Button
                                colorScheme={'green'}
                                bg={'green.400'}
                                px={6}
                                _hover={{
                                  bg: 'green.500'
                                }}
                            >
                                Create Schedule
                        </Button>
                        </Link>
                    </Stack>
                </Stack>
            </Container>
        </>
  )
}
