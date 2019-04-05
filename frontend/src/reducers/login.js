import {
  LOGIN_SAGA,
  LOGIN_SUCCESS,
  LOGIN_FAIL,

  LOGOUT_SAGA,
} from '../constants';

const initialState = {
  token: null,
  loggedIn: false,
};

export default function login(state = initialState, action) {
  switch (action.type) {
    case LOGIN_SAGA:
      return state;
    case LOGIN_SUCCESS:
      return {
        ...state,
        token: action.token,
        loggedIn: true,
      };
    case LOGIN_FAIL:
      return state;
    case LOGOUT_SAGA:
      return {...initialState};
    default:
      return state;
  }
}
