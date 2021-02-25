import { GET_HITSONG, GET_MONTHNEW } from "../actions/types";

const initialState = {
  songs: [],
  isLoading: true,
};

export default function songlist(state = initialState, action) {
  switch (action.type) {
    case GET_MONTHNEW:
      return {
        ...state,
        songs: action.payload,
        isLoading: false,
      };
    case GET_HITSONG:
      return {
        ...state,
        songs: action.payload,
        isLoading: false,
      };
    default:
      return state;
  }
}
