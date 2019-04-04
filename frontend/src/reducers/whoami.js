import {
  GET_WHOAMI_SAGA,
  GET_WHOAMI_SUCCESS,
  GET_WHOAMI_FAIL,
  CLEAR_WHOAMI,
} from '../constants';

const initialState = {};

export default function whoami(state = initialState, action) {
  switch (action.type) {
    case GET_WHOAMI_SAGA:
      return state;
    case GET_WHOAMI_SUCCESS:
      return {
        ...state,
        username: action.username,
        realname: action.realname,
        roles: action.roles,
        questionBanks: action.question_banks,
      };
    case GET_WHOAMI_FAIL:
      return state;
    case CLEAR_WHOAMI:
      return {...initialState};
    default:
      return state;
  }
}
