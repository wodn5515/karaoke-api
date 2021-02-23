import React, { Component } from "react";
import { NavLink } from "react-router-dom";

import Song from "./Song";

class App extends Component {
  render() {
    return (
      <div>
        <div className="link">
          <NavLink to="/">홈으로</NavLink>
          <NavLink to="/monthnew">이 달의 신곡</NavLink>
          <NavLink to="/hitsong">인기곡</NavLink>
        </div>
        <Song />
      </div>
    );
  }
}

export default App;
