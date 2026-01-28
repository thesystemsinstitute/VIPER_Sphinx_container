// Make external links open in new tab, keep internal links in same tab
document.addEventListener('DOMContentLoaded', function() {
    // Get all links
    var links = document.querySelectorAll('a');
    
    links.forEach(function(link) {
        var href = link.getAttribute('href');
        
        if (!href) return;
        
        // Check if link is external (starts with http:// or https://)
        var isExternal = href.startsWith('http://') || href.startsWith('https://');
        
        // Check if it's a localhost link (internal)
        var isLocalhost = href.includes('localhost') || href.includes('127.0.0.1');
        
        // Open in new tab if external and not localhost
        if (isExternal && !isLocalhost) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});
