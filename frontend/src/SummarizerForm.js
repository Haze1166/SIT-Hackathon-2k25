import React, { useState } from 'react';

function SummarizerForm({ onSummaryReceived }) {
    const [apiKey, setApiKey] = useState('');
    const [file, setFile] = useState(null);

    const handleApiKeyChange = (event) => {
        setApiKey(event.target.value);
    };

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!apiKey) {
            alert("Please enter your API key.");
            return;
        }

        if (!file) {
            alert("Please upload a document.");
            return;
        }

        const reader = new FileReader();
        reader.onload = async (event) => {
            const fileContent = event.target.result;
            try {
                const formData = new FormData();
                formData.append('apiKey', apiKey);
                formData.append('filename', file.name);
                formData.append('fileContent', fileContent);

                const response = await fetch('http://localhost:5000/summarize', {  // Adjust URL if needed
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();
                onSummaryReceived(data);
            } catch (error) {
                console.error("Error:", error);
                alert("An error occurred during summarization. Check the console for details.");
            }
        };
        reader.readAsText(file);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="apiKey">Gemini API Key:</label>
            <input
                type="password"
                id="apiKey"
                name="apiKey"
                value={apiKey}
                onChange={handleApiKeyChange}
            /><br /><br />

            <label htmlFor="fileUpload">Upload Document:</label>
            <input
                type="file"
                id="fileUpload"
                name="fileUpload"
                onChange={handleFileChange}
            /><br /><br />

            <button type="submit">Summarize</button>
        </form>
    );
}

export default SummarizerForm;