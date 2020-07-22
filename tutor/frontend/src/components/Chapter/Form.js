import React, { Component } from 'react';
import { connect } from "react-redux";
import PropTypes from 'prop-types';
import CourseSelect from "./CourseSelect";
import { addChapter } from "../../actions/chapters";


class Form extends Component {
    constructor(props) {
        super(props)
        this.state = {
            chapter_name: "",
            content: ""
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    };

    static propTypes() {
        addChapter: PropTypes.func.isRequired;
    };

    handleChange(e) { this.setState({ [e.target.name]: e.target.value }); }
    handleSubmit(e) {
        e.preventDefaut();
        const { chapter_name, content } = this.state;
        const chapter = { chapter_name, content, course };
        this.props.addChapter(chapter);
    };


    render() {
        const { chapter_name, content, course } = this.state;
        return (
            <div className="card card-body mt-4 mb-4">
                <h1>Add Chapter</h1>
                <form onSubmit={this.handleSubmit}>
                    <div className="form-group">
                        <label>Name</label>
                        <input
                            className="form-control"
                            type="text"
                            name="chapter_name"
                            onChange={this.handleChange}
                            value={chapter_name}
                        />
                    </div>
                    <div className="form-group">
                        <label>Content</label>
                        <input
                            className="form-control"
                            type="file"
                            name="content"
                            onChange={this.handleChange}
                            value={content}
                        />
                    </div>
                    <div className="form-group">
                        <label>Course</label>
                        <CourseSelect />
                    </div>
                    <div className="form-group">
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>

        )
    }
}

export default connect(null, { addChapter })(Form);