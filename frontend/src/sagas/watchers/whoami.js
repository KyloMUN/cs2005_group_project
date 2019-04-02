import {
  put,
  takeLatest,
  call
} from 'redux-saga/effects';

import {GET_WHOAMI_SAGA} from '../../constants';
import {
  getWhoamiSagaSuccess,
  getWhoamiSagaFailed,
} from '../../actions';
import {getWhoami} from '../../lib/api';

function* workerGetWhoamiSaga(token) {
  try {
    const response = yield call(getWhoami, token);
    yield put(getWhoamiSagaSuccess(response));
  } catch (err) {
    yield put(getWhoamiSagaFailed(err));
  }
}

export default function* watchGetWhoamiSaga() {
  yield takeLatest(GET_WHOAMI_SAGA, workerGetWhoamiSaga);
}
