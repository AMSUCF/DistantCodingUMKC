---
layout: default
---

## About This Guide

This guide walks through practical examples of using AI-assisted coding tools for digital humanities work. Each example demonstrates a real workflow -- from preparing source materials to generating a finished digital project -- using **Claude Code** connected to a GitHub repository.

These examples are designed for humanities researchers, graduate students, and faculty who want to explore what AI-assisted development looks like in practice, without requiring prior programming experience.

---

## Example 1: Building an ePortfolio from a CV

<div class="example-card" markdown="1">
<span class="tag">Beginner</span>

### From Word Document to Professional Website

This example demonstrates the most fundamental workflow: turning an existing document into a deployed website. Starting with a CV in `.docx` format, Claude Code reads the content, designs a site appropriate to the person's field, and builds it -- complete with responsive navigation, styled sections, and a downloadable link to the original document.

The result is a single-page ePortfolio with sections for publications, conference presentations, teaching, digital projects, awards, and education, all extracted directly from the CV content.

</div>

### Steps

<ol class="steps">
<li>

**Prepare a CV and any other materials** in Word or any other format. For this example, the CV was generated to represent a plausible digital humanities PhD candidate.

</li>
<li>

**Create a new repository on GitHub**, and use "Upload files" to add those documents to the repository.

</li>
<li>

**Open Claude and select Code.** This launches Claude Code, Anthropic's AI coding tool that can work directly with your GitHub repositories.

</li>
<li>

**Select the repository** after linking your GitHub account (which requires granting permissions for Claude to read and write to your repos).

</li>
<li>

**Use a prompt** to describe what you want. For this example, the prompt was:

<div class="prompt-block">
"this repository has a cv in it. build a fun but professional website appropriate to the type of work on the cv using the content from it. put the website and the cv document referenced into a subfolder, /eportfolio"
</div>

Claude reads the `.docx` file, identifies the person's field and research interests, and makes design decisions accordingly -- in this case, choosing an earthy green palette reflecting environmental humanities work, and adding a subtle pixel-art animation inspired by the candidate's work with Bitsy and electronic literature.

</li>
<li>

**Review and iterate.** Claude pushes the generated site to the repository. You can follow up with additional prompts to adjust the design, fix issues, or add features -- just as you would in conversation.

</li>
</ol>

### Sample Output

View the generated ePortfolio: **[Jordan M. Castillo -- ePortfolio](eportfolio/index.html)**

The source files are in the [`eportfolio/`](eportfolio/) subfolder of this repository, including the original CV document and the generated `index.html` and `style.css`.

---

## Example 2: Distant Reading a Text Corpus

<div class="example-card" markdown="1">
<span class="tag">Intermediate</span>

### Visualizing Word Distributions and Concordances

This example demonstrates a classic digital humanities workflow: distant reading. Starting with a set of plain-text files from Project Gutenberg -- all on the theme of technology and invention -- Claude Code preprocesses the texts, computes word frequency distributions, identifies key terms shared across the corpus, extracts keyword-in-context concordances, and builds an interactive web visualization.

The corpus includes four texts: *The Invention of the Sewing Machine* (1968), *The Telephone* (1877), *The Story of the Atlantic Telegraph* (1866), and *Printing Telegraphy... A New Era Begins* (1967).

</div>

### Steps

<ol class="steps">
<li>

**Gather source texts** in plain text format. For this example, four technology-related texts were downloaded from Project Gutenberg and uploaded to a `distantread/` subfolder in the repository.

</li>
<li>

**Open Claude Code** and select the repository, as in Example 1.

</li>
<li>

**Use a prompt** describing the analysis you want:

<div class="prompt-block">
"preprocess these texts (all of which are about technology) and create a web visualization comparing the word distribution of each (ignoring stop words) as well as the concordance of key terms appropriate across the set"
</div>

Claude writes a Python preprocessing script that strips Gutenberg boilerplate, tokenizes text, removes stop words, computes word frequencies, identifies key terms appearing across multiple texts, and extracts keyword-in-context concordances -- then outputs structured JSON. It then builds an interactive HTML/CSS/JS visualization that loads that data.

</li>
<li>

**Explore the results.** The visualization includes:
- **Corpus overview cards** showing word counts per text
- **Word frequency bar charts** for each text (toggling raw count vs. per-1,000-word normalization)
- **Key term comparison** with stacked bars showing each text's contribution
- **Concordance view** (keyword-in-context) for any selected term

</li>
</ol>

### Sample Output

View the visualization: **[Distant Reading: Technology Texts](distantread/index.html)**

The source files, preprocessing script (`preprocess.py`), and generated data (`data.json`) are all in the [`distantread/`](distantread/) subfolder.

---

## Example 3: Image Metadata and Slideshow from Photographs

<div class="example-card" markdown="1">
<span class="tag">Beginner</span>

### From Raw Photos to Accessible Slideshow

This example demonstrates a two-step workflow for working with images: first generating structured metadata (identification, alt text, and descriptive filenames), then building a presentation from that metadata. The source material is a set of personal photographs of Florida butterflies, uploaded as generic screenshots.

Claude Code analyzes each image visually, identifies the species, writes detailed descriptive alt text suitable for accessibility, renames the files to meaningful names, and then builds a themed reveal.js slideshow.

</div>

### Steps

<ol class="steps">
<li>

**Select a set of images** in need of metadata. Use images you have rights to -- personal photographs, public domain images, or Creative Commons materials. For this example, eight butterfly photographs from garden walks and hikes in Florida were uploaded as generic screenshots (e.g. `Screenshot 2026-03-12 122511.png`).

</li>
<li>

**Upload to a subfolder** in your GitHub repository. Here, the images were placed in an `images/` folder.

</li>
<li>

**Request identification, alt text, and renaming.** The prompt for this step was:

<div class="prompt-block">
"these images need to be analyzed. Create a file with detailed descriptive alt text for each image, and rename the image files to match the butterfly in each"
</div>

Claude examines each photograph, identifies the species (Spicebush Swallowtail, Eastern Tiger Swallowtail, Painted Lady, White Peacock, Monarch, Zebra Longwing, Ceraunus Blue, and Great Southern White), writes detailed alt text describing wing patterns, colors, posture, and surroundings, renames each file from its generic screenshot name, and saves all descriptions in a structured markdown file.

</li>
<li>

**Build a slideshow** from the processed images and metadata:

<div class="prompt-block">
"build a reveal.js slideshow with a Florida native plant inspired aesthetic featuring each of the butterflies, with the identification in the caption and the alt text beneath it"
</div>

Claude builds a reveal.js presentation with a custom color palette inspired by Florida native plants (live oak canopy shadow, saw palmetto green, coreopsis gold, sandy pine flatwoods cream), decorative frond-like corner borders, fade transitions, and each species displayed with its common name, scientific name, and full descriptive alt text panel.

</li>
</ol>

### Sample Output

View the slideshow: **[Florida Butterflies](images/index.html)**

The renamed images, alt text file (`alt-text.md`), and slideshow are all in the [`images/`](images/) subfolder.

---

*More examples coming soon.*
