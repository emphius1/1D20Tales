```javascript
import React, { useState, useEffect } from 'react';

const DialogueBox = ({ dialogue }) => {
    const [currentDialogue, setCurrentDialogue] = useState(0);

    useEffect(() => {
        setCurrentDialogue(0);
    }, [dialogue]);

    const handleNextDialogue = () => {
        setCurrentDialogue(currentDialogue + 1);
    };

    return (
        <div className="dialogue-box">
            {dialogue && dialogue.length > 0 && (
                <div>
                    <p>{dialogue[currentDialogue]}</p>
                    {currentDialogue < dialogue.length - 1 && (
                        <button onClick={handleNextDialogue}>Next</button>
                    )}
                </div>
            )}
        </div>
    );
};

export default DialogueBox;
```