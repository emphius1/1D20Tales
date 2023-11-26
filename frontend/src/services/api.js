```javascript
import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const createCharacter = async (characterData) => {
  try {
    const response = await axios.post(`${API_URL}/character`, characterData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getCharacter = async (characterId) => {
  try {
    const response = await axios.get(`${API_URL}/character/${characterId}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateCharacter = async (characterId, updatedData) => {
  try {
    const response = await axios.put(`${API_URL}/character/${characterId}`, updatedData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteCharacter = async (characterId) => {
  try {
    const response = await axios.delete(`${API_URL}/character/${characterId}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const manageInventory = async (characterId, inventoryData) => {
  try {
    const response = await axios.post(`${API_URL}/inventory/${characterId}`, inventoryData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const upgradeSkills = async (characterId, skillData) => {
  try {
    const response = await axios.post(`${API_URL}/skills/${characterId}`, skillData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
```