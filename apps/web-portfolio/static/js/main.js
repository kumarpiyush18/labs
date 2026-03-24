document.addEventListener('DOMContentLoaded', () => {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const tags = Array.from(card.querySelectorAll('.tag')).map(t => t.textContent.trim());

                if (filterValue === 'all' || tags.includes(filterValue)) {
                    card.style.display = 'flex';
                    // Re-trigger animation
                    card.style.animation = 'none';
                    card.offsetHeight; /* trigger reflow */
                    card.style.animation = 'fadeUp 0.5s ease forwards';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
