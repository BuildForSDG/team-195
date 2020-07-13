import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from 'prop-types';
import { register } from "../../actions/auth"


class Register extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: "",
            password2: "",
            is_staff: false
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    };
    static propTypes() {
        register: PropTypes.func.isRequired;
        isAuthenticated: PropTypes.bool;
    }

    handleChange(e) { this.setState({ [e.target.name]: e.target.value }); }
    handleSubmit(e) {
        event.preventDefault();
        const { password, password2 } = this.state;
        if (password != password2) {
            alert("Passwords do not match")
        }
        else {
            const { username, password, password2, is_staff } = this.state;
            const newUser = {
                username, password, password2, is_staff
            }
            this.props.register(newUser);
        }

    };
    render() {
        const { username, password, password2, is_staff } = this.state;
        return (
            <div className="col-md-6 m-auto">
                <div className="card card-body mt-5">
                    <h2 className="text-center">Register</h2>
                    <form onSubmit={this.handleSubmit}>

                        <div className="form-group">
                            <label>Username</label>
                            <input
                                type="text"
                                className="form-control"
                                placeholder="Username"
                                name="username"
                                onChange={this.handleChange}
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
                                onChange={this.handleChange}
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
                                onChange={this.handleChange}
                                value={password2}
                            />
                        </div>

                        <div className="form-group">
                            <label>Is Staff?</label>
                            <input
                                type="checkbox"
                                className="form-control"
                                name="is_staff"
                                value={is_staff}
                                onChange={(e) => this.setState({ is_staff: !is_staff.value })}
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

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { register })(Register);
