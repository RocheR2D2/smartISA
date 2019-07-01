import React, { Component } from "react";

import Checkbox from '../components/DocxFiles/Checkbox'
import Upload from '../components/DocxFiles/Upload'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chkArr: {},
    };
    this.addItems = this.addItems.bind(this);

  }
  addItems(new_labels) {
    console.debug(new_labels);
    var { chkArr } = this.state;
    for (var key in new_labels){
	var new_label = new_labels[key];
    	chkArr[new_label] = true;
    }
    console.debug(JSON.stringify(chkArr, null, 4));
    this.setState({
      chkArr: chkArr
    })
  }
  render() {
  return (
    <div style={divStyles}>
      <Upload addItems={this.addItems} />
      <Checkbox itemsToDisplay={this.state.chkArr} />
    </div>
  );
  }
};

const divStyles = {
    margin: "0 auto",
    maxWidth: 960,
};

export default App

