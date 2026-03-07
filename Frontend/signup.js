const API_URL = "http://127.0.0.1:8000";

async function signup() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const messageDiv = document.getElementById('message');

    if (!username || !email || !password) {
        messageDiv.style.color = "red";
        messageDiv.innerText = "Please fill in all fields.";
        return;
    }

    try {
        // Constructing the URL with query parameters for your FastAPI route
        const url = `${API_URL}/signup?username=${encodeURIComponent(username)}&email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`;

        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();

        if (data.message === "User created") {
            messageDiv.style.color = "green";
            messageDiv.innerText = "Account created! Redirecting to login...";
            setTimeout(() => {
                window.location.href = "index.html"; // Go to Sign In page
            }, 2000);
        } else {
            messageDiv.style.color = "orange";
            messageDiv.innerText = data.user || "Registration failed.";
        }
    } catch (error) {
        messageDiv.style.color = "red";
        messageDiv.innerText = "Error connecting to server.";
        console.error("Signup Error:", error);
    }
}