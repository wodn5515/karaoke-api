import React, { Component } from "react";
import { connect } from "react-redux";
import { getTodos } from "../../actions/todos";

export class Todolist extends Component {
  componentDidMount() {
    this.props.getTodos();
  }

  render() {
    return (
      <div>
        <table>
          <thead>
            <tr>
              <th>No</th>
              <th>Todo</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  todos: state.todos.todos,
});

export default connect(mapStateToProps, { getTodos })(Todolist);
