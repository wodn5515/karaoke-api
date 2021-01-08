import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import Todolist from "./Todolist";

export class Todos extends Component {
  render() {
    return <Todolist />;
  }
}
