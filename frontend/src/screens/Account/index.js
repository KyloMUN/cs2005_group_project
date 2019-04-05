import React, {Component} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import {Heading} from 'grommet';

import {getWhoamiSaga} from '../../actions';
import {isEmpty} from '../../utils';
import LoadingSpinner from '../../components/LoadingSpinner';
import LinkButton from '../../components/LinkButton';

class Account extends Component {
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
          label="Change password"
          whereto="/changepassword"
          history={this.props.history}
        />
      </>
    );
  };

  teacherView = () => {
    return (
      <LinkButton
        label="Create new quiz"
        whereto="/new/quiz"
        history={this.props.history}
      />
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
  getWhoamiSaga: (token) => dispatch(getWhoamiSaga(token))
});

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Account));
