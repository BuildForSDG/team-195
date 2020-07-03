import { combineReducers } from "redux";
import courses from "./courses";
import grades from "./grades";
import auth from "./auth";

export default combineReducers({
    courses,
    grades
});