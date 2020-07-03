import axios from "axios";
import { GET_COURSES, DELETE_COURSE, ADD_COURSE } from "./types";
import courses from "../reducers/courses";

// Get Courses
export const getCourses = () => dispatch => {
    axios.get('/courses/')
        .then(res => {
            dispatch({
                type: GET_COURSES,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

// Delete Course
export const deleteCourse = (id) => dispatch => {
    axios.delete('/courses/${id}/')
        .then(res => {
            dispatch({
                type: DELETE_COURSE,
                payload: id
            });
        }).catch(err => console.log(err));
};

// Add Course
export const addCourse = (course) => dispatch => {
    axios.post('/courses/', course)
        .then(res => {
            dispatch({
                type: ADD_COURSE,
                payload: res.data
            });
        }).catch(err => console.log(err));
};
