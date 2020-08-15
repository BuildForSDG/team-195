import React, { Component, Fragment } from 'react';
import { connect } from "react-redux";
import PropTypes from "prop-types";
import ReactPlayer from "react-player";
import { getChapters, deleteChapter } from "../../actions/chapters.js";
import get from "lodash/get";


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
        const { chapters } = this.props;
        const ChapterList = () => (
            <ul>
                {chapters.map(item => (
                    <li key={item.id}>
                        <div>{item.chapter_name}</div>
                        <div><ReactPlayer
                            className='react-player'
                            url={item.content.url}
                            width='100%'
                            height='100%'
                        /></div>
                        <div>{item.course}</div>
                    </li>
                ))}
            </ul>
        );

        return (
            <Fragment>
                <h1>Chapters</h1>
                <ChapterList chapters={chapters} />

            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    chapters: get(state.chapters, "chapters")
})

export default connect(mapStateToProps, { getChapters, deleteChapter })(Chapters);
