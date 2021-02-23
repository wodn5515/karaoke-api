import { GET_HITSONG, GET_MONTHNEW } from "../actions/types";

const initialState = {
  songs: [],
};

export default function songlist(state = initialState, action) {
  switch (action.type) {
    case GET_MONTHNEW:
      return {
        ...state,
        songs: action.payload,
      };
    case GET_HITSONG:
      return {
        ...state,
        songs: action.payload,
      };
    default:
      return state;
  }
}
