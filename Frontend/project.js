document.addEventListener('DOMContentLoaded', () => {
    const projectGrid = document.getElementById('project-grid');
    
    // 1. Get projects from local storage (or show empty message)
    const savedProjects = JSON.parse(localStorage.getItem('myProjects')) || [];

    if (savedProjects.length === 0) {
        projectGrid.innerHTML = `<p style="color: #64748b;">No projects found. Click "Add New" to start!</p>`;
        return;
    }

    // 2. Loop through and create cards
    savedProjects.forEach((project) => {
        const card = document.createElement('div');
        card.className = 'project-card';
        card.innerHTML = `
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <span class="project-date">Created: ${project.date}</span>
        `;
        projectGrid.appendChild(card);
    });
});