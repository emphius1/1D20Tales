```javascript
import React, { useState } from 'react';
import RaceClassDropdown from './RaceClassDropdown';
import CharacterNameTraits from './CharacterNameTraits';

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

    const handleFormSubmit = (event) => {
        event.preventDefault();
        // Call API to create character
    };

    return (
        <form onSubmit={handleFormSubmit}>
            <CharacterNameTraits 
                name={character.name} 
                traits={character.traits} 
                appearance={character.appearance} 
                onInputChange={handleInputChange} 
            />
            <RaceClassDropdown 
                race={character.race} 
                class={character.class} 
                onInputChange={handleInputChange} 
            />
            <button type="submit">Create Character</button>
        </form>
    );
};

export default CharacterCreationForm;
```