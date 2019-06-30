import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import Typography from "@material-ui/core/Typography";

const Upload = ({ classes }) => {
    return (
        <div className={classes.root}>
            <ExpansionPanel>
                <ExpansionPanelSummary>this is a title</ExpansionPanelSummary>
                <ExpansionPanelDetails className={classes.details}>
                <Typography>line 1</Typography>
                <Typography>line 2</Typography>
                <Typography>line 3</Typography>
                </ExpansionPanelDetails>
            </ExpansionPanel>
        </div>
    );
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

export default withStyles(styles)(Upload);