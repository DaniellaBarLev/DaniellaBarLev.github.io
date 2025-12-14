#!/usr/bin/env python3
"""
HUGO PUBLICATIONS IMPORTER - Preserves original BibTeX
Fixes: DOI errors, creates index.md + original cite.bib
"""

import os
import re
import yaml
import shutil
import bibtexparser
from datetime import datetime
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def clean_doi_for_yaml(doi):
    """Clean DOI for YAML frontmatter ONLY - remove ALL URL prefixes."""
    if not doi:
        return ''
    
    # Remove EVERY possible URL prefix
    doi_str = str(doi)
    patterns = [
        'http://dx.doi.org/', 'https://dx.doi.org/',
        'http://doi.org/', 'https://doi.org/',
        'dx.doi.org/', 'doi.org/', 'http://', 'https://'
    ]
    
    for pattern in patterns:
        if doi_str.startswith(pattern):
            doi_str = doi_str[len(pattern):]
    
    return doi_str.strip()

def format_authors_for_yaml(authors_bibtex):
    """Convert BibTeX authors to YAML format 'Last, F.' for index.md."""
    if not authors_bibtex:
        return []
    
    authors_list = []
    # Split by BibTeX ' and ' separator
    raw_authors = [a.strip() for a in authors_bibtex.split(' and ')]
    
    for author in raw_authors:
        # Remove BibTeX braces
        author = author.replace('{', '').replace('}', '')
        
        if ',' in author:
            # Format: "Last, First" -> "Last, F."
            parts = author.split(',', 1)
            last = parts[0].strip()
            first = parts[1].strip() if len(parts) > 1 else ''
            
            if first:
                first_initial = first[0].upper()
                authors_list.append(f"{last}, {first_initial}.")
            else:
                authors_list.append(f"{last},")
        else:
            # Format: "First Last" -> "Last, F."
            parts = author.split()
            if len(parts) >= 2:
                last = parts[-1]
                first = parts[0]
                authors_list.append(f"{last}, {first[0].upper()}.")
            else:
                authors_list.append(author)
    
    return authors_list

def determine_publication_type(entry):
    """Determine if journal or conference based on entry type and venue."""
    entry_type = entry.get('ENTRYTYPE', '').lower()
    
    # 1. Check entry type first
    if entry_type == 'article':
        return "article-journal"
    elif entry_type in ['inproceedings', 'conference']:
        return "paper-conference"
    
    # 2. Check venue keywords
    venue = ''
    if 'journal' in entry:
        venue = entry['journal'].lower()
    elif 'booktitle' in entry:
        venue = entry['booktitle'].lower()
    
    # Conference indicators (case-insensitive)
    conference_keywords = [
        'conference', 'symposium', 'workshop', 'proceedings',
        'proc.', 'isit', 'itw', 'infocom', 'globecom', 'sigcomm',
        'meeting', 'annual', 'international'
    ]
    
    # Journal indicators
    journal_keywords = [
        'journal', 'transactions', 'letters', 'magazine',
        'review', 'annals', 'bulletin', 'proceedings of the ieee'
    ]
    
    # Check for conference keywords
    for keyword in conference_keywords:
        if keyword in venue:
            return "paper-conference"
    
    # Check for journal keywords
    for keyword in journal_keywords:
        if keyword in venue:
            return "article-journal"
    
    # 3. Default based on fields present
    if 'journal' in entry:
        return "article-journal"
    elif 'booktitle' in entry:
        return "paper-conference"
    
    # Final fallback
    return "article-journal"

def create_slug(title, first_author, year):
    """Create folder name from paper info."""
    # Extract first author's last name
    if not first_author:
        author_part = 'paper'
    elif ',' in first_author:
        author_part = first_author.split(',')[0].strip().lower()
    else:
        author_part = first_author.split()[0].lower()
    
    # Clean author name
    author_part = re.sub(r'[^\w\s-]', '', author_part)
    author_part = re.sub(r'[-\s]+', '-', author_part).strip('-')
    
    # Clean title
    title_clean = re.sub(r'[^\w\s-]', '', title.lower())
    title_clean = re.sub(r'[-\s]+', '-', title_clean).strip('-')
    
    # Take first few words
    title_words = title_clean.split('-')[:3]
    title_part = '-'.join(title_words)
    
    # Build slug
    slug = f"{author_part}-{year}-{title_part}"
    return slug[:70].rstrip('-')

