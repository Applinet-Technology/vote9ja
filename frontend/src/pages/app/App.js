import React from 'react';
import {BrowserRouter , Route, Link } from "react-router-dom" 
import Home from "../../components/Home/Home" 
import About from "../../components/About/About" 

import Header from '../../components/Header'; 
const App = () => { 
  return ( 
    <div > 
      <Header /> 
      <BrowserRouter> 
        <div> 
        <Route path="/" exact component={Home} /> 
        <Route path="/about" exact component={About} /> 
        </div>  
      </BrowserRouter> 
    </div> 
  ); 
}; 
export default App;
