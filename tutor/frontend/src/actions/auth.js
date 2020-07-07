import axios from "axios";

import { USER_LOADING, USER_LOADED, AUTH_ERROR } from "./types";

//Check token and Load User
export const loadUser = () => (dispatch, getState) => {
    //User Loading
    dispatch({ type: USER_LOADING });

    //Get token from state
    const token = getState().auth.token;

    //Headers
    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    }
    //If token, add to headers config
    if (token) {
        config.headers['Authorization'] = `Token ${token}`;
    }
}