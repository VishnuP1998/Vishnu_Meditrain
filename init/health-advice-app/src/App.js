import React, { useState } from 'react';
import './App.css';
import logo from './logo.svg';

function App() {
  // State to handle user input and fetched advice
  const [userQuery, setUserQuery] = useState('');
  const [healthAdvice, setHealthAdvice] = useState('');

  // Handle input change
  const handleInputChange = (event) => {
    setUserQuery(event.target.value);
  };

  // Fetch advice based on the user's query
  const getHealthAdvice = () => {
    let advice = '';

    if (userQuery.toLowerCase().includes('headache')) {
      advice = 'It’s important to stay hydrated and rest. Consider using over-the-counter pain relief if necessary.';
    } else if (userQuery.toLowerCase().includes('fever')) {
      advice = 'Drink plenty of fluids and rest. If symptoms persist, consult a healthcare professional.';
    } else if (userQuery.toLowerCase().includes('cold')) {
      advice = 'Stay warm, hydrate, and rest. Over-the-counter medications can help alleviate symptoms.';
    } else {
      advice = 'Please enter a specific health concern to receive advice.';
    }

    setHealthAdvice(advice);
  };

  return (
    <div className="HealthApp">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to My Health Advice App</h1>

        <div className="input-container">
          <input
            type="text"
            value={userQuery}
            onChange={handleInputChange}
            placeholder="Enter your health issue..."
            className="input-field"
          />
          <button onClick={getHealthAdvice} className="advice-button">
            Get Health Advice
          </button>
        </div>

        <div className="advice-container">
          <h3>Advice:</h3>
          <p>{healthAdvice}</p>
        </div>

        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}

export default App;
