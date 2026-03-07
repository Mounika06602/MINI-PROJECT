document.addEventListener('DOMContentLoaded', () => {
    // This pulls the "user" data we saved in the console earlier
    const userData = JSON.parse(localStorage.getItem('user'));

    if (userData) {
        // These IDs must match your HTML exactly!
        document.getElementById('user-name').textContent = `Name: ${userData.name}`;
        document.getElementById('user-email').textContent = `Email: ${userData.email}`;
        document.getElementById('user-role').textContent = `Role: ${userData.role}`;

        // If the user is an admin, show the extra menu item
        if (userData.role === 'admin') {
            const adminTools = document.getElementById('admin-tools-item');
            if (adminTools) {
                adminTools.style.display = 'block';
            }
        }
    } else {
        // If no user is found, it sends you back to the login page
        console.log("No user found in localStorage");
    }
});