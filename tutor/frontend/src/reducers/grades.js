import { GET_GRADES, DELETE_GRADE, ADD_GRADE } from "../actions/types";

const initialState = {
    grades: []
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_GRADES:
            return {
                ...state,
                grades: action.payload
            };
        case DELETE_GRADE:
            return {
                ...state,
                grades: state.grades.filter(grade => grade.id !==
                    action.payload)
            };

        case ADD_GRADE:
            return {
                ...state,
                grades: [...state.grades, action.payload]
            };

        default:
            return state;

    }
}