// Enhanced admin page security
(function() {
    // Prevent back button navigation
    window.history.pushState(null, null, window.location.href);
    
    window.onpopstate = function() {
        window.history.pushState(null, null, window.location.href);
        // Show a helpful message to users
        alert("For security reasons, please use the navigation menu or logout button to navigate.");
    };

    // Disable right-click in admin pages
    document.addEventListener('contextmenu', function(e) {
        if (window.location.href.includes('/admin')) {
            e.preventDefault();
            return false;
        }
    });

    // Handle page reload and closing
    window.addEventListener('beforeunload', function(e) {
        if (window.location.href.includes('/admin')) {
            e.preventDefault();
            // Clear message for modern browsers
            e.returnValue = 'Changes you made may not be saved. Are you sure you want to leave?';
            return e.returnValue;
        }
    });

    // Disable keyboard shortcuts that could navigate away
    document.addEventListener('keydown', function(e) {
        if (window.location.href.includes('/admin')) {
            // Prevent Alt+Left/Right (browser back/forward)
            if (e.altKey && (e.keyCode === 37 || e.keyCode === 39)) {
                e.preventDefault();
                return false;
            }
            // Prevent Backspace for navigation
            if (e.keyCode === 8 && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
                e.preventDefault();
                return false;
            }
        }
    });
})();