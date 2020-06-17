import { GET_COURSES, DELETE_COURSE } from "../actions/types";

const initialState = {
    courses: []
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_COURSES:
            return {
                ...state,
                courses: action.payload
            };
        case DELETE_COURSE:
            return {
                ...state,
                courses: state.courses.filter(course => course.id !==
                    action.payload)
            };
        default:
            return state;

    }
}