```javascript
import React, { useState, useEffect } from 'react';

const DialogueBox = ({ dialogue }) => {
    const [dialogueText, setDialogueText] = useState('');

    useEffect(() => {
        setDialogueText(dialogue);
    }, [dialogue]);

    return (
        <div className="dialogue-box">
            <p>{dialogueText}</p>
        </div>
    );
};

export default DialogueBox;
```