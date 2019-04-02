import {combineReducers} from 'redux';

import loginReducer from './login';
import whoamiReducer from './whoami';

export default combineReducers({
  login: loginReducer,
  whoami: whoamiReducer,
});
