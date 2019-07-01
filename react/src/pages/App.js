import React, { Component } from "react";

import Checkbox from '../components/DocxFiles/Checkbox'
import Upload from '../components/DocxFiles/Upload'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chkArr: [
	//{ label: '梨', checked: false },
      ],
      checkedLabel: ''
    };
  }
  render() {
  return (
    <div style={divStyles}>
      <Upload />
      <Checkbox />
    </div>
  );
  }
};

const divStyles = {
    margin: "0 auto",
    maxWidth: 960,
};

export default App

