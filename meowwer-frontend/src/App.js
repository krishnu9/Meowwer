import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function loadMews(callback) {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "http://127.0.0.1:8000/api/meowws";
  const responseType = "json";
  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.onload = function () {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = function (e) {
    console.log(e);
    callback({ message: "The request was an error" }, 400);
  };
  xhr.send();
}
function App() {
  const [mews, setMews] = useState([]);

  useEffect(() => {
    const mycallback = (response, status) => {
      console.log(response, status);
      if (status === 200) {
        setMews(response);
      } else {
        alert("There was an error");
      }
    };
    loadMews(mycallback);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {mews.map((mew, index) => {
            return <li>{mew.content}</li>;
          })}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
