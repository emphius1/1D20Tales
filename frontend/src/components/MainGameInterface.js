```javascript
import React, { Component } from 'react';
import InteractiveMap from './InteractiveMap';
import QuestLog from './QuestLog';
import DialogueBox from './DialogueBox';

class MainGameInterface extends Component {
    constructor(props) {
        super(props);
        this.state = {
            character: {},
            inventory: [],
            quests: [],
            dialogue: ''
        };
    }

    componentDidMount() {
        // Fetch character, inventory, and quests data from the API
    }

    handleDialogueUpdate = (dialogue) => {
        this.setState({ dialogue });
    }

    render() {
        const { character, inventory, quests, dialogue } = this.state;

        return (
            <div className="main-game-interface">
                <div className="character-info">
                    <h2>{character.name}</h2>
                    <p>Level: {character.level}</p>
                    <p>Health: {character.health}</p>
                    <p>Mana: {character.mana}</p>
                </div>
                <div className="inventory">
                    <h2>Inventory</h2>
                    {inventory.map(item => (
                        <p key={item.id}>{item.name}</p>
                    ))}
                </div>
                <InteractiveMap />
                <QuestLog quests={quests} />
                <DialogueBox dialogue={dialogue} onDialogueUpdate={this.handleDialogueUpdate} />
            </div>
        );
    }
}

export default MainGameInterface;
```