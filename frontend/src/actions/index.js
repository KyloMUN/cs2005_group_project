import {
  LOGIN_SAGA,
  LOGIN_FAIL,
  LOGIN_SUCCESS,

  GET_WHOAMI_SAGA,
  GET_WHOAMI_SUCCESS,
  GET_WHOAMI_FAIL,

  SET_WHOAMI_SAGA,
  SET_WHOAMI_SUCCESS,
  SET_WHOAMI_FAIL,
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

export function loginSagaFailed() {
  return {
    type: LOGIN_FAIL,
  };
}
