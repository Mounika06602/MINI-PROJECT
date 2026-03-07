function saveNote() {
    const title = document.getElementById('note-title').value;
    const content = document.getElementById('note-content').value;

    if (!title || !content) {
        alert("Please fill in both fields!");
        return;
    }

    const savedNotes = JSON.parse(localStorage.getItem('myNotes')) || [];

    const newNote = {
        title: title,
        content: content,
        Createdat: new Date().toISOString(),
        Updatedat: new Date().toISOString()
    };

    savedNotes.push(newNote);
    localStorage.setItem('myNotes', JSON.stringify(savedNotes));

    alert("Note saved!");
    // This redirects you back to the list to see your new note
    window.location.href = 'notes.html'; 
}




document.addEventListener('DOMContentLoaded', () => {
    loadNotes();
});

function loadNotes() {
    const notesBody = document.getElementById('notes-body');
    if (!notesBody) return; // Safety check

    const savedNotes = JSON.parse(localStorage.getItem('myNotes')) || [];
    notesBody.innerHTML = ""; 

    if (savedNotes.length === 0) {
        notesBody.innerHTML = "<tr><td colspan='5' style='text-align:center;'>No notes found.</td></tr>";
        return;
    }

    savedNotes.forEach((note, index) => {
        const row = document.createElement('tr');
        const created = new Date(note.Createdat).toLocaleString();
        const updated = new Date(note.Updatedat).toLocaleString();

        row.innerHTML = `
            <td><strong>${note.title}</strong></td>
            <td>${note.content.substring(0, 40)}...</td>
            <td>${created}</td>
            <td>${updated}</td>
            <td>
                <button class="delete-btn" onclick="deleteNote(${index})">
                    <i class="fas fa-trash"></i> Delete
                </button>
            </td>
        `;
        notesBody.appendChild(row);
    });
}


// new_notes.js
async function saveNote() {
    const title = document.getElementById('note-title').value;
    const content = document.getElementById('note-content').value;

    if (!title || !content) {
        alert("Please fill in both fields!");
        return;
    }

    const newNote = {
        title: title,
        content: content
    };

    try {
        // Calling your FastAPI backend
        const response = await fetch('/notes/create', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newNote)
        });

        const result = await response.json();

        if (response.ok) {
            alert("Note saved to MongoDB!");
            window.location.href = 'notes.html'; 
        } else {
            alert("Error: " + result.detail);
        }
    } catch (error) {
        console.error("Connection failed:", error);
        alert("Could not connect to the server.");
    }
}

