import React from 'react';
import { Link } from 'react-router-dom';
import { Box, Button, Stack, Flex, useColorModeValue, useColorMode } from '@chakra-ui/react';
import { MoonIcon, SunIcon } from '@chakra-ui/icons';
import { FaHome } from 'react-icons/fa';

/*
This page is used to render our navbar which stays persistent throughout the various
pages in our application
*/

const Navbar = () => {
  // the below line is used to toggle Light mode or Dark Mode in our UI
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <>
      <Box bg={useColorModeValue('gray.100', 'gray.900')} px={4}>
        <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
          <Stack direction={'row'} spacing={8} alignItems={'center'}>
            <Box>
              {/* A logo on our navbar which links to our homepage */}
              <Link to='/'>
                <FaHome />
              </Link>
            </Box>
            <Stack direction={'row'} spacing={4}>
              {/* links to our wiki and course scheduling page */}
              <Link to='/wiki' data-testid='wiki-id'>
                Wiki
              </Link>
              <Link to='/create-schedule'>Scheduler</Link>
            </Stack>
          </Stack>

          <Flex alignItems={'center'}>
            <Stack direction={'row'}>
              {/* used to change the display to dark or light mode */}
              <Button onClick={toggleColorMode}>{colorMode === 'light' ? <MoonIcon /> : <SunIcon />}</Button>
            </Stack>
          </Flex>
        </Flex>
      </Box>
    </>
  );
};

export default Navbar;
