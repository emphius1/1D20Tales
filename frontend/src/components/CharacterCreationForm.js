```javascript
import React, { useState } from 'react';
import RaceClassDropdown from './RaceClassDropdown';
import CharacterNameTraits from './CharacterNameTraits';
import api from '../services/api';

const CharacterCreationForm = () => {
    const [character, setCharacter] = useState({
        name: '',
        race: '',
        class: '',
        traits: [],
        appearance: ''
    });

    const handleInputChange = (event) => {
        setCharacter({
            ...character,
            [event.target.name]: event.target.value
        });
    };

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await api.createCharacter(character);
            if (response.status === 200) {
                alert('Character created successfully!');
            }
        } catch (error) {
            console.error('Error creating character: ', error);
        }
    };

    return (
        <form onSubmit={handleFormSubmit}>
            <CharacterNameTraits 
                character={character} 
                handleInputChange={handleInputChange} 
            />
            <RaceClassDropdown 
                character={character} 
                handleInputChange={handleInputChange} 
            />
            <button type="submit">Create Character</button>
        </form>
    );
};

export default CharacterCreationForm;
```