def create_single_bib_entry(entry):
    """Create a .bib file with ONLY this entry (original BibTeX)."""
    # Create a new database with just this entry
    db = BibDatabase()
    db.entries = [entry]
    
    # Write with original formatting
    writer = BibTexWriter()
    writer.indent = '  '
    writer.comma_first = False
    
    return writer.write(db)

def create_publication_folder(entry, output_dir):
    """Create folder with index.md and cite.bib."""
    
    # Get basic info
    title = entry.get('title', 'Untitled').strip('{}')
    year = entry.get('year', '2023')
    
    # Format authors for YAML
    authors_yaml = format_authors_for_yaml(entry.get('author', ''))
    first_author = authors_yaml[0] if authors_yaml else ''
    
    # Create slug and folder
    slug = create_slug(title, first_author, year)
    folder_path = os.path.join(output_dir, slug)
    os.makedirs(folder_path, exist_ok=True)
    
    # Determine publication type
    pub_type = determine_publication_type(entry)
    
    # Get publication venue
    publication = ''
    if 'journal' in entry:
        publication = entry['journal']
    elif 'booktitle' in entry:
        publication = entry['booktitle']
    
    # ========== CREATE index.md ==========
    frontmatter = {
        'title': title,
        'authors': authors_yaml,
        'date': f"{year}-01-01",
        'publication_types': [pub_type],
    }
    
    if publication:
        frontmatter['publication'] = publication
    
    # Add DOI (CLEANED for YAML - NO URL!)
    if 'doi' in entry:
        cleaned_doi = clean_doi_for_yaml(entry['doi'])
        if cleaned_doi:
            frontmatter['doi'] = cleaned_doi
    
    # Add PDF URL if present and not a DOI URL
    if 'url' in entry:
        url = entry['url']
        # Check if it's a DOI URL
        if 'doi.org' not in url:
            frontmatter['url_pdf'] = url
    elif 'link' in entry:
        url = entry['link']
        if 'doi.org' not in url:
            frontmatter['url_pdf'] = url
    
    # Add optional fields
    optional = ['abstract', 'volume', 'number', 'pages']
    for field in optional:
        if field in entry and entry[field]:
            frontmatter[field] = entry[field]
    
    # Write index.md
    with open(os.path.join(folder_path, 'index.md'), 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True))
        f.write('---\n\n')
        
        if 'abstract' not in entry:
            f.write('<!-- Add abstract here if needed -->\n')
    
    # ========== CREATE cite.bib ==========
    # Write ORIGINAL BibTeX entry (unchanged!)
    bib_content = create_single_bib_entry(entry)
    with open(os.path.join(folder_path, 'cite.bib'), 'w', encoding='utf-8') as f:
        f.write(bib_content)
    
    return slug, pub_type

