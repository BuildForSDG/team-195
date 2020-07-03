import React, { Component } from 'react';
import { connect } from "react-redux";
import PropTypes from 'prop-types';
import { addGrade } from "../../actions/grades";


class Form extends Component {
    constructor(props) {
        super(props)
        this.state = {
            grade_name: ""
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    };

    static propTypes() {
        addGrade: PropTypes.func.isRequired;
    };

    handleChange(e) {
        this.setState({ [e.target.name]: e.target.value });
    }

    handleSubmit(event) {
        event.preventDefault();
        const { grade_name } = this.state;
        const grade = { grade_name };
        this.props.addGrade(grade);
    }


    render() {
        const { grade_name } = this.state;
        return (
            <div className="card card-body mt-4 mb-4">
                <h1>Add Grade</h1>
                <form onSubmit={this.handleSubmit}>
                    <div className="form-group">
                        <label>Name</label>
                        <input
                            className="form-control"
                            type="text"
                            name="grade_name"
                            onChange={this.handleChange}
                            value={grade_name}
                        />
                    </div>
                    <div className="form-group">
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>

        )
    }
}

export default connect(null, { addGrade })(Form);
