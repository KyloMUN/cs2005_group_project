import React, {Component} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import {
  Heading,
  Box,
  Button,
  TextInput,
  RadioButtonGroup,
} from 'grommet';

import {
  getWhoamiSaga,
  createNewUserSaga,
} from '../../actions';
import {isEmpty} from '../../utils';
import LoadingSpinner from '../../components/LoadingSpinner';
import LinkButton from '../../components/LinkButton';

class Account extends Component {
  state = {
    newUsername: '',
    newPassword: '',
    newRole: '',
  }

  componentDidMount() {
    if (!this.props.loggedIn) {
      this.props.history.push('/login');
    }
    else {
      this.props.getWhoamiSaga(this.props.token);
    }
  }

  studentView = () => {
    const {
      username,
      realname,
      classes,
    } = this.props.whoami;

    return (
      <>
        <Heading level='4'>Hello {realname ? realname : username}, here are your classes:</Heading>
        {
          Object.keys(classes).map((key) => (
            <LinkButton
              label={classes[key].classname}
              key={key}
              whereto={`/view/class/${classes[key].id}`}
              history={this.props.history}
            />
          ))
        }
        <LinkButton
          label='Change password'
          whereto='/changepassword'
          history={this.props.history}
        />
      </>
    );
  };

  newUsernameChange = (e) => {
    this.setState({newUsername: e.target.value});
  };
  newPasswordChange = (e) => {
    this.setState({newPassword: e.target.value});
  };
  newRoleChange = (e) => {
    this.setState({newRole: e.target.value});
  };

  handleCreateNewUser = () => {
    const {
      newUsername,
      newPassword,
      newRole,
    } = this.state;

    this.props.createNewUserSaga(
      this.props.token, newUsername, newPassword, newRole,
    );
  };

  teacherView = () => {
    return (
      <>
        <LinkButton
          label='Create new quiz'
          whereto='/new/quiz'
          history={this.props.history}
        />
        <Box
          pad='large'
          align='center'
          background={{color: 'light-1', opacity: 'strong'}}
          round
          gap='small'
        >
          <Heading level='4' margin='none'>Create new user</Heading>
          <TextInput
            type='password'
            placeholder='Username'
            value={this.state.newUsername}
            onChange={this.newUsernameChange}
          />
          <TextInput
            type='password'
            placeholder='Password'
            value={this.state.newPassword}
            onChange={this.newPasswordChange}
          />
          <RadioButtonGroup
            options={['Student', 'Professor']}
            value={this.state.newRole}
            onChange={this.newRoleChange}
          />
          <Button
            label='Create'
            onClick={this.handleCreateNewUser}
          />
        </Box>
      </>
    )
  }

  render() {
    const {whoami} = this.props;
    if (isEmpty(whoami)) {
      return <LoadingSpinner />;
    }

    if (whoami.roles.includes('professor')) {
      return this.teacherView();
    }

    return this.studentView();
  }
}

const mapStateToProps = (state) => ({
  token: state.login.token,
  loggedIn: state.login.loggedIn,
  whoami: state.whoami,
});

const mapDispatchToProps = (dispatch) => ({
  getWhoamiSaga: (token) => dispatch(getWhoamiSaga(token)),
  createNewUserSaga: (token, username, password, role) => dispatch(
    createNewUserSaga(token, username, password, role)
  ),
});

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Account));
