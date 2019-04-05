import {all, fork} from 'redux-saga/effects';

import watchLoginSaga from './watchers/login';
import watchGetWhoamiSaga from './watchers/whoami';

export default function* root() {
  yield all([
    fork(watchLoginSaga),
    fork(watchGetWhoamiSaga),
  ]);
}
