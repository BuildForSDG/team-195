import { combineReducers } from "redux";
import courses from "./courses";
import grades from "./grades";
import chapters from "./chapters"
import auth from "./auth";

export default combineReducers({
    courses,
    grades,
    chapters,
    auth
});