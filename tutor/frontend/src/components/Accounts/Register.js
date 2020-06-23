import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class Register extends Component {
    constructor(props) {
        super(props)
        this.state = {
            firstname: "",
            middlename: "",
            lastname: "",
            email: "",
            password: "",
            password2: ""
        }
        this.onChange = this.onChange.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    };

    onChange(e) { this.setState({ [e.target.name]: e.target.value }); }
    onSubmit(e) {
        e.preventDefaut();
        console.log("submit")
    };
    render() {
        const { firstname, middlename, lastname, email, password, password2 } = this.state;
        return (
            <form onSubmit={this.onSubmit}>
                <h3>Register</h3>

                <div className="form-group">
                    <label>First name</label>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="First name"
                        name="firstname"
                        onChange={this.onChange}
                        value={firstname}
                    />
                </div>

                <div className="form-group">
                    <label>Middle name</label>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Middle name"
                        name="middlename"
                        onChange={this.onChange}
                        value={middlename}
                    />
                </div>

                <div className="form-group">
                    <label>Last name</label>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Last name"
                        name="lastname"
                        onChange={this.onChange}
                        value={lastname}
                    />
                </div>

                <div className="form-group">
                    <label>Email address</label>
                    <input
                        type="email"
                        className="form-control"
                        placeholder="Enter email"
                        name="email"
                        onChange={this.onChange}
                        value={email}
                    />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input
                        type="password"
                        className="form-control"
                        placeholder="Enter password"
                        name="password"
                        onChange={this.onChange}
                        value={password}
                    />
                </div>

                <div className="form-group">
                    <label>Confirm password</label>
                    <input
                        type="password"
                        className="form-control"
                        placeholder="Confirm password"
                        name="password2"
                        onChange={this.onChange}
                        value={password2}
                    />
                </div>

                <button type="submit" className="btn btn-primary btn-block">Register</button>
                <p>
                    Already have an account?
                    <Link to="/login"
                        className="nav-link">Login</Link>
                </p>
            </form>
        );
    }
}