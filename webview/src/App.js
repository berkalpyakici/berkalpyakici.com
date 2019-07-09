import React, { Component } from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import Socials from "./Component/Socials/index";

class App extends Component {
  render() {
    return (
      <Router>
        <Route path="/" exact component={Socials} />
    </Router>
    );
  }
}

export default App;