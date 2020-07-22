import { GET_CHAPTERS, DELETE_CHAPTER, ADD_CHAPTER } from "../actions/types";

const initialState = {
    chapters: []
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_CHAPTERS:
            return {
                ...state,
                chapters: action.payload
            };
        case DELETE_CHAPTER:
            return {
                ...state,
                chapters: state.chapters.filter(chapter => chapter.id !==
                    action.payload)
            };

        case ADD_CHAPTER:
            return {
                ...state,
                chapters: [...state.chapters, action.payload]
            };
        default:
            return state;

    }
}