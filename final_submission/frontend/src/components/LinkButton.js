import React from 'react';
import {Button} from 'grommet';

export default (props) => {
  return (
    <Button
      label={props.label}
      onClick={() => {props.history.push(props.whereto)}}
      margin={{bottom: '0.5em'}}
    />
  );
};
