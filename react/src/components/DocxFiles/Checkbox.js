import React from "react";
import "./Checkbox.css";
const { Component } = React;

class Checkbox extends React.Component {
  constructor(props) {
    super(props);
  }

  // handleClick was inlined

  render() {
    return (
      <div>
        <form>
          {Object.keys(this.props.itemsToDisplay).map((key) => (
            <div key={key}>
              <input
                name={key}
                id={`checkbox-${key}`}
                type="checkbox"
                checked={this.props.itemsToDisplay[key]}
                onChange={() => this.setState({ [key]: !this.props.itemsToDisplay[key] })}
              />

              <span className="padding">
                {/* Don't need a `key` prop here */}
                <label htmlFor={`checkbox-${key}`}>
                  {key}
                </label>
              </span>
            </div>
          ))}
        </form>
        <div className="center">
          <h2>Current State: </h2>
          <ul>
            {Object.keys(this.props.itemsToDisplay).map(key => (
              <li key={key}>{`${key}: ${this.props.itemsToDisplay[key]}`}</li>
            ))}
          </ul>
        </div>
      </div>
    );
  }
}

/*
const Checkbox = (props) => {
  return (
    <span style={{ 'marginLeft': '32px' }}>
      <input
        type="checkbox"
        checked={props.checked}
        onChange={props.onInputChange}
        id={props.id} />
      <label
        className="checkbox"
        htmlFor={props.id}>
        {props.label}
      </label>
    </span>
  )
}

class CheckboxWrap extends Component {
  constructor(props) {
    super(props);
    this.checkAll = this.checkAll.bind(this)
    this.checkInvert = this.checkInvert.bind(this)
    this.checkNone = this.checkNone.bind(this)
  }
  onInputChange(index) {
    var { chkArr } = this.props.itemsToDisplay;
    chkArr[index].checked = !chkArr[index].checked;
    //this.setState({
    //  chkArr: chkArr
    //})
  }
  
  checkAll(e) {
    e.preventDefault();

    var { chkArr } = this.props.itemsToDisplay;
    var targetArr = chkArr.map((item) => {
      return {
        label: item.label,
        checked: true
      }
    })
    //this.setState({
    //  chkArr: targetArr
    //});
  }
  checkInvert(e) {
    e.preventDefault();

    var { chkArr } = this.props.itemsToDisplay;
    var targetArr = chkArr.map((item) => {
      return {
        label: item.label,
        checked: !item.checked
      }
    })
	  
    this.setState({
      chkArr: targetArr
    })
  }
  checkNone(e) {
    e.preventDefault();

    var { chkArr } = this.props.itemsToDisplay;
    var targetArr = chkArr.map((item) => {
      return {
        label: item.label,
        checked: false
      }
    })
	
    this.setState({
      chkArr: targetArr
    })
   
  }
  render() {
    var checkArr = []
    {this.props.itemsToDisplay}.map((item) => {
      if (item.checked === true) {
        checkArr.push(item.label)
      }
    })
    var checkFruitLabel = checkArr.length > 1 ? checkArr.join('、') : checkArr.join('')
    return (
      <div className="container center-align">
        <div >
          {
            chkArr.map((item, index) => {
              return (
                <Checkbox
                  id={'checkbox' + index}
                  label={item.label}
                  checked={item.checked}
                  onInputChange={this.onInputChange.bind(this, index)}
                />
              )
            })
          }
        </div>
        <div className="divider"></div>
        <div className="btn-row">
          <a
            className="waves-effect waves-light btn red tooltipped"
            onClick={this.checkAll.bind(this)}
            data-position="left"
            data-delay="50"
            data-tooltip="redcheck">
            <i className="fa fa-fw fa-check" />
          </a>
          <a
            className="waves-effect waves-light btn green tooltipped"
            onClick={this.checkInvert.bind(this)} data-position="top"
            data-delay="50"
            data-tooltip="greencheck">
            <i className="fa fa-fw fa-hourglass-2" />
          </a>
          <a
            className="waves-effect waves-light btn blue tooltipped"
            onClick={this.checkNone.bind(this)}
            data-position="right"
            data-delay="50"
            data-tooltip="bluecheck">
            <i className="fa fa-fw fa-times" />
          </a>
        </div>
        <h6>
          {checkFruitLabel === '' ? 'You have to choose at least one' : 'Current selection：' + checkFruitLabel}
        </h6>
      </div>
    )
  }
}
*/
export default Checkbox;
