import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import * as CounterAPI from './counter-api';

class Counter extends React.Component {
  render() {
    return (
      <p>
        {`Clicked ${this.props.count} times`}
        {' '}
        <button type="button" onClick={this.props.incCounterRequest}>
          +
        </button>
        {' '}
        <button type="button" onClick={this.props.decCounterRequest}>
          -
        </button>
        {' '}
        <button type="button" onClick={this.props.incrementAsync}>
          Increment async
        </button>
        {' '}
        <button type="button" onClick={this.props.decrementAsync}>
          Decrement async
        </button>
      </p>
    );
  }
}

function mapStateToProps({ counter }) {
  return {
    count: counter.count,
    isIncrementing: counter.isIncrementing,
    isDecrementing: counter.isDecrementing
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(CounterAPI, dispatch);
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Counter);
