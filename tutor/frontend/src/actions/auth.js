import axios from "axios";

import { USER_LOADING, USER_LOADED, AUTH_ERROR, LOGIN_SUCCESS, LOGIN_FAIL, REGISTER_SUCCESS, REGISTER_FAIL } from "./types";

//LOGIN USER
export const login = (username, password) => dispatch => {
    //Headers
    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    };

    //Request body
    const body = JSON.stringify({ username, password });

    axios.post('/api-token-auth/', body, config)
        .then(res => {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            });
        })
        .catch(err =>
            console.log(err)
        )
};

//REGISTER USER
export const register = ({ username, password, password2, is_staff }) => dispatch => {
    //Headers
    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    };

    //Request body
    const body = JSON.stringify({ username, password, password2, is_staff });

    axios.post('/users/add/', body, config)
        .then(res => {
            dispatch({
                type: REGISTER_SUCCESS,
                payload: res.data
            });
        })
        .catch(err =>
            console.log(err)
        )
};