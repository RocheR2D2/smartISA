import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
//import List from '@material-ui/core/List';
//import ListItem from '@material-ui/core/ListItem';
//import ListItemText from '@material-ui/core/ListItemText';
//import TypoGraphy from '@material-ui/core/Typography';
//import ListItemIcon from '@material-ui/core/ListItemIcon';
//import { Home, Book, AccountBox } from '@material-ui/icons';
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import FaceIcon from "@material-ui/icons/FaceTwoTone";
import Typography from "@material-ui/core/Typography";
import { Link } from "react-router-dom";
import Signout from "../Auth/Signout";

const Header = ({ classes,  currentUser }) => {
  return (
    <AppBar position="static" className={classes.root}>
    <Toolbar>
      {/* Title / Logo */}
      <Link to="/" className={classes.grow}>
        <Typography variant="h6" noWrap className={classes.faceIcon}>
          SmartISA
        </Typography>
      </Link>

      {/* Auth User Info */}
      {currentUser && (
        <Link to={`/profile/${currentUser.id}`} className={classes.grow}>
          <FaceIcon className={classes.faceIcon} />
          <Typography variant="h6" className={classes.username} noWrap>
            {currentUser.username}
          </Typography>
        </Link>
      )}

      {/* Signout Button */}
      <Signout />
    </Toolbar>
  </AppBar>
  )
};

const styles = theme => ({
  root: {
    flexGrow: 1,
    margin: 0,
    padding: 0
  },
  grow: {
    flexGrow: 1,
    display: "flex",
    alignItems: "center",
    textDecoration: "none"
  },
  logo: {
    marginRight: theme.spacing.unit,
    fontSize: 45
  },
  faceIcon: {
    marginRight: theme.spacing.unit,
    fontSize: 30,
    color: "white"
  },
  username: {
    color: "white",
    fontSize: 30
  }
});

export default withStyles(styles)(Header);
