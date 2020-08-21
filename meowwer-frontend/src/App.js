import React from "react";
import logo from "./logo.svg";
import {MewsComponent} from './mews'
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
          <MewsComponent/>
        </div>
      </header>
    </div>
  );
}

export default App;
