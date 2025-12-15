---

reading_time: false

# These disable sidebars and table of contents
_build:
  list: never
toc: false
---

<style>

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
  /*display: none !important;*/
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

/* ===== TABLE STYLING ===== */
.talks-table {
  width: 100% !important;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.9rem;
  table-layout: fixed;
}

.talks-table th, .talks-table td {
  padding: 8px 12px;
  border-bottom: 1px solid ;
  vertical-align: top;
  text-align: left;
}

.talks-table th {
  font-weight: 800;
  white-space: nowrap;
}

/* Column widths */
.talks-table th:nth-child(1), .talks-table td:nth-child(1) { width: 13%; }
.talks-table th:nth-child(2), .talks-table td:nth-child(2) { width: 15%; }
.talks-table th:nth-child(3), .talks-table td:nth-child(3) { width: 42%; }
.talks-table th:nth-child(4), .talks-table td:nth-child(4) { width: 15%; }
.talks-table th:nth-child(5), .talks-table td:nth-child(5) { width: 15%; }

/* Compact content */
.talks-table td strong {
  display: block;
  margin-bottom: 3px;
}

.talks-table td em {
  display: block;
  margin-bottom: 3px;
  font-size: 0.9em;
}

.talks-table td span {
  font-size: 0.85em;
}

/* ===== PAGE TITLE AND HEADERS ===== */
/* Center the page title - target the h1 inside main */
main h1 {
  text-align: center !important;
  margin-bottom: 1.5rem !important;
}

/* Section headers */
h2, h3 {
  text-align: left !important;
  margin-top: 2rem !important;
  margin-bottom: 2rem !important;
}

/* ===== REMOVE ANY LEFTOVER MARGINS/PADDING ===== */
/* The table should now fill the entire prose container */
.prose .talks-table {
  margin-left: 0 !important;
  margin-right: 0 !important;
}

/* Mobile responsiveness */
@media (max-width: 700px) {
  .talks-table {
    font-size: 0.85rem;
    display: block;
    overflow-x: auto;
  }
  
  .talks-table th:nth-child(1), .talks-table td:nth-child(1) { width: 22%; }
  .talks-table th:nth-child(2), .talks-table td:nth-child(2) { width: 25%; }
  .talks-table th:nth-child(3), .talks-table td:nth-child(3) { width: 38%; }
  .talks-table th:nth-child(4), .talks-table td:nth-child(4) { width: 15%; }
  .talks-table th:nth-child(5), .talks-table td:nth-child(5) { width: 20%; }
}
</style>

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
<td><strong>Feb 25–27, 2026</strong></td>
<td>IZS 2026</td>
<td>
<strong>The Coded Coupons Collector’s Problem</strong>
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
<td><strong>Mar 1–2, 2025</strong></td>
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
<td><strong>Mar 1–2, 2025</strong></td>
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