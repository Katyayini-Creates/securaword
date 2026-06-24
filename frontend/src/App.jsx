import "./App.css"
import { useState } from "react"

function App() {

  const [password, setPassword] = useState("")
  const [entropy, setEntropy] = useState(null)
  const [score, setScore] = useState(null)
  const [feedback, setFeedback] = useState([])

  async function analyzePassword(value) {

    setPassword(value)

    if (value.length === 0) {
      setEntropy(null)
      setScore(null)
      setFeedback([])
      return
    }

    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        password: value
      })
    })

    const data = await response.json()

    setEntropy(data.entropy)
    setScore(data.score)
    setFeedback(data.feedback)
  }

  const meterWidth = score ? (score / 5) * 100 : 0

  return (
    <div className="app">

      <div className="panel">

        <h1 className="title">
          🔐 SECURAWORD
        </h1>

        <p className="subtitle">
          PASSWORD ANALYSIS TERMINAL
        </p>

        <input
          type="password"
          placeholder="ENTER PASSWORD..."
          value={password}
          onChange={(e) => analyzePassword(e.target.value)}
          className="password-input"
        />

        <div className="meter-container">
          <div
            className="meter-fill"
            style={{
              width: `${meterWidth}%`
            }}
          ></div>
        </div>

      </div>

    </div>
  )
}

export default App

