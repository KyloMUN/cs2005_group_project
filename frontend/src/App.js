import React, {Component} from 'react';
import {
  Box,
  Heading,
  Grommet,
  Button,
} from 'grommet';
import {
  Menu,
} from 'grommet-icons';
import {
  Router,
  Route,
} from 'react-router-dom';
import {createBrowserHistory} from 'history';
import {Provider} from 'react-redux';

import {
  AccountPage,
  HomePage,
  LoginPage,
  LogoutPage,
} from './pages';

const history = createBrowserHistory();

history.push('/login');

const theme = {
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

class App extends Component {
  state = {
    showSidebar: false,
  }

  render() {
    return (
      <Grommet theme={theme} full>
        <Router
          history={history}
        >
          <Box fill>
            <AppBar>
              <Heading level='3' margin='none'>Quiz App</Heading>
              <Button
                icon={<Menu />}
                onClick={() => this.setState((prevState) => ({showSidebar: !prevState.showSidebar}))}
              />
            </AppBar>
            <Box direction='row' flex overflow={{horizontal: 'hidden'}}>
              <Box flex align='center' justify='center'>
                <Route path='/' exact component={HomePage} />
                <Route path='/login' component={LoginPage} />
                <Route path='/logout' component={LogoutPage} />
                <Route path='/account' component={AccountPage} />
              </Box>
              {this.state.showSidebar && (
                <Box
                  width='medium'
                  background='light-2'
                  elevation='small'
                  align='center'
                  justify='center'
                  gap='small'
                >
                  <Button
                    label="Homepage"
                    onClick={() => {history.push('/')}}
                  />
                  {
                    this.state.token && (
                      <Button
                        label="Account"
                        onClick={() => {history.push('/account')}}
                      />
                    )
                  }
                  {
                    this.state.token && (
                      <Button
                        label="Logout"
                        onClick={() => {history.push('/logout')}}
                      />
                    )
                  }
                  {
                    !this.state.token && (
                      <Button
                        label="Login"
                        onClick={() => {history.push('/login')}}
                      />
                    )
                  }
                </Box>
              )}
            </Box>
          </Box>
        </Router>
      </Grommet>
    );
  }
}

export default App;
