```javascript
import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const InteractiveMap = ({ characterLocation }) => {
    const [position, setPosition] = useState(characterLocation);

    useEffect(() => {
        setPosition(characterLocation);
    }, [characterLocation]);

    return (
        <MapContainer center={position} zoom={13} style={{ height: "100vh", width: "100%" }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            />
            <Marker position={position}>
                <Popup>
                    You are here
                </Popup>
            </Marker>
        </MapContainer>
    );
};

export default InteractiveMap;
```