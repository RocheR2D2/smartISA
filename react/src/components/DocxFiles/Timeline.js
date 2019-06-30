import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";


const Timeline = ({ classes }) => {
    return <div>Timeline</div>;
  };


  



const styles = theme => ({
container: {
    display: "flex",
    flexWrap: "wrap"
},
dialog: {
    margin: "0 auto",
    maxWidth: 550
},
textField: {
    margin: theme.spacing.unit
},
cancel: {
    color: "red"
},
save: {
    color: "green"
},
button: {
    margin: theme.spacing.unit * 2
},
icon: {
    marginLeft: theme.spacing.unit
},
input: {
    display: "none"
},
fab: {
    position: "fixed",
    bottom: theme.spacing.unit * 2,
    right: theme.spacing.unit * 2,
    zIndex: "200"
}
});

export default withStyles(styles)(Timeline);