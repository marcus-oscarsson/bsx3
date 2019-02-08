import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import Counter from '../counter/Counter';

import './main.css';


class Main extends Component {
  render() {
    return (
      <div className="main">
        <div>
          <Route exact path="/" component={Counter} />
        </div>
      </div>
    );
  }
}

export default Main;
