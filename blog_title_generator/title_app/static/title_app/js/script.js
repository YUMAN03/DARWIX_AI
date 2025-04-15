
document.addEventListener('DOMContentLoaded', function() {
    // Add loading animation to form submission
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const submitButton = this.querySelector('button[type="submit"]');
            submitButton.innerHTML = 'Generating Titles...';
            submitButton.classList.add('btn-loading');
            submitButton.disabled = true;
        });
    }
    
    // Add character counter to textarea
    const textarea = document.querySelector('textarea');
    if (textarea) {
        const formText = textarea.nextElementSibling;
        const originalText = formText.textContent;
        
        // Update character count
        function updateCount() {
            const count = textarea.value.length;
            formText.textContent = `${originalText} (${count} characters)`;
            
            // Give visual feedback on length
            if (count < 100) {
                formText.classList.add('text-danger');
                formText.textContent += ' - Add more content for better results';
            } else {
                formText.classList.remove('text-danger');
            }
        }
        
        // Initial count
        updateCount();
        
        // Listen for changes
        textarea.addEventListener('input', updateCount);
    }
});