import { FiEye, FiEyeOff } from "react-icons/fi"
import "./App.css"
import { useState } from "react"

function App() {
  const [password, setPassword] = useState("")
  const [entropy, setEntropy] = useState(null)
  const [score, setScore] = useState(null)
  const [feedback, setFeedback] = useState([])
  const [showPassword, setShowPassword] = useState(false)

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
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        password: value,
      }),
    })

    const data = await response.json()

    setEntropy(data.entropy)
    setScore(data.score)
    setFeedback(data.feedback)
  }

  const meterWidth = score ? (score / 5) * 100 : 0

  const meterColor =
    score === null
      ? "#00F5FF"
      : score <= 1
      ? "#FF3131"
      : score <= 3
      ? "#FFB000"
      : "#39FF14"

  return (
    <div className="app">
      <div className="panel">

        <h1 className="title">SECURAWORD</h1>

        <p className="subtitle">
          PASSWORD STRENGTH ANALYZER
        </p>

        <div className="input-container">
          <input
            type={showPassword ? "text" : "password"}
            placeholder="ENTER PASSWORD..."
            value={password}
            onChange={(e) => analyzePassword(e.target.value)}
            className="password-input"
          />

          <button
            type="button"
            className="eye-button"
            onClick={() => setShowPassword(!showPassword)}
          >
            {showPassword ? <FiEyeOff /> : <FiEye />}
          </button>
        </div>

        <div className="meter-labels">
          <span className={score <= 1 ? "active-weak" : ""}>
            WEAK
          </span>

          <span
            className={
              score > 1 && score <= 3
                ? "active-medium"
                : ""
            }
          >
            MEDIUM
          </span>

          <span className={score > 3 ? "active-strong" : ""}>
            STRONG
          </span>
        </div>

        <div className="meter-container">
          <div
            className="meter-fill"
            style={{
              width: `${meterWidth}%`,
              background: meterColor,
              boxShadow: `0 0 10px ${meterColor}, 0 0 20px ${meterColor}`,
            }}
          ></div>
        </div>

        {score !== null && (
          <div
            className="strength-label"
            style={{
              color:
                score <= 1
                  ? "#FF3131"
                  : score <= 3
                  ? "#FFB000"
                  : "#39FF14",

              textShadow:
                score <= 1
                  ? "0 0 10px #FF3131"
                  : score <= 3
                  ? "0 0 10px #FFB000"
                  : "0 0 10px #39FF14",
            }}
          >
            SECURITY LEVEL:{" "}
            {score <= 1
              ? "WEAK"
              : score <= 3
              ? "MEDIUM"
              : "STRONG"}
          </div>
        )}

        {entropy !== null && (
          <div className="entropy-display">
            ENTROPY: {entropy.toFixed(2)} BITS
          </div>
        )}

        {score !== null && (
          <div className="report-container">

            <div className="report-title">
              SECURITY REPORT
            </div>

            {feedback.length > 0 ? (
              feedback.map((item, index) => (
                <div key={index} className="report-item">
                  ⚠ {item}
                </div>
              ))
            ) : (
              <div className="report-success">
                ✓ No security issues detected
              </div>
            )}

          </div>
        )}

      </div>
    </div>
  )
}

export default App