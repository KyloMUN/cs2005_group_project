import {
  LOGIN_SAGA,
  LOGIN_FAIL,
  LOGIN_SUCCESS,

  LOGOUT_SAGA,

  GET_WHOAMI_SAGA,
  GET_WHOAMI_SUCCESS,
  GET_WHOAMI_FAIL,

  CLEAR_WHOAMI,
} from '../constants';

export function loginSaga(username, password) {
  return {
    type: LOGIN_SAGA,
    username,
    password,
  };
}

export function loginSagaSuccess(token) {
  return {
    type: LOGIN_SUCCESS,
    token,
  };
}

export function loginSagaFailed(err) {
  return {
    type: LOGIN_FAIL,
    err,
  };
}

export function logoutSaga() {
  return {
    type: LOGOUT_SAGA,
  };
}

export function getWhoamiSaga(token) {
  return {
    type: GET_WHOAMI_SAGA,
    token,
  };
}

export function getWhoamiSagaSuccess(whoami) {
  return {
    type: GET_WHOAMI_SUCCESS,
    ...whoami,
  };
}

export function getWhoamiSagaFailed(err) {
  return {
    type: GET_WHOAMI_FAIL,
    err,
  };
}

export function clearWhoami() {
  return {
    type: CLEAR_WHOAMI,
  }
}
