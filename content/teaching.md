---
type: "page"
reading_time: false
_build:
  list: never
toc: false
---

<div class="teaching-container">

<h1 class="page-title">Teaching Experience</h1>

<div class="course-list">
  
  <!-- Logic and Set Theory -->
  <div class="course-item">
    <div class="course-header">
      <div class="course-title-row">
        <h4 class="course-title">69 - Logic and Set Theory</h4>
      </div>
      <div class="course-institution">Reichman University</div>
      <div class="course-role">Lecturer</div>
      <div class="course-semester-row">
        <span class="course-semester">Spring 2024</span>
      </div>
      <span class="course-level undergraduate">Undergraduate</span>
    </div>
    <p class="course-description">
      Foundations of countable and uncountable infinite sets, propositional logic, and first-order logic.
    </p>
  </div>

  <!-- Coding Theory -->
  <div class="course-item">
    <div class="course-header">
      <div class="course-title-row">      
        <h4 class="course-title">3559 - Coding Theory</h4>
      </div>
      <div class="course-institution">Reichman University</div>
      <div class="course-role">Lecturer</div>
      <div class="course-semester-row">
        <span class="course-semester">Summer 2023</span>
      </div>
      <span class="course-level graduate">Graduate</span>
    </div>
    <p class="course-description">
      Channels, bounds, and linear codes (Hamming, BCH, Reed-Solomon) with applications in storage/communication
    </p>
  </div>

  <!-- Computational Models -->
  <div class="course-item">
    <div class="course-header">
      <div class="course-title-row">
        <h4 class="course-title">3699 - Computational Models</h4>
      </div>
      <div class="course-institution">Reichman University</div>
      <div class="course-role">Teaching Assistant</div>
      <div class="course-semester-row">
        <span class="course-semester">Spring 2023</span>
      </div>
      <span class="course-level undergraduate">Undergraduate</span>
    </div>
    <p class="course-description">
      Formal models of computation including finite automata, context-free languages, pushdown automaton, Turing machines, and fundamental concepts of computability theory.
    </p>
  </div>

  <!-- Coding and Algorithms for Memories -->
  <div class="course-item">
    <div class="course-header">
      <div class="course-title-row">
        <h4 class="course-title">02360379 - Coding and Algorithms for Memories</h4>
      </div>
      <div class="course-institution">Technion – Israel Institute of Technology</div>
      <div class="course-role">Head Teaching Assistant</div>
      <div class="course-semester-row">
        <span class="course-semester">Winter 2021, Winter 2022, Winter 2023</span>
      </div>
      <span class="course-level graduate">Graduate</span>
    </div>
    <p class="course-description">
      Advanced coding techniques for data management, non-volatile memories, RAID technologies and DNA-based data storage.
    </p>
  </div>

  <!-- Combinatorics -->
  <div class="course-item">
    <div class="course-header">
      <div class="course-title-row">
        <h4 class="course-title">02340141 - Combinatorics</h4>
      </div>
      <div class="course-institution">Technion – Israel Institute of Technology</div>
      <div class="course-role">Teaching Assistant & Head Teaching Assistant</div>
      <div class="course-semester-row">
        <span class="course-semester">Spring 2019, Winter 2020, Spring 2020, Winter 2021, Spring 2021, Winter 2024</span>
      </div>
      <span class="course-level undergraduate">Undergraduate</span>
    </div>
    <p class="course-description">
      Counting techniques, generating functions, and graph theory.
    </p>
  </div>

  <!-- C Language Programming -->
  <div class="course-item">
    <div class="course-header">
      <div class="course-title-row">
        <h4 class="course-title">02340114 / 02340117 - C Language Programming</h4>
      </div>
      <div class="course-institution">Technion – Israel Institute of Technology</div>
      <div class="course-role">Teaching Assistant</div>
      <div class="course-semester-row">
        <span class="course-semester">Winter 2019</span>
      </div>
      <span class="course-level undergraduate">Undergraduate</span>
    </div>
    <p class="course-description">
      Fundamental programming concepts in C language, including pointers, memory management, recursion and backtracking.
    </p>
  </div>

