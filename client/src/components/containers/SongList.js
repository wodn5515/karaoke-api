import React, { Component, Fragment } from "react";
import { connect } from "react-redux";

export class SongList extends Component {
  render() {
    return <Fragment></Fragment>;
  }
}

class MonthNew extends Component {
  render() {
    return <div></div>;
  }
}

const MonthNewmapStateToProps = state => ({});

const MonthNewmapDispatchToProps = {};

MonthNew = connect(mapStateToProps, mapDispatchToProps)(MonthNew);

export MonthNew;

class HitSong extends Component {
  render() {
    return <div></div>;
  }
}

const HitSongmapStateToProps = state => ({});

const HitSongmapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(HitSong);
