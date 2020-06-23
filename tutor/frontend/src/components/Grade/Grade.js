import React, { Component } from 'react';

class GradesDropDown extends Component {
    constructor(props) {
        super(props)
        this.state = {
            values: []
        }

    }

    componentDidMount() {
        fetch('/courses/grades/')
            .then(function (res) {
                return res.json();
            }).then(function (json) {
                this.setState({
                    values: json
                })
            });
    }
    render() {
        return <div className="drop-down">
            <select>{
                this.state.values.map((obj) => {
                    return <option value={obj.id}>{obj.name}</option>
                })
            }</select>
        </div>;
    }
}

export default GradesDropDown;