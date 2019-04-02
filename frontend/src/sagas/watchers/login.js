import {push} from 'react-router-redux';
import {
  put,
  takeLatest,
  call,
  all,
} from 'redux-saga/effects';

import {
  LOGIN_SAGA,
  LOGOUT_SAGA,
} from '../../constants';
import {
  loginSagaSuccess,
  loginSagaFailed,
  clearWhoami,
} from '../../actions';
import {login} from '../../lib/api';

function* workerLoginSaga(username, password) {
  try {
    const response = yield call(login, username, password);

    const token = response.access_token;
    if (token !== undefined) {
      yield put(loginSagaSuccess(token));
      yield put(push('/account'));
    }
    else {
      yield put(loginSagaFailed(response));
    }
  } catch (err) {
    yield put(loginSagaFailed(err));
  }
}

function* workerLogoutSaga() {
  yield put(clearWhoami());
}

export default function* watchLoginSaga() {
  yield all([
    takeLatest(LOGIN_SAGA, workerLoginSaga),
    takeLatest(LOGOUT_SAGA, workerLogoutSaga)
  ]);
}
