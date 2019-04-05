import React, {Component} from 'react';
import {PulseLoader} from 'react-spinners';

import {theme} from '../App';

export default class LoadingSpinner extends Component {
  constructor(props) {
    super(props);
    this.state = {
    loading: true
    }
  }
  render() {
    return (
      <PulseLoader
        sizeUnit='em'
        size={1}
        color={theme.global.colors.brand}
        loading={true}
      />
    );
  }
}