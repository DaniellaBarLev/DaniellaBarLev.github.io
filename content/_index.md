---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '2rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: |
        Hi, I’m Daniella, a postdoctoral researcher passionate about building the future of secure data storage.
        My work sits at the intersection of theory and practice, designing coding schemes and algorithms for reliable, high-density **DNA-based storage and cryptography systems**. I enjoy tackling hard problems in **coding theory** and **combinatorics** to solve real-world challenges.

        Please reach out if you’re interested in collaborating on the future of storage, coding theory, or algorithms! 😃
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf

    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: compact # Options: compact (long names), balanced (default), display (short names)

      # Avatar customization
      avatar:
        size: small # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded

      spacing:
        padding: ['0rem', '2rem', '0rem', '0rem']

---
