```javascript
import { createContext, useReducer } from 'react';

// Initial state
const initialState = {
  character: {},
  inventory: [],
  gameStates: {},
};

// Create context
export const GameDataContext = createContext(initialState);

// Reducer
const gameDataReducer = (state, action) => {
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
    case 'SET_GAME_STATES':
      return {
        ...state,
        gameStates: action.payload,
      };
    default:
      return state;
  }
};

// Provider component
export const GameDataProvider = ({ children }) => {
  const [state, dispatch] = useReducer(gameDataReducer, initialState);

  // Actions
  const setCharacter = (character) => {
    dispatch({
      type: 'SET_CHARACTER',
      payload: character,
    });
  };

  const setInventory = (inventory) => {
    dispatch({
      type: 'SET_INVENTORY',
      payload: inventory,
    });
  };

  const setGameStates = (gameStates) => {
    dispatch({
      type: 'SET_GAME_STATES',
      payload: gameStates,
    });
  };

  return (
    <GameDataContext.Provider
      value={{
        character: state.character,
        inventory: state.inventory,
        gameStates: state.gameStates,
        setCharacter,
        setInventory,
        setGameStates,
      }}
    >
      {children}
    </GameDataContext.Provider>
  );
};
```