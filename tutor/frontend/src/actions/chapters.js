import axios from "axios";
import { GET_CHAPTERS, ADD_CHAPTER, DELETE_CHAPTER } from "./types";

// Get Grades
export const getChapters = () => dispatch => {
    axios.get('/courses/chapters/')
        .then(res => {
            dispatch({
                type: GET_CHAPTERS,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

// Delete Grade
export const deleteChapter = (id) => dispatch => {
    axios.delete(`/courses/chapters/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_CHAPTER,
                payload: id
            });
        }).catch(err => console.log(err));
};

// Add Grade
export const addChapter = (chapter) => dispatch => {
    axios.post('/courses/chapters/', chapter)
        .then(res => {
            dispatch({
                type: ADD_CHAPTER,
                payload: res.data
            });
        }).catch(err => console.log(err));
};
