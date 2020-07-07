import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class Register extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: "",
            password2: "",
            is_staff: ""
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
        const { username, password, password2, is_staff } = this.state;
        return (
            <div className="col-md-6 m-auto">
                <div className="card card-body mt-5">
                    <h2 className="text-center">Register</h2>
                    <form onSubmit={this.onSubmit}>

                        <div className="form-group">
                            <label>Username</label>
                            <input
                                type="text"
                                className="form-control"
                                placeholder="Username"
                                name="username"
                                onChange={this.onChange}
                                value={username}
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

                        <div className="form-group">
                            <label>Is Staff</label>
                            <input
                                type="is_staff"
                                className="form-control"
                                name="is_staff"
                                onChange={this.onChange}
                                value={is_staff}
                            />
                        </div>

                        <button type="submit" className="btn btn-primary btn-block">Register</button>
                        <p>
                            Already have an account?
                    <Link to="/login"
                                className="nav-link">Login</Link>
                        </p>
                    </form>
                </div>
            </div>
        );
    }
}