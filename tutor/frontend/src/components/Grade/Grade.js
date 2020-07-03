import React, { Component, Fragment } from 'react';
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getGrades, deleteGrade } from "../../actions/grades";


class Grades extends Component {
    static propTypes() {
        grades: PropTypes.array.isRequired;
        getGrades: PropTypes.func.isRequired;
        deleteGrade: PropTypes.func.isRequired;
    };

    componentDidMount() {
        this.props.getGrades();
    }

    render() {
        return (
            <Fragment>
                <h1>Grades</h1>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Name</th>
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.grades.map(grade => (
                            <tr key={grade.id}>
                                <td>{grade.id}</td>
                                <td>{grade.grade_name}</td>
                                <td><button
                                    onClick={this.props.deleteGrade.bind(this, grade.id)}
                                    className="btn btn-danger btn-sm">
                                    {""}
                                        Delete
                                    </button>
                                </td>
                            </tr>))}

                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    grades: state.grades.grades
})

export default connect(mapStateToProps, { getGrades, deleteGrade })(Grades);
