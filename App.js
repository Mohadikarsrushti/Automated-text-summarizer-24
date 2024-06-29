import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      setText(e.target.result);
    };
    reader.readAsText(file);
  };

  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  const getSummary = () => {
    fetch('http://127.0.0.1:5000/summarize', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    })
      .then(response => response.json())
      .then(data => setSummary(data.summary))
      .catch(error => console.error('Error:', error));
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Text Summarizer</h1>
      <div>
        <h2>Upload a Text File</h2>
        <input type="file" onChange={handleFileUpload} />
      </div>
      <div>
        <h2>Or Enter Text Manually</h2>
        <textarea
          rows="10"
          cols="50"
          placeholder="Enter your text here..."
          value={text}
          onChange={handleTextChange}
          style={{ width: '100%', padding: '10px', fontSize: '16px' }}
        />
      </div>
      <button onClick={getSummary} style={{ marginTop: '20px', padding: '10px 20px', fontSize: '16px' }}>
        Summarize
      </button>
      {summary && (
        <div>
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;