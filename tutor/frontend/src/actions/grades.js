import axios from "axios";
import { GET_GRADES } from "./types";

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