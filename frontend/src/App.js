import React, {Component} from 'react';
import {Provider} from 'react-redux';
import {ConnectedRouter} from 'connected-react-router';
import {Route} from 'react-router-dom';
import {
  Box,
  Heading,
  Grommet,
  Button,
} from 'grommet';
import {
  Menu,
} from 'grommet-icons'

import './App.css';

import Sidebar from './components/Sidebar';
import store, {history} from './store';
import Home from './screens/Home';
import Login from './screens/Login';
import Logout from './screens/Logout';
import Account from './screens/Account';
import ChangePassword from './screens/ChangePassword';
import CreateQuiz from './screens/CreateQuiz';

export const theme = {
  global: {
    colors: {
      brand: '#BF263C',
    },
    font: {
      family: 'Roboto',
      size: '14px',
      height: '20px',
    },
  },
};

const AppBar = (props) => (
  <Box
    tag='header'
    direction='row'
    align='center'
    justify='between'
    background='brand'
    pad={{left: 'medium', right: 'small', vertical: 'small'}}
    elevation='medium'
    style={{zIndex: '1'}}
    {...props}
  />
);

export default class App extends Component {
  state = {
    showSidebar: false,
  }

  toggleAppBar = () => {
    this.setState((prevState) => ({showSidebar: !prevState.showSidebar}));
  };

  render() {
    return (
      <Grommet theme={theme} full>
        <Provider store={store}>
          <ConnectedRouter history={history}>
            <Box fill>
              <AppBar>
                <Heading level='3' margin='none'>Quizm</Heading>
                <Button
                  icon={<Menu />}
                  onClick={this.toggleAppBar}
                />
              </AppBar>
              <Box direction='row' flex overflow={{horizontal: 'hidden'}}>
                <Box flex align='center' justify='center'>
                  <Route path='/' exact component={Home} />
                  <Route path='/new/quiz' component={CreateQuiz} />
                  <Route path='/login' component={Login} />
                  <Route path='/logout' component={Logout} />
                  <Route path='/account' component={Account} />
                  <Route path='/changepassword' component={ChangePassword} />
                </Box>
                {this.state.showSidebar && <Sidebar />}
              </Box>
            </Box>
          </ConnectedRouter>
        </Provider>
      </Grommet>
    );
  }
}
