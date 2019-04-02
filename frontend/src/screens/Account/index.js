import React, {Component} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import {Markdown} from 'grommet';

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

  componentWillReceiveProps(newProps) {
  }

  studentView = () => {
    return (
      <p>Student view</p>
    );
    /*return (
      <Button
        label="Homepage"
        onClick={() => {this.props.history.push('/')}}
        {...buttonStyle}
      />
    )*/
  }

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
