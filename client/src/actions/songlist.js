import axios from "axios";

import { GET_HITSONG, GET_MONTHNEW } from "./types";

export const getMonthnew = () => dispatch => {
  axios
    .get("/api/tj/monthnew")
    .then(res => {
      dispatch({
        type: GET_MONTHNEW,
        payload: res.data,
      });
    })
    .catch(err => console.log(err));
};

export const getHitsong = () => dispatch => {
  axios
    .get("/api/tj/hitsong")
    .then(res => {
      dispatch({
        type: GET_HITSONG,
        payload: res.data,
      });
    })
    .catch(err => console.log(err));
};
