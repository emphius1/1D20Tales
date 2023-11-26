```javascript
import React, { useState, useEffect } from 'react';
import InteractiveMap from './InteractiveMap';
import QuestLog from './QuestLog';
import DialogueBox from './DialogueBox';
import api from '../services/api';

const MainGameInterface = () => {
  const [character, setCharacter] = useState(null);
  const [quests, setQuests] = useState([]);
  const [dialogue, setDialogue] = useState('');

  useEffect(() => {
    const fetchCharacter = async () => {
      const response = await api.getCharacter();
      setCharacter(response.data);
    };

    const fetchQuests = async () => {
      const response = await api.getQuests();
      setQuests(response.data);
    };

    fetchCharacter();
    fetchQuests();
  }, []);

  const handleDialogue = (newDialogue) => {
    setDialogue(newDialogue);
  };

  return (
    <div className="main-game-interface">
      <InteractiveMap character={character} handleDialogue={handleDialogue} />
      <QuestLog quests={quests} />
      <DialogueBox dialogue={dialogue} />
    </div>
  );
};

export default MainGameInterface;
```