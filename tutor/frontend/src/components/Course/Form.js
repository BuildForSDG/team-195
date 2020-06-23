import React, { Component } from 'react';
import { connect } from "react-redux";
import PropTypes from 'prop-types';
import GradesDropDown from "../Grade/Grade";
import { addCourse } from "../../actions/courses";


class Form extends Component {
    constructor(props) {
        super(props)
        this.state = {
            course_name: "",
            grade: "",
            description: "",
            tutor: ""
        }
        this.handleChange = this.handleChange.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    };

    static propTypes() {
        addCourse: PropTypes.func.isRequired;
    };

    handleChange(e) { this.setState({ [e.target.name]: e.target.value }); }
    onSubmit(e) {
        e.preventDefaut();
        const { course_name, grade, description, tutor } = this.state;
        const course = { course_name, grade, description, tutor };
        this.props.addCourse(course);
    };


    render() {
        const { course_name, grade, description, tutor } = this.state;
        return (
            <div className="card card-body mt-4 mb-4">
                <h1>Add Course</h1>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Name</label>
                        <input
                            className="form-control"
                            type="text"
                            name="course_name"
                            onChange={this.handleChange}
                            value={course_name}
                        />
                    </div>
                    <div className="form-group">
                        <label>Grade</label>
                        <input
                            className="form-control"
                            type="text"
                            name="grade"
                            onChange={this.handleChange}
                            value={grade}
                        />
                    </div>
                    <div className="form-group">
                        <label>Description</label>
                        <input
                            className="form-control"
                            type="text"
                            name="description"
                            onChange={this.handleChange}
                            value={description}
                        />
                    </div>
                    <div className="form-group">
                        <label>Tutor</label>
                        <input
                            className="form-control"
                            type="text"
                            name="tutor"
                            onChange={this.handleChange}
                            value={tutor}
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

export default connect(null, { addCourse })(Form);
