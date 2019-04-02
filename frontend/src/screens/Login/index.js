import React, {Component} from 'react';
import {connect} from 'react-redux';
import {
  Box,
  Button,
  TextInput,
} from 'grommet';

import {loginSaga} from '../../actions';

class Login extends Component {
  state = {
    username: '',
    password: '',
  }

  handleUsernameChange = (e) => {
    this.setState({username: e.target.value});
  };
  handlePasswordChange = (e) => {
    this.setState({password: e.target.value});
  };

  handleLogin = () => {
    console.log('skaljfhasldkfhasdlkjfh');
    console.log(this.props.loginSaga(this.state.username, this.state.password));
    console.log('skaljfhasldkfhasdlkjfh');
  };

  render() {
    console.log(this.state);
    return (
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
    );
  }
}

const mapStateToProps = (state) => ({});

const mapDispatchToProps = (dispatch) => ({
  loginSaga: (username, password) => dispatch(loginSaga(username, password))
});

export default connect(mapStateToProps, mapDispatchToProps)(Login);
