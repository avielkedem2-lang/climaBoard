import { Route, Routes } from 'react-router'
import './App.css'
import Welcome from './components/pages/Welcome/Welcome'
import Dashboard from './components/pages/Dashboard/Dashboard'
import Search from './components/pages/Search/Search'
import Favorites from './components/pages/Favorites/Favorites'
import Layout from './components/Layout/Layout'
import CityDetails from './components/pages/CityDetails/CityDetails'

function App() {

  return (
    <>
      <Routes>
        <Route path='/' element={<Welcome />} />
        <Route element={<Layout />}>
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/search' element={<Search />} />
          <Route path='/city-details/:city' element={<CityDetails/>} />
          <Route path='/favorites' element={<Favorites />} />
        </Route>
        <Route path='*' element="404 not found" />
      </Routes>
    </>
  )
}

export default App
