import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";


import Checkbox from '../components/DocxFiles/Checkbox'
import Findresult from '../components/DocxFiles/Findresult'
import Timeline from '../components/DocxFiles/Timeline'
import Upload from '../components/DocxFiles/Upload'

const App = ({ classes }) => {
  return (
    <div className = {classes.container}>
      <Upload />
      <Timeline />
    </div>
  );
};

const styles = theme => ({
  container: {
    margin: "0 auto",
    maxWidth: 960,
    padding: theme.spacing.unit * 2
  }
});

export default withStyles(styles)(App);
