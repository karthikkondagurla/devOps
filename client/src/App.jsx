import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null)

  useEffect(() => {
    // Use environment variable for API URL, fallback to localhost for local dev
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:5000';
    console.log("Fetching data from:", apiUrl);

    fetch(`${apiUrl}/`)
      .then(res => res.json())
      .then(data => setData(data))
      .catch(err => console.error("Error fetching data:", err))
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>Pipeline Pulse</h1>
        <p>Full-Stack DevOps Demo</p>

        <div className="card">
          {data ? (
            <div>
              <h3>Backend Response:</h3>
              <pre>{JSON.stringify(data, null, 2)}</pre>
            </div>
          ) : (
            <p>Loading data from Flask...</p>
          )}
        </div>
      </header>
    </div>
  )
}

export default App
