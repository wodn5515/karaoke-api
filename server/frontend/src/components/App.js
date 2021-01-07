import React, { Component, Fragment } from "react";
import ReactDOM, { render } from "react-dom";
import Header from "./layout/Header";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    document.title = "할일";
    fetch("/api/todo")
      .then(response => {
        return response.json();
      })
      .then(data => {
        this.setState({ data });
      });
  }

  render() {
    return (
      <>
        <Header />
        <ul>
          {this.state.data.map(todo => {
            return (
              <li key={todo.id}>
                {todo.todo} - {todo.date}
              </li>
            );
          })}
        </ul>
      </>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
