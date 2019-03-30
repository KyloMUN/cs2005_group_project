import React, {Component} from 'react';
import {
  Box,
  Button,
  TextInput,
} from 'grommet';

export default class LoginPage extends Component {
  state = {
    username: '',
    password: '',
  }

  componentWillMount() {
    /*if (this.props.token !== null) {
      history.push('/account');
    }*/
  }

  handleUsernameChange = (e) => {
    this.setState({username: e.target.value});
  };
  handlePasswordChange = (e) => {
    this.setState({password: e.target.value});
  };

  handleLogin = async () => {
    const {username, password} = this.state;
    /*const response = await api.post('login', {username, password});

    if (response.access_token !== undefined) {
      this.props.setToken(response.access_token);
      history.push('/account');
    }*/
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