def main():
    """Main import function."""
    
    # Configuration
    PROJECT_ROOT = os.getcwd()
    BIB_FILE = os.path.join(PROJECT_ROOT, 'my-publications.bib')
    OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'content', 'publications')
    BACKUP_DIR = os.path.join(PROJECT_ROOT, 'backups')
    
    print("=" * 70)
    print("HUGO PUBLICATION IMPORTER - PRESERVES ORIGINAL BIBTEX")
    print("=" * 70)
    
    # Check input file
    if not os.path.exists(BIB_FILE):
        print(f"❌ ERROR: BibTeX file not found: {BIB_FILE}")
        print(f"Please place your file in: {PROJECT_ROOT}/")
        return
    
    # Backup existing folder
    if os.path.exists(OUTPUT_DIR):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(BACKUP_DIR, f"publications_{timestamp}")
        os.makedirs(BACKUP_DIR, exist_ok=True)
        shutil.move(OUTPUT_DIR, backup_dir)
        print(f"📦 Backed up existing to: {backup_dir}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Parse BibTeX
    print(f"\n📖 Reading BibTeX file: {os.path.basename(BIB_FILE)}")
    try:
        parser = BibTexParser(common_strings=True)
        with open(BIB_FILE, 'r', encoding='utf-8') as f:
            bib_db = bibtexparser.load(f, parser=parser)
        
        entries = bib_db.entries
        print(f"📊 Found {len(entries)} publications")
        
    except Exception as e:
        print(f"❌ Failed to parse BibTeX: {e}")
        return
    
    # Process each entry
    print("\n🔄 Processing...")
    stats = {'journal': 0, 'conference': 0, 'other': 0, 'errors': 0}
    
    for i, entry in enumerate(entries, 1):
        try:
            # Extract key fields for display
            title = entry.get('title', 'Untitled')[:40].strip('{}')
            
            # Create publication folder
            slug, pub_type = create_publication_folder(entry, OUTPUT_DIR)
            
            # Update statistics
            if pub_type == "article-journal":
                stats['journal'] += 1
                type_icon = "📄"
            elif pub_type == "paper-conference":
                stats['conference'] += 1
                type_icon = "🎤"
            else:
                stats['other'] += 1
                type_icon = "❓"
            
            print(f"  [{i:3d}] {type_icon} {slug}")
            
        except Exception as e:
            stats['errors'] += 1
            title = entry.get('title', 'Untitled')[:40].strip('{}')
            print(f"  [{i:3d}] ❌ {title}... - ERROR: {str(e)[:50]}")
    
    # ========== FINAL REPORT ==========
    print("\n" + "=" * 70)
    print("✅ IMPORT COMPLETE")
    print("=" * 70)
    
    print(f"\n📊 STATISTICS:")
    print(f"   Journal Articles:     {stats['journal']}")
    print(f"   Conference Papers:    {stats['conference']}")
    print(f"   Other/Unknown:        {stats['other']}")
    print(f"   Errors:               {stats['errors']}")
    
    # Verify folder structure
    print(f"\n🔍 FOLDER STRUCTURE (first 3):")
    sample_folders = sorted(os.listdir(OUTPUT_DIR))[:3]
    
    for folder in sample_folders:
        folder_path = os.path.join(OUTPUT_DIR, folder)
        
        # Check files exist
        index_file = os.path.join(folder_path, 'index.md')
        bib_file = os.path.join(folder_path, 'cite.bib')
        
        has_index = os.path.exists(index_file)
        has_bib = os.path.exists(bib_file)
        
        print(f"\n   📁 {folder}/")
        print(f"     ✓ index.md: {'YES' if has_index else 'NO'}")
        print(f"     ✓ cite.bib: {'YES' if has_bib else 'NO'}")
        
        # Check DOI in index.md
        if has_index:
            with open(index_file, 'r') as f:
                content = f.read()
                for line in content.split('\n'):
                    if 'doi:' in line:
                        print(f"     DOI in YAML: {line.strip()}")
                        break
                    if 'url_pdf:' in line:
                        print(f"     url_pdf: {line.strip()}")
    
    # Check publication types
    print(f"\n🔍 PUBLICATION TYPE DISTRIBUTION:")
    type_counts = {}
    for folder in os.listdir(OUTPUT_DIR):
        index_file = os.path.join(OUTPUT_DIR, folder, 'index.md')
        if os.path.exists(index_file):
            with open(index_file, 'r') as f:
                content = f.read()
                if 'article-journal' in content:
                    type_counts['journal'] = type_counts.get('journal', 0) + 1
                elif 'paper-conference' in content:
                    type_counts['conference'] = type_counts.get('conference', 0) + 1
                else:
                    type_counts['other'] = type_counts.get('other', 0) + 1
    
    print(f"   Journals: {type_counts.get('journal', 0)}")
    print(f"   Conferences: {type_counts.get('conference', 0)}")
    
    # ========== FINAL INSTRUCTIONS ==========
    print(f"\n🎯 NEXT STEPS:")
    print(f"   1. Clear Hugo cache:")
    print(f"      rm -rf public resources")
    print(f"      hugo --gc")
    print(f"   2. Start Hugo server:")
    print(f"      hugo server --disableFastRender")
    print(f"   3. Check publications page:")
    print(f"      http://localhost:1313/publications/")
    print(f"   4. Verify:")
    print(f"      - Authors display as 'D. Bar-Lev' (IEEE style)")
    print(f"      - Journals/Conferences are separated")
    print(f"      - No DOI errors in terminal")
    
    # Fix template reminder
    print(f"\n⚠️  REMINDER: Your template at layouts/section/publications.html")
    print(f"   should filter publications using:")
    print(f"   {{ $journals := where .Pages \".Params.publication_types\" \"intersect\" (slice \"article-journal\") }}")
    print(f"   {{ $conferences := where .Pages \".Params.publication_types\" \"intersect\" (slice \"paper-conference\") }}")
    
    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()