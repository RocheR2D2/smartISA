import React from "react";
import { ApolloConsumer } from "react-apollo";
import withStyles from "@material-ui/core/styles/withStyles";
import ExitToApp from "@material-ui/icons/ExitToApp";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

const Signout = ({ classes }) => {
  const handleSignout = client => {
    localStorage.removeItem("authToken");
    client.writeData({ data: { isLoggedIn: false } });
    console.log("Signed out user", client);
  };

  return (
    <ApolloConsumer>
      {client => (
        <Button onClick={() => handleSignout(client)}>
          <Typography
            variant="h6"
            className={classes.accountIcon} 
          >
            Signout
          </Typography>
          <ExitToApp className={classes.buttonIcon} />
        </Button>
      )}
    </ApolloConsumer>
  );
};
const styles = {
  root: {
    cursor: "pointer",
    display: "flex"
  },
  buttonIcon: {
    marginLeft: "5px",    
  },
  accountIcon: {
    fontSize: 30,
    color: "white"
  }
};

export default withStyles(styles)(Signout);
