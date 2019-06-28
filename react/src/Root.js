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


const Root = () => (
    <Query query={GET_DOCX_QUERY}>
        {({ data, loading, error }) => {
            if(loading) return <div>Loading</div>
            if(error) return <div>Error</div>

            return (
                <Router>
                    <>
                        <Header />
                        <Switch>
                            <Route exact path="/" component={App}/>
                            <Route path="/profile/:id" component={Profile}/>
                        </Switch>
                    </>
                </Router>
            )
        }}
    </Query>
)
const GET_DOCX_QUERY = gql`
{
    docxs {
        id
        title
        description
    }
}`;

export default withRoot(Root);
