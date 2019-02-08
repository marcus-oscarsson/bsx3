/* global it */
import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'connected-react-router';
import store, { history } from './redux-store';

import Main from './Main';

it('renders without crashing', () => {
  const div = document.createElement('div');
  render(
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <Main />
      </ConnectedRouter>
    </Provider>,
    div
  );
  unmountComponentAtNode(div);
});
