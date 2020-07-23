import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function loadMews(callback) {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "http://localhost:8000/api/meowws/";
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

function ActionBtn(props) {
  const { mew, action } = props;
  const className = props.className
    ? props.className
    : "btn btn-primary btn-sm";
  return action.type === "like" ? (
    <button className={className}>{mew.likes} Like</button>
  ) : null;
}

function Mew(props) {
  const mew = props.mew;
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6";
  return (
    <div className={className}>
      <p>
        {mew.id} - {mew.content}
      </p>
      <div>
        <ActionBtn mew={mew} action={{ type: "like" }} />
        <ActionBtn mew={mew} action={{ type: "unlike" }} />
      </div>
    </div>
  );
}

function App() {
  const [mews, setMews] = useState([]);

  useEffect(() => {
    const mycallback = (response, status) => {
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
        <div>
          {mews.map((mew, index) => {
            return <Mew mew={mew} key={index} />;
          })}
        </div>
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
