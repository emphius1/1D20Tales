```javascript
import { createContext, useReducer } from 'react';

// Initial state
const initialState = {
  character: {},
  inventory: [],
  gameProgress: {},
};

// Create context
export const GameDataContext = createContext(initialState);

// Reducer
const reducer = (state, action) => {
  switch (action.type) {
    case 'SET_CHARACTER':
      return {
        ...state,
        character: action.payload,
      };
    case 'SET_INVENTORY':
      return {
        ...state,
        inventory: action.payload,
      };
    case 'SET_GAME_PROGRESS':
      return {
        ...state,
        gameProgress: action.payload,
      };
    default:
      return state;
  }
};

// Provider component
export const GameDataProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <GameDataContext.Provider value={[state, dispatch]}>
      {children}
    </GameDataContext.Provider>
  );
};
```