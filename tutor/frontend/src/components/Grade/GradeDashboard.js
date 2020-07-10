import React, { Fragment } from 'react';
import Form from './Form';
import Grades from './Grade';

export default function Dashboard() {
    return (
        <Fragment>
            <Form />
            <Grades />
        </Fragment>
    )
}