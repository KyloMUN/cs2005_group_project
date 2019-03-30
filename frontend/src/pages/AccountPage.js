import React, {Component} from 'react';

export default class AccountPage extends Component {
  componentWillMount() {
    if (this.props.token === null) {
      //history.push('/login');
    }
  }

  async componentDidMount() {
    //const response = await api.get('whoami', {token: this.props.token});
    //console.log(response);
  }

  render() {
    return (
      <>
        Account
      </>
    );
  }
}