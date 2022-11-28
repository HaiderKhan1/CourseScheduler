import * as React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './Home'
import Wiki from './components/Wiki'
import Navbar from './components/Navbar'
import Scheduler from './components/Scheduler'
import { ChakraProvider } from '@chakra-ui/react'

export default function App () {
  return (
    <ChakraProvider>
      <BrowserRouter>
        <Navbar />
        <Routes>
          {/* we use the below Route component to route to the various different pages we have in our UI */}
          <Route exact path="/" element={<Home />} />
          <Route exact path="/wiki" element={<Wiki />} />
          <Route exact path="/create-schedule" element={<Scheduler />} />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  )
}
