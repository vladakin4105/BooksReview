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

    // 3. Logica pentru Recomandare AI
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

    // 4. Logica pentru Filtrare Genuri (Corectată)
    const filterBtns = document.querySelectorAll('.filter-btn');
    const books = document.querySelectorAll('.book-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Scoate clasa 'active-filter' de pe toate butoanele și pune-o pe cel apăsat
            filterBtns.forEach(b => b.classList.remove('active-filter'));
            this.classList.add('active-filter');

            // Ia genul pe care vrem să-l filtrăm
            const selectedGenre = this.getAttribute('data-filter');

            // Arată sau ascunde cărțile
            books.forEach(book => {
                const bookGenre = book.getAttribute('data-genre');
                
                // Am adăugat o protecție mică: (bookGenre && ...) în caz că o carte nu are gen deloc
                if (selectedGenre === 'all' || (bookGenre && bookGenre.includes(selectedGenre))) {
                    book.style.display = 'block'; // Arată
                } else {
                    book.style.display = 'none';  // Ascunde
                }
            });
        });
    });

    // === Logica pentru Bilețelul Uitat ===
    const btnNote = document.getElementById('btn-note');
    const noteContainer = document.getElementById('vintage-note-container');
    const closeNote = document.getElementById('close-note');
    const noteText = document.getElementById('note-text');
    const noteAuthor = document.getElementById('note-author');

    if (btnNote) {
        btnNote.addEventListener('click', async () => {
            try {
                // 1. Facem fetch către fișierul JSON local
                const response = await fetch('/static/quotes.json');
                const quotes = await response.json();

                // 2. Alegem un citat complet la întâmplare
                const randomIndex = Math.floor(Math.random() * quotes.length);
                const randomQuote = quotes[randomIndex];

                // 3. Punem textul în HTML
                noteText.innerText = randomQuote.text;
                noteAuthor.innerText = "- " + randomQuote.author;

                // 4. Afișăm bilețelul pe ecran (îi scoatem clasa hidden)
                noteContainer.classList.remove('hidden');

            } catch (error) {
                console.error("Eroare la aducerea citatelor:", error);
            }
        });
    }

    // Funcția de închidere a bilețelului
    if (closeNote) {
        closeNote.addEventListener('click', () => {
            noteContainer.classList.add('hidden');
        });
    }

});