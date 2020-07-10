import axios from "axios";
import { GET_GRADES, ADD_GRADE, DELETE_GRADE } from "./types";

// Get Grades
export const getGrades = () => dispatch => {
    axios.get('/courses/grades/')
        .then(res => {
            dispatch({
                type: GET_GRADES,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

// Delete Grade
export const deleteGrade = (id) => dispatch => {
    axios.delete(`/courses/grades/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_GRADE,
                payload: id
            });
        }).catch(err => console.log(err));
};

// Add Grade
export const addGrade = (grade) => dispatch => {
    axios.post('/courses/grades/', grade)
        .then(res => {
            dispatch({
                type: ADD_GRADE,
                payload: res.data
            });
        }).catch(err => console.log(err));
};
