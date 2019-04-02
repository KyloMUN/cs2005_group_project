import {
  put,
  takeLatest,
  call
} from 'redux-saga/effects';

import {LOGIN_SAGA} from '../../constants';
import {
  loginSagaSuccess,
  loginSagaFailed
} from '../../actions';
import {login} from '../../lib/api';

function* workerLoginSaga(username, password) {
  try {
    const response = yield call(login, username, password);

    const token = response.access_token;
    if (token !== undefined) {
      yield put(loginSagaSuccess(token));
    }
    else {
      yield put(loginSagaFailed());
    }
  } catch (err) {
    console.error(err);
    yield put(loginSagaFailed());
  }
}

export default function* watchLoginSaga() {
  yield takeLatest(LOGIN_SAGA, workerLoginSaga);
}