</div>

</div>

<script>
// Teaching page theme handler - SIMPLE AND CLEAN
function updateTeachingTheme() {
  const isDark = document.documentElement.classList.contains('dark') || 
                 document.documentElement.getAttribute('data-theme') === 'dark';
  
  // Get computed styles to check what variables are available
  const rootStyles = getComputedStyle(document.documentElement);
  
  // Get theme variables
  const primary800 = rootStyles.getPropertyValue('--color-primary-800').trim();
  const primary600 = rootStyles.getPropertyValue('--color-primary-600').trim();
  const primary400 = rootStyles.getPropertyValue('--color-primary-400').trim();
  const primary200 = rootStyles.getPropertyValue('--color-primary-200').trim();
  const gray300 = rootStyles.getPropertyValue('--color-gray-300').trim();
  const gray600 = rootStyles.getPropertyValue('--color-gray-600').trim();
  const gray800 = rootStyles.getPropertyValue('--color-gray-800').trim();
  const gray900 = rootStyles.getPropertyValue('--color-gray-900').trim() || '#171717';
  
  // Apply styles based on mode
  const pageTitle = document.querySelector('.page-title');
  const items = document.querySelectorAll('.course-item');
  const titles = document.querySelectorAll('.course-title');
  const titleCodes = document.querySelectorAll('.course-title-row .course-code');
  const institutions = document.querySelectorAll('.course-institution');
  const roles = document.querySelectorAll('.course-role');
  const descriptions = document.querySelectorAll('.course-description');
  const semesters = document.querySelectorAll('.course-semester');
  const gradLevels = document.querySelectorAll('.course-level.graduate');
  const undergradLevels = document.querySelectorAll('.course-level.undergraduate');
  
  if (isDark) {
    // DARK MODE - use light colors on dark background
    if (pageTitle) pageTitle.style.color = '#ffffff';
    
    items.forEach(el => {
      el.style.borderLeftColor = gray600;
      el.style.backgroundColor = 'rgba(var(--color-gray-950-rgb, 36 34 32), 0.1)';
    });
    
    titles.forEach(el => el.style.color = primary400);
    titleCodes.forEach(el => el.style.color = primary400);
    institutions.forEach(el => el.style.color = primary200);
    roles.forEach(el => el.style.color = gray300);
    descriptions.forEach(el => el.style.color = gray300);
    semesters.forEach(el => el.style.color = gray300);
    
    gradLevels.forEach(el => {
      el.style.backgroundColor = 'rgba(var(--hb-secondary-950-rgb, 54 69 64), 0.3)';
      el.style.color = 'rgb(var(--color-secondary-300, 232 248 242))';
      el.style.borderColor = 'rgb(var(--color-secondary-800, 117 151 139))';
    });
    
    undergradLevels.forEach(el => {
      el.style.backgroundColor = 'rgba(var(--hb-secondary-950-rgb, 54 69 64), 0.3)';
      el.style.color = 'rgb(var(--color-secondary-300, 232 248 242))';
      el.style.borderColor = 'rgb(var(--color-secondary-800, 117 151 139))';
    });
  } else {
    // LIGHT MODE - use dark colors on light background
    if (pageTitle) pageTitle.style.color = gray900;
    
    items.forEach(el => {
      el.style.borderLeftColor = gray300;
      el.style.backgroundColor = 'rgba(var(--color-gray-50-rgb, 248 247 247), 0.1)';
    });
    
    titles.forEach(el => el.style.color = primary800);
    titleCodes.forEach(el => el.style.color = primary800);
    institutions.forEach(el => el.style.color = primary600);
    roles.forEach(el => el.style.color = gray600);
    descriptions.forEach(el => el.style.color = gray800);
    semesters.forEach(el => el.style.color = gray600);
    
    gradLevels.forEach(el => {
      el.style.backgroundColor = 'rgba(var(--color-secondary-100-rgb, 247 252 250), 0.5)';
      el.style.color = 'rgb(var(--color-secondary-800, 117 151 139))';
      el.style.borderColor = 'rgb(var(--color-secondary-300, 232 248 242))';
    });
    
    undergradLevels.forEach(el => {
      el.style.backgroundColor = 'rgba(var(--color-secondary-100-rgb, 247 252 250), 0.5)';
      el.style.color = 'rgb(var(--color-secondary-800, 117 151 139))';
      el.style.borderColor = 'rgb(var(--color-secondary-300, 232 248 242))';
    });
  }
}

