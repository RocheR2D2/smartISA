import React from "react";
import withRoot from "./withRoot";
import {Query} from 'react-apollo';
import {gql} from 'apollo-boost';


const Root = () => (
    <Query query={GET_DOCX_QUERY}>
        {({ data, loading, error }) => {
            if(loading) return <div>Loading</div>
            if(error) return <div>Error</div>

            return <div>{ JSON.stringify(data) }</div>
        }}
    </Query>
)
const GET_DOCX_QUERY = gql`
{
    docxs {
        id
        title
        description
        url
    }
}`;

export default withRoot(Root);
