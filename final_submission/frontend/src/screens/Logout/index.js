import React, {Component} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';

import {logoutSaga} from '../../actions';

class Login extends Component {
  componentDidMount() {
    this.props.logout();
    this.props.history.push('/login');
  }

  render = () => null;
}

const mapStateToProps = (state) => ({});

const mapDispatchToProps = (dispatch) => ({
  logout: () => dispatch(logoutSaga()),
});

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Login));
