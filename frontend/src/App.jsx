import { useState } from "react"

function App() {

  const [password, setPassword] = useState("")
  const [entropy, setEntropy] = useState(null)
  const [score, setScore] = useState(null)
  const [feedback, setFeedback] = useState([])

  async function analyzePassword(value){

    setPassword(value)

    if(value.length === 0){
      setEntropy(null)
      setScore(null)
      setFeedback([])
      return
    }

    const response = await fetch("http://127.0.0.1:8000/analyze",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        password:value
      })
    })

    const data = await response.json()

    setEntropy(data.entropy)
    setScore(data.score)
    setFeedback(data.feedback)
  }

  const meterWidth = score ? (score/5)*100 : 0

  return (

    <div style={{textAlign:"center",marginTop:"100px"}}>

      <h1>🔐 SecuraWord Password Analyzer</h1>

      <input
        type="password"
        placeholder="Enter password"
        value={password}
        onChange={(e)=> analyzePassword(e.target.value)}
        style={{padding:"10px",width:"300px"}}
      />

      <div style={{
        width:"300px",
        height:"15px",
        background:"#ddd",
        margin:"20px auto",
        borderRadius:"5px"
      }}>

        <div style={{
          width:`${meterWidth}%`,
          height:"100%",
         background:
         score <= 1 ? "red" :
         score <= 3 ? "orange" :
        "limegreen"
        }}></div>

      </div>

      {entropy && <p>Entropy: {entropy} bits</p>}

      <ul style={{width:"300px",margin:"auto",textAlign:"left"}}>
        {feedback.map((item,index)=>(
          <li key={index}>{item}</li>
        ))}
      </ul>

    </div>

  )
}

export default App