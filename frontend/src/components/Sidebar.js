import React, {Component} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import {Box} from 'grommet';

import {isEmpty} from '../utils/';
import LinkButton from './LinkButton';
import LoadingSpinner from './LoadingSpinner';

class Sidebar extends Component {
  grabOptions() {
    if (!this.props.loggedIn) {
      return (
        <>
          <LinkButton
            label="Homepage"
            whereto='/'
            history={this.props.history}
          />
          <LinkButton
            label="Login"
            whereto='/login'
            history={this.props.history}
          />
        </>
      );
    }

    if (isEmpty(this.props.whoami)) {
      return <LoadingSpinner />;
    }

    return (
      <>
        <LinkButton
          label="Homepage"
          whereto='/'
          history={this.props.history}
          />
        <LinkButton
          label="Account"
          whereto='/account'
          history={this.props.history}
        />
        <LinkButton
          label="Logout"
          whereto='/logout'
          history={this.props.history}
        />
      </>
    );
  }

  render() {
    return (
      <Box
        width='medium'
        background='light-2'
        elevation='small'
        align='center'
        justify='center'
        gap='small'
      >
        {this.grabOptions()}
      </Box>
    );
  }
}

const mapStateToProps = (state) => ({
  loggedIn: state.login.loggedIn,
  whoami: state.whoami,
});

const mapDispatchToProps = () => ({});

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Sidebar));
