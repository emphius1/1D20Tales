import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RaceClassDropdown = () => {
    const [races, setRaces] = useState([]);
    const [classes, setClasses] = useState([]);
    const [selectedRace, setSelectedRace] = useState('');
    const [selectedClass, setSelectedClass] = useState('');

    useEffect(() => {
        axios.get('/api/races')
            .then(response => {
                setRaces(response.data);
                setSelectedRace(response.data[0]);
            })
            .catch(error => console.error(`Error: ${error}`));

        axios.get('/api/classes')
            .then(response => {
                setClasses(response.data);
                setSelectedClass(response.data[0]);
            })
            .catch(error => console.error(`Error: ${error}`));
    }, []);

    const handleRaceChange = (event) => {
        setSelectedRace(event.target.value);
    };

    const handleClassChange = (event) => {
        setSelectedClass(event.target.value);
    };

    return (
        <div>
            <label>
                Race:
                <select value={selectedRace} onChange={handleRaceChange}>
                    {races.map(race => <option key={race} value={race}>{race}</option>)}
                </select>
            </label>
            <label>
                Class:
                <select value={selectedClass} onChange={handleClassChange}>
                    {classes.map(cls => <option key={cls} value={cls}>{cls}</option>)}
                </select>
            </label>
        </div>
    );
};

export default RaceClassDropdown;