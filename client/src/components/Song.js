import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";

import { MonthNew, HitSong } from "./containers/SongList";

export default class Song extends Component {
  render() {
    return (
      <div id="song-wrap">
        <Switch>
          <Route exact path="/"></Route>
          <Route path="/monthnew" component={MonthNew} />
          <Route path="/hitsong" component={HitSong} />
        </Switch>
      </div>
    );
  }
}
