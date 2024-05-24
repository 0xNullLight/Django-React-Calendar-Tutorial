import './App.css'
import Home from './components/Home'
import About from './components/About'
import Navbar from './components/Navbar'
import {Routes, Route, useLocation} from 'react-router-dom'
import Calendar1 from './components/Calendar1'
import Calendar2 from './components/Calendar2'
import Calendar3 from './components/Calendar3'
import Calendar4 from './components/Calendar4'
import Calendar5 from './components/Calendar5'
import Calendar6 from './components/Calendar6'

function App() {
  return (
    <>
        <Navbar
            content={
              <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route path="/calendar1" element={<Calendar1/>}/>
                    <Route path="/calendar2" element={<Calendar2/>}/>
                    <Route path="/calendar3" element={<Calendar3/>}/>
                    <Route path="/calendar4" element={<Calendar4/>}/>
                    <Route path="/calendar5" element={<Calendar5/>}/>
                    <Route path="/calendar6" element={<Calendar6/>}/>
                    <Route path="/about" element={<About/>}/>
              </Routes>
        }/>
   </>
  )
}

export default App