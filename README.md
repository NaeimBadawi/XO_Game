
**Die Zusammenfassung des eindimensionalen Tic-Tac-Toe-Spiels (XO):**

**Spielregeln:**
1. Das Spiel wird auf einer eindimensionalen Linie (eine Reihe von leeren Feldern) gespielt.  
2. Zwei Spieler sind beteiligt:  
   - **Spieler 1** setzt ein **X** in ein leeres Feld.  
   - **Spieler 2** setzt ein **O** in ein leeres Feld.  
3. Die Spieler wechseln sich ab, beginnend mit Spieler 1.  

**Beispielverlauf:**  
1. **Größe 1:** `----------x---------` (Spieler 1 setzt X)  
2. **Größe 2:** `-------x--o---------` (Spieler 2 setzt O)  
3. **Größe 3:** `-------xx-o---------` (Spieler 1 setzt ein zweites X)  
4. **Größe 4:** `-------xxoo---------` (Spieler 2 setzt ein zweites O)  
5. **Größe 5:** `------xxxoo---------` (Spieler 1 setzt ein drittes X und gewinnt mit "XXX")  

**Ziel:**  
- Gewonnen hat, wer zuerst **drei seiner Symbole in einer Reihe** hat (z. B. XXX oder OOO). 
