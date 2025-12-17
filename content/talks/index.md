---
reading_time: false
type: talks
# These disable sidebars and table of contents
_build:
  list: never
toc: false
---

<style>
/* Hide sidebars and unnecessary elements */
.max-w-prose {
    display: none !important 
}

/* Hide sidebars on talks page */
.col-12.col-xl-3,
.col-12.col-xl-2,
aside,
.docs-sidebar,
.td-sidebar,
.hb-scrollbar,
.hb-toc,
.td-toc {
    max-width: 20% !important;
}

/* Make main content full width */
.col-12.col-xl-7,
.col-12.col-xl-8,
.td-content {
  max-width: 90% !important;
  flex: 0 0 100% !important;
}

/* ===== TARGET THE MAIN CONTAINERS ===== */
/* Remove the max-width constraint from the main container */
main.max-w-6xl {
  max-width: 100% !important;
  width: 100% !important;
}

/* Remove horizontal padding from the main container */
main.px-6, main.md\:px-12 {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

/* Remove max-width from the prose container */
.prose {
  max-width: 100% !important;
}

/* ===== THEME AWARE COLOR STYLING ===== */
:root, [data-theme="light"] {
  .talks-page {
    --page-title-color: var(--color-gray-900, #171717);
    --section-title-color: var(--color-primary-800, #935b59);
    --table-border: var(--color-gray-300, #d6d4d2);
    --table-header-bg: var(--color-primary-50, #f6dcdb);
    --table-header-color: var(--color-primary-800, #935b59);
    --table-row-bg: transparent;
    --table-row-bg-alt: var(--color-gray-50, #f8f7f7);
    --table-text-primary: var(--color-gray-800, #4e4a45);
    --table-text-secondary: var(--color-gray-600, #6c6660);
    --link-color: var(--color-primary-600, #cc7e7b);
    --link-hover-color: var(--color-primary-800, #935b59);
  }
}

.dark, [data-theme="dark"] {
  .talks-page {
    --page-title-color: #ffffff;
    --section-title-color: var(--color-primary-300, #f6dcdb);
    --table-border: var(--color-gray-600, #6c6660);
    --table-header-bg: rgba(var(--color-primary-900, 30 58 138), 0.3);
    --table-header-color: var(--color-primary-300, #f6dcdb);
    --table-row-bg: transparent;
    --table-row-bg-alt: rgba(var(--color-gray-950-rgb, 36 34 32), 0.2);
    --table-text-primary: var(--color-gray-300, #d6d4d2);
    --table-text-secondary: var(--color-gray-400, #9ca3af);
    --link-color: var(--color-primary-400, #60a5fa);
    --link-hover-color: var(--color-primary-300, #93c5fd);
  }
}

/* ===== PAGE TITLE AND HEADERS ===== */
.talks-page h1 {
  text-align: center !important;
  margin-bottom: 1.5rem !important;
  color: var(--page-title-color);
  font-weight: 700;
  font-size: 2.5rem;
  transition: color 0.3s ease;
}

.talks-page h2, .talks-page h3 {
  text-align: left !important;
  margin-top: 2.5rem !important;
  margin-bottom: 1.5rem !important;
  color: var(--section-title-color);
  font-weight: 600;
  border-bottom: 2px solid var(--table-border);
  padding-bottom: 0.5rem;
  transition: color 0.3s ease, border-color 0.3s ease;
}

/* ===== TABLE STYLING ===== */
.talks-table {
  width: 100% !important;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.85rem;
  table-layout: fixed;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid var(--table-border);
}

.talks-table th, .talks-table td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--table-border);
  vertical-align: top;
  text-align: left;
  transition: all 0.3s ease;
}

.talks-table th {
  font-weight: 700;
  white-space: nowrap;
  /*background-color: var(--table-header-bg);
  color: var(--table-header-color);*/
  border-bottom: 2px solid var(--table-border);
}

.talks-table tbody tr {
  background-color: var(--table-row-bg);
}


.talks-table tbody tr:hover {
  background-color: var(--table-row-hover);
  transform: translateX(2px);
}

/* Column widths */
.talks-table th:nth-child(1), .talks-table td:nth-child(1) { width: 13%; }
.talks-table th:nth-child(2), .talks-table td:nth-child(2) { width: 15%; }
.talks-table th:nth-child(3), .talks-table td:nth-child(3) { width: 42%; }
.talks-table th:nth-child(4), .talks-table td:nth-child(4) { width: 15%; }
.talks-table th:nth-child(5), .talks-table td:nth-child(5) { width: 15%; }

/* Compact content styling */
.talks-table td {
  color: var(--table-text-primary);
}

.talks-table td strong {
  display: block;
  margin-bottom: 4px;
  font-weight: 600;
  color: var(--table-text-primary);
}

.talks-table td em {
  display: block;
  margin-bottom: 4px;
  font-size: 0.9em;
  font-style: italic;
  color: var(--table-text-secondary);
}

.talks-table td span {
  font-size: 0.85em;
  color: var(--table-text-secondary);
}

/* Links */
.talks-table a {
  color: var(--link-color);
  text-decoration: none;
  border-bottom: 1px dotted transparent;
  transition: all 0.2s ease;
}

.talks-table a:hover {
  color: var(--link-hover-color);
  border-bottom: 1px dotted var(--link-hover-color);
}

/* Type and Location columns styling - SIMPLE TEXT */
.talks-table td:nth-child(4), /* Location */
.talks-table td:nth-child(5) { /* Type */
  font-size: 0.85rem;
  color: var(--table-text-secondary);
}

/* Emoji styling */
.talks-table .emoji {
  font-size: 0.9em;
  margin-right: 4px;
}

/* ===== THEME TRANSITION ===== */
.talks-page * {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .talks-page h1 {
    font-size: 2rem;
    margin-bottom: 1.25rem;
  }
  
  .talks-page h2, .talks-page h3 {
    margin-top: 2rem;
    font-size: 1.5rem;
  }
  
  .talks-table {
    font-size: 0.85rem;
    display: block;
    overflow-x: auto;
  }
  
  .talks-table th, .talks-table td {
    padding: 10px 12px;
  }
  
  .talks-table th:nth-child(1), .talks-table td:nth-child(1) { width: 22%; }
  .talks-table th:nth-child(2), .talks-table td:nth-child(2) { width: 25%; }
  .talks-table th:nth-child(3), .talks-table td:nth-child(3) { width: 38%; }
  .talks-table th:nth-child(4), .talks-table td:nth-child(4) { width: 15%; }
  .talks-table th:nth-child(5), .talks-table td:nth-child(5) { width: 20%; }
}
</style>

<script>
// Theme-aware talks page
function updateTalksTheme() {
  const isDark = document.documentElement.classList.contains('dark') || 
                 document.documentElement.getAttribute('data-theme') === 'dark';
  
  const root = document.documentElement;
  
  if (isDark) {
    // Dark mode - override any light mode fallbacks
    root.style.setProperty('--page-title-color', '#ffffff');
    root.style.setProperty('--section-title-color', 'var(--color-primary-300, #f6dcdb)');
    root.style.setProperty('--table-border', 'var(--color-gray-600, #6c6660)');
    root.style.setProperty('--table-header-bg', 'rgba(var(--color-primary-900-rgb, 30 58 138), 0.3)');
    root.style.setProperty('--table-header-color', 'var(--color-primary-300, #f6dcdb)');
    root.style.setProperty('--table-row-bg-alt', 'rgba(var(--color-gray-950-rgb, 36 34 32), 0.2)');
    root.style.setProperty('--table-row-hover', 'rgba(var(--color-primary-700-rgb, 30 58 138), 0.3)');
    root.style.setProperty('--table-text-primary', 'var(--color-gray-300, #d6d4d2)');
    root.style.setProperty('--table-text-secondary', 'var(--color-gray-400, #9ca3af)');
    root.style.setProperty('--link-color', 'var(--color-primary-400, #60a5fa)');
    root.style.setProperty('--link-hover-color', 'var(--color-primary-300, #93c5fd)');
  } else {
    // Light mode
    root.style.setProperty('--page-title-color', 'var(--color-gray-900, #171717)');
    root.style.setProperty('--section-title-color', 'var(--color-primary-800, #935b59)');
    root.style.setProperty('--table-border', 'var(--color-gray-300, #d6d4d2)');
    root.style.setProperty('--table-header-bg', 'var(--color-primary-100, #f6dcdb)');
    root.style.setProperty('--table-header-color', 'var(--color-primary-800, #935b59)');
    root.style.setProperty('--table-row-bg-alt', 'var(--color-gray-50, #f8f7f7)');
    root.style.setProperty('--table-row-hover', 'rgba(var(--color-primary-100-rgb, 246 220 219), 0.3)');
    root.style.setProperty('--table-text-primary', 'var(--color-gray-800, #4e4a45)');
    root.style.setProperty('--table-text-secondary', 'var(--color-gray-600, #6c6660)');
    root.style.setProperty('--link-color', 'var(--color-primary-600, #cc7e7b)');
    root.style.setProperty('--link-hover-color', 'var(--color-primary-800, #935b59)');
  }
}

// Initial setup
document.addEventListener('DOMContentLoaded', function() {
  // Add talks-page class to body or main container
  const main = document.querySelector('main') || document.body;
  main.classList.add('talks-page');
  
  // Apply theme
  updateTalksTheme();
});

// Listen for theme changes
document.addEventListener('hbThemeChange', function() {
  setTimeout(updateTalksTheme, 50);
});

// Watch for theme changes
const observer = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    if (mutation.attributeName === 'class' || mutation.attributeName === 'data-theme') {
      setTimeout(updateTalksTheme, 50);
    }
  });
});
observer.observe(document.documentElement, { attributes: true });
</script>

<div class="talks-page">

### 📅 Upcoming Talks

<table class="talks-table">
<thead>
<tr>
<th>Date</th>
<th>Event</th>
<th>Title & Details</th>
<th>Location</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Feb 25–27, 2026</td>
<td>IZS 2026</td>
<td>
<strong>The Coded Coupons Collector's Problem</strong>
<em>D. Bar-Lev</em>
<span>🔗 <a href="https://www.izs.ethz.ch">Seminar</a></span>
</td>
<td>Zurich, Switzerland</td>
<td>Invited talk</td>
</tr>
</tbody>
</table>

### 📚 Past Talks

<table class="talks-table">
<thead>
<tr>
<th>Date</th>
<th>Event</th>
<th>Title & Details</th>
<th>Location</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mar 1–2, 2025</td>
<td>NVMW 2025</td>
<td>
<strong>Scalable and Robust DNA-based Storage via Coding Theory and Deep Learning</strong>
<em>D. Bar-Lev</em>
<span>🔗 <a href="http://nvmw.ucsd.edu">Workshop</a></span> · 
<span>📄 <a href="http://nvmw.ucsd.edu/nvmw2025-program/nvmw2025-final9.pdf">Abstract</a></span>
</td>
<td>Las Vegas, Nevada, USA</td>
<td>Oral presentation</td>
</tr>
<tr>
<td>Mar 1–2, 2025</td>
<td>NVMW 2025</td>
<td>
<strong>Cover Your Bases: How to Minimize the Sequencing Coverage in DNA Storage Systems</strong>
<em>D. Bar-Lev</em>
<span>🔗 <a href="http://nvmw.ucsd.edu">Workshop</a></span> · 
<span>📄 <a href="http://nvmw.ucsd.edu/nvmw2025-program/nvmw2025-final38.pdf">Abstract</a></span>
</td>
<td>Las Vegas, Nevada, USA</td>
<td>Oral presentation</td>
</tr>
<tr>
<td>Dec 15–20, 2024</td>
<td>Dagstuhl Seminar 2024</td>
<td>
<strong>Scalable and Robust DNA-based Storage via Coding Theory and Deep Learning</strong>
<em>D. Bar-Lev</em>
<span>🔗 <a href="https://www.dagstuhl.de/24511">Seminar</a></span>
</td>
<td>Dagstuhl, Germany</td>
<td>Oral presentation</td>
</tr>
<tr>
<td>Jul 7–12, 2024</td>
<td>ISIT 2024 Workshop</td>
<td>
<strong>Universal Framework for Parametric Constrained Coding</strong>
<em>D. Bar-Lev</em>
<span>🔗 <a href="https://2024.ieee-isit.org/workshops">Workshop</a></span>
</td>
<td>Athens, Greece</td>
<td>Plenary (15min)</td>
</tr>
<tr>
<td>Jun 25–30, 2023</td>
<td>ISIT 2023 Tutorial</td>
<td>
<strong>Coding and Algorithms for DNA Storage Systems</strong>
<em>D. Bar-Lev, O. Sabary, E. Yaakobi</em>
<span>🔗 <a href="https://2023.ieee-isit.org">ISIT 2023</a> · 📊 <a href="https://drive.google.com/file/d/1_P-aAYM_YWJ5AX5wfGXbQ-VQG71qNDyH/view">Slides</a></span>
</td>
<td>Taipei, Taiwan</td>
<td>Tutorial (3 hours)</td>
</tr>
<tr>
<td>May 17–19, 2023</td>
<td>London Calling 2023</td>
<td>
<strong>Cover Your Bases: How to Minimize the Sequencing Coverage in DNA Storage Systems</strong>
<em>D. Bar-Lev</em>
</td>
<td>London, England</td>
<td>Poster</td>
</tr>
<tr>
<td>Jun 22–24, 2022</td>
<td>Munich Workshop 2022</td>
<td>
<strong>Minimizing the Sequencing Coverage of DNA Storage Systems</strong>
<em>D. Bar-Lev</em>
</td>
<td>Munich, Germany</td>
<td>Poster</td>
</tr>
<tr>
<td>Mar 21–23, 2022</td>
<td>Data Storage in Molecular Media 2022</td>
<td>
<strong>Adversarial Torn-paper Codes</strong>
<em>D. Bar-Lev</em>
</td>
<td>Marburg, Germany (virtual)</td>
<td>Oral presentation</td>
</tr>
</tbody>
</table>

</div>