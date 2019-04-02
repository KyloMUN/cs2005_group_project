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

import store, {history} from './store';
import Home from './screens/Home';
import Login from './screens/Login';

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
                <Heading level='3' margin='none'>Quiz App</Heading>
                <Button
                  icon={<Menu />}
                  onClick={this.toggleAppBar}
                />
              </AppBar>
              <Box direction='row' flex overflow={{horizontal: 'hidden'}}>
                <Box flex align='center' justify='center'>
                  <Route path='/' exact component={Home} />
                  <Route path='/login' component={Login} />
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
          </ConnectedRouter>
        </Provider>
      </Grommet>
    );
  }
}
