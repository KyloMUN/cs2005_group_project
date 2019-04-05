import React, {Component} from 'react';
import {connect} from 'react-redux';
import {
  Box,
  Button,
  TextInput,
} from 'grommet';

import {changePasswordSaga} from '../../actions';

class ChangePassword extends Component {
  state = {
    oldPassword: '',
    newPassword: '',
  }

  handleOldPasswordChange = (e) => {
    this.setState({oldPassword: e.target.value});
  };
  handleNewPasswordChange = (e) => {
    this.setState({newPassword: e.target.value});
  };

  handlePasswordChange = () => {
    this.props.changePasswordSaga(this.state.oldPassword, this.state.newPassword);
  };

  render() {
    return (
      <Box
        pad='large'
        align='center'
        background={{color: 'light-1', opacity: 'strong'}}
        round
        gap='small'
      >
        <TextInput
          type='password'
          placeholder='Old password'
          value={this.state.oldPassword}
          onChange={this.handleOldPasswordChange}
        />
        <TextInput
          type='password'
          placeholder='New password'
          value={this.state.newPassword}
          onChange={this.handleNewPasswordChange}
        />
        <Button
          label="Change"
          onClick={this.handlePasswordChange}
        />
      </Box>
    );
  }
}

const mapStateToProps = (state) => ({});

const mapDispatchToProps = (dispatch) => ({
  changePasswordSaga: (oldPassword, newPassword) => dispatch(changePasswordSaga(oldPassword, newPassword))
});

export default connect(mapStateToProps, mapDispatchToProps)(ChangePassword);
