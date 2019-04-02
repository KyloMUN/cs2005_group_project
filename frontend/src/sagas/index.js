import {all, fork} from 'redux-saga/effects';

import watchLoginSaga from './watchers/login';

export default function* root() {
  yield all([
    fork(watchLoginSaga),
  ]);
}
