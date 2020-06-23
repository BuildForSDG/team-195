import { GET_GRADES } from "../actions/types";

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
        default:
            return state;

    }
}