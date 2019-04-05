import {
  LOGIN_SAGA,
  LOGIN_FAIL,
  LOGIN_SUCCESS,

  LOGOUT_SAGA,

  CREATE_NEW_USER_SAGA,
  CREATE_NEW_USER_SUCCESS,
  CREATE_NEW_USER_FAIL,

  CREATE_QUIZ_SAGA,
  CREATE_QUIZ_SUCCESS,
  CREATE_QUIZ_FAIL,

  GET_WHOAMI_SAGA,
  GET_WHOAMI_SUCCESS,
  GET_WHOAMI_FAIL,

  CLEAR_WHOAMI,

  CHANGE_PASSWORD_SAGA,
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

export function createNewUserSaga(token, username, password, role) {
  return {
    type: CREATE_NEW_USER_SAGA,
    token,
    username,
    password,
    role,
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

export function changePasswordSaga(oldPassword, newPassword) {
  return {
    type: CHANGE_PASSWORD_SAGA,
    oldPassword,
    newPassword,
  };
}

export function createQuizSaga() {
  return {
    type: CREATE_QUIZ_SAGA,
  };
}
