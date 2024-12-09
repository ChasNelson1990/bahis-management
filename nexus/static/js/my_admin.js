document.addEventListener("DOMContentLoaded", function () {
    // Create a new container for search input and checkbox list
    const container = document.createElement('div');

    // Create a search input
    const searchInput = document.createElement('input');
    searchInput.placeholder = 'Search Users...';
    searchInput.style.width = '100%';
    searchInput.style.marginBottom = '10px';

    // Find the checkbox container
    const checkboxContainer = document.querySelector('.user-checkboxes');

    // Append search input to the new container
    container.appendChild(searchInput);

    // Create a new div to hold the checkboxes (copying their content)
    const newCheckboxContainer = document.createElement('div');
    newCheckboxContainer.className = 'user-checkboxes'; // Optional: keep the same class for styling

    // Clone the checkbox labels to the new container
    checkboxContainer.childNodes.forEach(child => {
        newCheckboxContainer.appendChild(child.cloneNode(true));
    });

    // Append the new checkbox container to the new parent container
    container.appendChild(newCheckboxContainer);

    // Replace the old checkbox container in the DOM with the new container
    checkboxContainer.parentNode.replaceChild(container, checkboxContainer);

    // Filter checkboxes based on search input
    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase();
        const checkboxes = newCheckboxContainer.querySelectorAll('label');

        checkboxes.forEach(label => {
            const isVisible = label.textContent.toLowerCase().includes(searchTerm);
            label.style.display = isVisible ? 'flex' : 'none';
        });
    });
});
