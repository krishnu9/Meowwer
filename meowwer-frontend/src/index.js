import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {MewsComponent} from './mews'
import * as serviceWorker from './serviceWorker';

const appEl = document.getElementById('root')
if (appEl) {
    ReactDOM.render(<App />, appEl);
}
const mewsEl = document.getElementById("meowwer")
if (mewsEl) {
    ReactDOM.render(<MewsComponent />, mewsEl);
}

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
