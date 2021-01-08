import React, { Component, Fragment } from "react";
import ReactDOM, { render } from "react-dom";

import { Provider } from "react-redux";
import store from "../store";
import { Todos } from "./todos/TodoApp";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Todos />
      </Provider>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
