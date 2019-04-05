import React, {Component} from 'react';
import {connect} from 'react-redux';
import {
  Box,
  Button,
  TextInput,
} from 'grommet';

import {createQuizSaga} from '../../actions';

class CreateQuiz extends Component {
  state = {
    quizname: '',
  }

  handleSubmit = () => {
    this.props.createQuizSaga();
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
          placeholder='Quiz name'
          value={this.state.quizname}
          onChange={(e) => this.setState({quizname: e.target.quizname})}
        />
        <Button
          label='Submit'
          onClick={this.handleSubmit}
        />
      </Box>
    );
  }
}

const mapStateToProps = (state) => ({});

const mapDispatchToProps = (dispatch) => ({
  createQuizSaga: () => dispatch(createQuizSaga())
});

export default connect(mapStateToProps, mapDispatchToProps)(CreateQuiz);
