import React, { Component, Fragment } from "react";
import { connect } from "react-redux";

import { getHitsong, getMonthnew } from "../../actions/songlist";

class SongList extends Component {
  render() {
    return <Fragment></Fragment>;
  }
}

class MonthNew extends Component {
  componentDidMount() {
    this.props.getMonthnew();
  }

  render() {
    return (
      <ul>
        {this.props.songs.map((song, index) => (
          <li key={index}>{song.title}</li>
        ))}
      </ul>
    );
  }
}

class HitSong extends Component {
  componentDidMount() {
    this.props.getHitsong();
  }

  render() {
    return (
      <ul>
        {this.props.songs.map((song, index) => (
          <li key={index}>{song.title}</li>
        ))}
      </ul>
    );
  }
}

const mapStateToProps = state => ({
  songs: state.songs.songs,
});

MonthNew = connect(mapStateToProps, { getHitsong, getMonthnew })(MonthNew);

HitSong = connect(mapStateToProps, { getHitsong, getMonthnew })(HitSong);

export { MonthNew, HitSong, SongList };
