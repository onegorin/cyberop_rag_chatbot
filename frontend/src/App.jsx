import { useState } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    const response = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await response.json();
    setAnswer(data.answer);
  };

  return (
    <div className="p-6 font-sans text-white bg-gray-900 min-h-screen">
      <h1 className="text-3xl mb-6">Cyber Op Chatbot</h1>
      <textarea
        className="w-full p-4 text-black"
        rows="5"
        placeholder="Ask a cybersecurity question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      ></textarea>
      <button className="bg-blue-600 px-6 py-2 mt-4" onClick={askQuestion}>Submit</button>
      <div className="mt-6 p-4 bg-gray-800">{answer}</div>
    </div>
  );
}

export default App;