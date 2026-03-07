const API_URL = "http://127.0.0.1:8000";

async function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const messageDiv = document.getElementById('message');

    // Basic Validation
    if (!email || !password) {
        messageDiv.style.color = "red";
        messageDiv.innerText = "Please fill in all fields.";
        return;
    }

    try {
        // This matches your @router.get("/login")
        const response = await fetch(`${API_URL}/login?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`);
        const data = await response.json();

        if (data["Log in"] === "Successful") {
            messageDiv.style.color = "green";
            messageDiv.innerText = "Success! Redirecting...";
            
            // Wait 1 second then redirect to your notes page
            setTimeout(() => {
                window.location.href = "notes.html"; 
            }, 1000);
        } else {
            messageDiv.style.color = "red";
            messageDiv.innerText = data["Log in"] === "Not Matched" ? "Incorrect password." : "User not found.";
        }
    } catch (error) {
        messageDiv.style.color = "red";
        messageDiv.innerText = "Cannot connect to server.";
        console.error("Error:", error);
    }
}