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

## Example 4: Complex Projects with Claude Code on the Desktop

<div class="example-card" markdown="1">
<span class="tag">Advanced</span>

### From Terminal to Full-Stack Projects

The previous examples used Claude Code through the web interface, which connects to a GitHub repository remotely. For more complex, iterative projects -- building full applications, working with local files, running tests, installing dependencies -- you can install Claude Code directly on your machine and run it from the command line.

This opens up significantly more capability: Claude can read and write files across your entire project, run shell commands, install packages, execute scripts, and iterate on errors in real time. Combined with brainstorming tools, this becomes a powerful environment for designing and building ambitious digital humanities projects from scratch.

</div>

### Steps

<ol class="steps">
<li>

**Download and install Claude Code.** Visit [claude.ai/code](https://claude.ai/code) and follow the installation instructions for your operating system. This requires Node.js (v18+). On most systems, you can install it with:

```
npm install -g @anthropic-ai/claude-code
```

</li>
<li>

**Open your terminal** (Terminal on Mac, Command Prompt or PowerShell on Windows) and navigate to a project folder -- ideally a GitHub repository you've already cloned or initialized:

```
cd ~/projects/my-dh-project
```

If you don't have a project folder yet, create one and initialize a git repository:

```
mkdir my-dh-project && cd my-dh-project && git init
```

</li>
<li>

**Launch Claude Code** by typing `claude` in that folder. Claude will start an interactive session with full access to your project directory. On first launch, you'll authenticate with your Anthropic account.

```
claude
```

</li>
<li>

**Activate the brainstorming plugin.** Once inside the Claude Code session, type `/install` and select the **superpowers** plugin. This adds extended capabilities for project planning and brainstorming. After installation, use the `/brainstorm` command to begin designing a project collaboratively:

<div class="prompt-block">
/brainstorm I want to build an interactive timeline of women in computing from Ada Lovelace to the present, with primary source excerpts, portraits, and a network visualization showing mentorship and collaboration connections between figures
</div>

The brainstorming mode helps you think through architecture, scope, data sources, and implementation strategy before writing code. Claude will ask clarifying questions, suggest approaches, identify potential challenges, and help you break an ambitious idea into manageable pieces.

</li>
<li>

**Build iteratively.** After brainstorming, you can move directly into implementation. Claude Code on the desktop can:

- Create and edit files across your entire project
- Run build tools, linters, and test suites
- Install npm/pip/etc. dependencies
- Debug errors by reading stack traces and fixing code
- Commit and push to GitHub
- Iterate based on your feedback in real time

This is where the workflow shifts from single-prompt generation (as in Examples 1-3) to an ongoing collaborative development process -- closer to pair programming than to filling out a form.

</li>
</ol>

### What You Can Build

With Claude Code on the desktop and brainstorming tools, the scope of possible projects expands significantly. Some examples relevant to digital humanities:

- **Interactive archives** with search, filtering, and metadata visualization
- **Mapping projects** combining GIS data with narrative and primary sources
- **Network visualizations** of historical correspondence, citation patterns, or social connections
- **Custom text analysis tools** with NLP pipelines tailored to specific corpora
- **Digital exhibits** with multimedia, timelines, and curatorial commentary
- **Pedagogical tools** -- interactive exercises, annotation platforms, or game-based learning environments

The key difference from the web-based workflow is that Claude Code on the desktop can handle projects with many files, complex dependencies, and iterative development cycles -- the kind of work that typically requires a dedicated developer.

---

*More examples coming soon.*
