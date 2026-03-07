document.addEventListener('DOMContentLoaded', () => {
    loadAllNotes();
});

// 1. Fetch ALL notes from MongoDB
async function loadAllNotes() {
    const notesBody = document.getElementById('notes-body');
    if (!notesBody) return;

    try {
        const response = await fetch('/notes/all'); // Calls the new route
        const notes = await response.json();

        notesBody.innerHTML = ""; 

        if (!response.ok || notes.length === 0) {
            notesBody.innerHTML = "<tr><td colspan='5' style='text-align:center;'>No notes found in database.</td></tr>";
            return;
        }

        notes.forEach((note) => {
            const row = document.createElement('tr');
            const created = new Date(note.Createdat).toLocaleString();
            const updated = new Date(note.Updatedat).toLocaleString();

            row.innerHTML = `
                <td><strong>${note.title}</strong></td>
                <td>${note.content.substring(0, 40)}...</td>
                <td>${created}</td>
                <td>${updated}</td>
                <td>
                    <button class="delete-btn" onclick="deleteNoteFromServer('${note.title}')">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            `;
            notesBody.appendChild(row);
        });
    } catch (error) {
        console.error("Failed to fetch notes:", error);
    }
}

// 2. Delete Note from MongoDB
async function deleteNoteFromServer(title) {
    if (!confirm(`Are you sure you want to delete "${title}"?`)) return;

    try {
        const response = await fetch(`/notes/delete?title=${encodeURIComponent(title)}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            alert("Note deleted from database!");
            loadAllNotes(); // Refresh the list
        } else {
            const error = await response.json();
            alert("Error: " + error.detail);
        }
    } catch (error) {
        alert("Delete failed. Check server connection.");
    }
}

// 3. Real-time Search (Kept as is, it works locally on the loaded rows)
function searchNotes() {
    let input = document.getElementById('search-input').value.toLowerCase();
    let rows = document.getElementById('notes-body').getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        let titleCell = rows[i].getElementsByTagName('td')[0];
        if (titleCell) {
            let textValue = titleCell.textContent || titleCell.innerText;
            rows[i].style.display = textValue.toLowerCase().includes(input) ? "" : "none";
        }
    }
}