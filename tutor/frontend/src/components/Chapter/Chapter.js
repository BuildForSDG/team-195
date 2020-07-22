import React, { Component, Fragment } from 'react';
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getChapters, deleteChapter } from "../../actions/chapters.js";


class Chapters extends Component {
    static propTypes() {
        chapters: PropTypes.array.isRequired;
        getChapters: PropTypes.func.isRequired;
        deleteChapter: PropTypes.func.isRequired;
    };

    componentDidMount() {
        this.props.getChapters();
    }

    render() {
        return (
            <Fragment>
                <h1>Chapters</h1>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Content</th>
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.chapters.map(chapter => (
                            <tr key={chapter.id}>
                                <td>{chapter.chapter_name}</td>
                                <td>{chapter.content}</td>
                                <td><button onClick=
                                    {this.props.deleteChapter.bind(this, chapter.id)}
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
    chapters: state.chapters.chapters
})

export default connect(mapStateToProps, { getChapters, deleteChapter })(Chapters);
