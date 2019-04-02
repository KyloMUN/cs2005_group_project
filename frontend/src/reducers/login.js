import {
  LOGIN_SUCCESS
} from '../constants';

const initialState = {
  token: null,
};

export default function setLoginInfo(state = initialState, action) {
  console.log(action);
  switch (action.type) {
    case LOGIN_SUCCESS:
      return {
        ...state,
        token: action.token,
      };
    default:
      return state;
  }
}
