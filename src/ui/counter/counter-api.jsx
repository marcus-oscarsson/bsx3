import axios from 'axios';

// Actions
export const INCREMENT_REQUESTED = 'counter/INCREMENT_REQUESTED';
export const INCREMENT = 'counter/INCREMENT';
export const DECREMENT_REQUESTED = 'counter/DECREMENT_REQUESTED';
export const DECREMENT = 'counter/DECREMENT';
export const SET_LOADING = 'counter/SET_LOADING';
export const SET_COUNT = 'counter/SET_COUNT';
export const INIT = 'counter/INIT';

const API_URL = '/api/counter';

const initialState = {
  count: 0,
  isIncrementing: false,
  isDecrementing: false
};


// Reducer
export default (state = initialState, action) => {
  switch (action.type) {
    case INCREMENT_REQUESTED:
      return {
        ...state,
        isIncrementing: true
      };

    case INCREMENT:
      return {
        ...state,
        count: state.count + 1,
        isIncrementing: !state.isIncrementing
      };

    case DECREMENT_REQUESTED:
      return {
        ...state,
        isDecrementing: true
      };

    case DECREMENT:
      return {
        ...state,
        count: state.count - 1,
        isDecrementing: !state.isDecrementing
      };
    case SET_COUNT:
      return {
        ...state,
        count: action.count,
        isDecrementing: false,
        isIncrementing: false
      };
    case INIT:
      return {
        ...state,
        count: action.count
      };
    default:
      return state;
  }
};


// Action creators
export function increment() {
  return (dispatch) => {
    dispatch({
      type: INCREMENT_REQUESTED
    });

    dispatch({
      type: INCREMENT
    });
  };
}

export function incrementAsync() {
  return (dispatch) => {
    dispatch({
      type: INCREMENT_REQUESTED
    });

    return setTimeout(() => {
      dispatch({
        type: INCREMENT
      });
    }, 3000);
  };
}

export function decrement() {
  return (dispatch) => {
    dispatch({
      type: DECREMENT_REQUESTED
    });

    dispatch({
      type: DECREMENT
    });
  };
}

export function decrementAsync() {
  return (dispatch) => {
    dispatch({
      type: DECREMENT_REQUESTED
    });

    return setTimeout(() => {
      dispatch({
        type: DECREMENT
      });
    }, 3000);
  };
}

export function initSuccess(data) {
  return (dispatch) => {
    dispatch({
      type: INIT,
      files: data
    });
  };
}


export function setLoading(loading) {
  return (dispatch) => {
    dispatch({
      type: SET_LOADING,
      loading
    });
  };
}


export function setCount(count) {
  return (dispatch) => {
    dispatch({
      type: SET_COUNT,
      count
    });
  };
}


export function initCounterRequest() {
  return (dispatch) => {
    dispatch(setLoading(true));
    axios.post(`${API_URL}/get-count`)
      .then((response) => {
        dispatch(setCount(response.data.counter));
      })
      .catch((error) => {
        throw (error);
      })
      .then(() => {
        dispatch(setLoading(false));
      });
  };
}

export function incCounterRequest() {
  return (dispatch) => {
    dispatch(setLoading(true));
    dispatch({ type: INCREMENT_REQUESTED });

    axios.post(`${API_URL}/increment`)
      .then((response) => {
        dispatch(setCount(response.data.counter));
      })
      .catch((error) => {
        throw (error);
      })
      .then(() => {
        dispatch(setLoading(false));
      });
  };
}

export function decCounterRequest() {
  return (dispatch) => {
    dispatch(setLoading(true));
    dispatch({ type: DECREMENT_REQUESTED });

    axios.post(`${API_URL}/decrement`)
      .then((response) => {
        dispatch(setCount(response.data.counter));
      })
      .catch((error) => {
        throw (error);
      })
      .then(() => {
        dispatch(setLoading(false));
      });
  };
}
