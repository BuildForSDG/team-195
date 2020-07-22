import React, { Component, Fragment } from 'react';
import ReactDom from "react-dom";
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom";

import Header from "./Layout/Header";
import Dashboard from "./Course/Dashboard";
import GradeDashboard from "./Grade/GradeDashboard";
import ChapterDashboard from "./Chapter/ChapterDashboard";

import Register from "./Accounts/Register";
import Login from "./Accounts/Login";
import PrivateRoute from "./common/PrivateRoute";

import { Provider } from "react-redux";
import store from "../store";

const App = () => {

    return (
        <Provider store={store}>
            <Router>
                <Fragment>
                    <Header />
                    <div className="container">
                        <Switch>
                            <Route exact path="/" component={ChapterDashboard} />
                            <Route exact path="/register" component={Register} />
                            <Route exact path="/login" component={Login} />
                        </Switch>
                    </div>
                </Fragment>
            </Router>
        </Provider>
    );
};

ReactDom.render(<App />, document.getElementById("app"));
