// Main JavaScript for Student Hostel Portal

document.addEventListener('DOMContentLoaded', function() {
    
    // Auto-hide alert messages after 4 seconds
    const flashMessages = document.querySelectorAll('.alert-flash');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500);
            });
        }, 4000);
    }

    // Confirmation on submitting complaints or posts
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerText = 'Processing...';
                submitBtn.style.opacity = '0.7';
            }
        });
    });

    // Rating input client-side validator (Limit ratings 1-5)
    const ratingInputs = document.querySelectorAll('input[type="number"][name="rating"], input[type="number"][name="hygiene_rating"]');
    ratingInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.value > 5) this.value = 5;
            if (this.value < 1) this.value = 1;
        });
    });
});