// Initial setup
document.addEventListener('DOMContentLoaded', updateTeachingTheme);

// Listen for Hugo Blox theme changes
document.addEventListener('hbThemeChange', function() {
  setTimeout(updateTeachingTheme, 50);
});

// Also watch for class changes
const observer = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    if (mutation.attributeName === 'class' || mutation.attributeName === 'data-theme') {
      setTimeout(updateTeachingTheme, 50);
    }
  });
});
observer.observe(document.documentElement, { attributes: true });
</script>

<style>
/* Base structure styles */
.teaching-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 1rem;
}

.page-title {
  text-align: center;
  margin-bottom: 3rem;
  font-weight: 700;
  font-size: 2.5rem;
  transition: color 0.3s ease;
}

.course-list {
  margin-top: 2rem;
}

.course-item {
  border-left: 3px solid;
  padding: 2rem 0 2rem 2rem;
  margin-bottom: 2rem;
  transition: all 0.2s ease;
  border-radius: 0 12px 12px 0;
}

.course-item:hover {
  padding-left: 2.5rem;
  transform: translateX(5px);
}

.course-header {
  margin-bottom: 1rem;
  position: relative;
  min-height: 60px; /* Ensure enough height for the level badge */
}

.course-institution {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  letter-spacing: 0.5px;
}

.course-role {
  font-size: 0.9rem;
  font-style: italic;
  margin-bottom: 0.5rem;
}

.course-title-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.25rem;
  flex-wrap: wrap;
  max-width: calc(100% - 30px); /* Leave space for level badge */
}

.course-title {
  margin: 0;
  font-weight: 700;
  font-size: 1.4rem;
  line-height: 1.3;
  flex-grow: 1;
}

.course-level {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  padding: 0.4rem 1.2rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  border: 1px solid transparent;
  letter-spacing: 0.3px;
  text-align: center;
  min-width: 100px;
  margin: 0;
}

.course-semester-row {
  margin-bottom: 0.75rem;
}

.course-semester {
  font-style: italic;
  font-size: 0.95rem;
}

.course-description {
  margin: 0;
  line-height: 1.7;
  font-size: 1rem;
  max-width: 90%;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .teaching-container {
    padding: 0 1rem;
  }
  
  .page-title {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  
  .course-item {
    padding: 1.5rem 0 1.5rem 1.5rem;
    margin-bottom: 1.5rem;
  }
  
  .course-item:hover {
    padding-left: 2rem;
  }
  
  .course-title {
    font-size: 1.25rem;
  }
  
  .course-title-row {
    max-width: 100%;
    gap: 0.5rem;
  }
  
  .course-header {
    padding-right: 0;
    min-height: auto;
  }
  
  .course-level {
    position: static;
    transform: none;
    margin-top: 0.75rem;
    margin-bottom: 0.75rem;
    min-width: auto;
    width: fit-content;
  }
  
  .course-description {
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .course-item {
    padding: 1.25rem 0 1.25rem 1.25rem;
  }
  
  .course-title {
    font-size: 1.15rem;
  }
}


/* Ensure proper color transitions */
.course-item,
.course-title,
.course-institution,
.course-description,
.course-code,
.course-level,
.course-semester {
  transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
}

.max-w-prose {
  display: none;
}
</style>