document.getElementById('geminiForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const reviewText = document.getElementById('reviewText').value;
    const resultDiv = document.getElementById('aiResult');
    
    resultDiv.innerHTML = '<span class="text-info">Analizez cu Gemini... ⏳</span>';

    try {
        const formData = new FormData();
        formData.append('review_text', reviewText);

        const response = await fetch('/api/analyze-review', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        resultDiv.innerHTML = `<div class="alert alert-success mt-2">
            <strong>Rezultat Gemini:</strong><br> ${data.sentiment_gemini}
        </div>`;
    } catch (error) {
        resultDiv.innerHTML = `<div class="alert alert-danger mt-2">Eroare la procesare.</div>`;
    }
});