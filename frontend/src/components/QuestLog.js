```javascript
import React, { useState, useEffect } from 'react';

const QuestLog = () => {
    const [quests, setQuests] = useState([]);

    useEffect(() => {
        // Fetch quests from the backend
        fetch('/api/quests')
            .then(response => response.json())
            .then(data => setQuests(data.quests));
    }, []);

    return (
        <div className="quest-log">
            <h2>Quest Log</h2>
            {quests.length > 0 ? (
                <ul>
                    {quests.map((quest, index) => (
                        <li key={index}>
                            <h3>{quest.title}</h3>
                            <p>{quest.description}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No quests at the moment.</p>
            )}
        </div>
    );
};

export default QuestLog;
```