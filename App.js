import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');

  const createUser = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/user', { username });
      console.log(response.data); // Handle the response accordingly
    } catch (error) {
      console.error("An error occurred while sending the request", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button onClick={createUser}>Create User</button>
    </div>
  );
}

export default App;
