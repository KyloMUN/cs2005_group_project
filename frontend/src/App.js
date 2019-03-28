import React, {Component} from 'react';
import {
  Box,
  Heading,
  Grommet,
  Button,
  TextInput,
} from 'grommet';
import {
  Menu,
} from 'grommet-icons';
import {
  Router,
  Route,
} from 'react-router-dom';
import {createBrowserHistory} from 'history';

import api from './api';

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

class HomePage extends Component {
  render() {
    return (
      <>
        Homepage
      </>
    );
  }
}

class LogoutPage extends Component {
  componentWillMount() {
    this.props.setToken(null);
    history.push('/login');
  }

  render() {
    return (
      <>
        Logout
      </>
    );
  }
}

class AccountPage extends Component {
  componentWillMount() {
    if (this.props.token === null) {
      history.push('/login');
    }
  }

  async componentDidMount() {
    const response = await api.get('whoami');

    console.log(response);
  }

  render() {
    return (
      <>
        Account
      </>
    );
  }
}

class LoginPage extends Component {
  state = {
    username: '',
    password: '',
  }

  componentWillMount() {
    if (this.props.token !== null) {
      history.push('/account');
    }
  }

  handleUsernameChange = (e) => {
    this.setState({username: e.target.value});
  };
  handlePasswordChange = (e) => {
    this.setState({password: e.target.value});
  };
  handleLogin = async () => {
    const {username, password} = this.state;
    const response = await api.post('login', {username, password});

    if (response.access_token !== undefined) {
      this.props.setToken(response.access_token);
      history.push('/account');
    }
  };

  render() {
    return (
      <>
        <Box
          pad='large'
          align='center'
          background={{ color: 'light-1', opacity: 'strong' }}
          round
          gap='small'
        >
          <TextInput
            placeholder='Username'
            value={this.state.username}
            onChange={this.handleUsernameChange}
          />
          <TextInput
            type='password'
            placeholder='Password'
            value={this.state.password}
            onChange={this.handlePasswordChange}
          />
          <Button
            label="Login"
            onClick={this.handleLogin}
          />
        </Box>
      </>
    );
  }
}

class App extends Component {
  state = {
    showSidebar: false,
    token: null,
  }

  setToken = (token) => {
    this.setState({token});
  }

  wrappedLoginPage = () => {
    return <LoginPage token={this.state.token} setToken={this.setToken} />
  };

  wrappedLogoutPage = () => {
    return <LogoutPage setToken={this.setToken} />
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
                <Route path='/login' component={this.wrappedLoginPage} />
                <Route path='/logout' component={this.wrappedLogoutPage} />
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
