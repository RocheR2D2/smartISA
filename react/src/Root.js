import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import withRoot from "./withRoot";
import {Query} from 'react-apollo';
import {gql} from 'apollo-boost';
import App from "./pages/App";
import Profile from "./pages/Profile";
import Header from './components/Shared/Header';
import Loading from "./components/Shared/Loading";
import Error from "./components/Shared/Error";

export const UserContext = React.createContext();

const Root = () => (
    <Query query={ LOGGEDMEMBER_QUERY } fetchPolicy="cache-and-network">
        {({ data, loading, error }) => {
            if(loading) return <Loading />
            if(error) return <Error />
            const currentUser = data.member;

            return (
                <Router>
                    <UserContext.Provider value={currentUser}>
                        <Header currentUser={currentUser}/>
                        <Switch>
                            <Route exact path="/" component={App}/>
                            <Route path="/profile/:id" component={Profile}/>
                        </Switch>
                    </UserContext.Provider>
                </Router>
            )
        }}
    </Query>
)
export const LOGGEDMEMBER_QUERY = gql`
  {
    member {
      id
      username
      email
    }
  }
`;

export default withRoot(Root);
