document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Logica pentru Formularul de Analiză Sentiment (Gemini)
    const geminiForm = document.getElementById('geminiForm');
    if (geminiForm) {
        geminiForm.addEventListener('submit', async function(e) {
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
    }

    // 2. Logica pentru Adăugare/Ștergere Favorite
    const favoriteButtons = document.querySelectorAll(".btn-favorite");
    
    favoriteButtons.forEach(button => {
        button.addEventListener("click", async function() {
            const bookId = this.getAttribute("data-id");
            
            try {
                // Facem apelul către backend pentru a schimba starea cărții
                const response = await fetch(`/api/books/${bookId}/favorite`, {
                    method: 'PUT'
                });
                
                if (response.ok) {
                    const data = await response.json();
                    
                    // Actualizăm aspectul butonului în funcție de răspunsul serverului
                    if (data.is_favorite) {
                        this.classList.remove("btn-outline-danger");
                        this.classList.add("btn-danger");
                        this.innerHTML = "❤️ Elimină din Favorite";
                    } else {
                        this.classList.remove("btn-danger");
                        this.classList.add("btn-outline-danger");
                        this.innerHTML = "🤍 Adaugă la Favorite";
                    }
                } else {
                    alert("Eroare la actualizarea favoritelor.");
                }
            } catch (error) {
                console.error("Eroare:", error);
            }
        });
    });

    const btnRecommend = document.getElementById("btnRecommend");
    const recommendationResult = document.getElementById("recommendationResult");

    if (btnRecommend) {
        btnRecommend.addEventListener("click", async () => {
            // Blocăm butonul și arătăm că procesăm
            btnRecommend.disabled = true;
            btnRecommend.innerHTML = "Se generează... ⏳";
            recommendationResult.innerHTML = "";

            try {
                const response = await fetch('/api/recommendation');
                const data = await response.json();

                if (response.ok) {
                    // Afișăm recomandarea de la Gemini
                    recommendationResult.innerHTML = `<div class="alert alert-success small text-start">${data.recomandare}</div>`;
                } else {
                    recommendationResult.innerHTML = `<div class="alert alert-danger small">A apărut o eroare.</div>`;
                }
            } catch (error) {
                recommendationResult.innerHTML = `<div class="alert alert-danger small">Eroare de conexiune.</div>`;
            } finally {
                // Readucem butonul la starea inițială
                btnRecommend.disabled = false;
                btnRecommend.innerHTML = "Obține Recomandare";
            }
        });
    }
});