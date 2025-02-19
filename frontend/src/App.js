import React, { useState } from 'react';
import SummarizerForm from './components/SummarizerForm';
import './App.css';

function App() {
    const [summary, setSummary] = useState('');

    const handleSummaryReceived = (summaryData) => {
        setSummary(summaryData.summary);
    };

    return (
        <div className="App">
            <h1>Document Summarizer</h1>
            <SummarizerForm onSummaryReceived={handleSummaryReceived} />
            <h2>Summary:</h2>
            <div id="summaryOutput">{summary}</div>
        </div>
    );
}

export default App;