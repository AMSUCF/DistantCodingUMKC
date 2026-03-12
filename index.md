---
layout: default
---

## About This Workshop

In this workshop, we'll be walking through pragmatic approaches to using agentic AI tools as assistants for digital humanities projects: this approach introduces [distant coding](https://dl.acm.org/doi/10.1007/978-3-032-12408-1_15), a method John Murray and I define as akin to distant reading, as it involves the manipulation of code and data at a distance. To follow along, you will need a subscription to Anthropic's Claude.

---

## Example 1: Building an ePortfolio from a CV

<div class="example-card" markdown="1">
<span class="tag">Beginner</span>

### From Word Document to Professional Website

This example demonstrates the most fundamental workflow: turning an existing document into a deployed website. Starting with a CV in `.docx` format, Claude Code reads the content, designs a site appropriate to the person's field, and builds it.

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

**Review and iterate.** Claude pushes the generated site to the repository. You can follow up with additional prompts to adjust the design, fix issues, or add features -- just as you would in conversation. To deploy the portfolio to the web, go to GitHub.com, commit the changes, and select Pages under settings - deploy from main branch.

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

**Gather source texts** in plain text format. For this example, five technology-related texts were downloaded from Project Gutenberg and uploaded to a `distantread/` subfolder in the repository. One source text was chosen to be misleading (it has no content) - Claude handles this by eliminating it from the dataset.

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

**Download and install Claude Code.** Visit the [Claude Code documentation](https://code.claude.com/docs/en/overview) and follow the installation instructions for your operating system. This is a command line or terminal tool, so you will need to install it from the terminal.

</li>
<li>

**Open a project through your command line.** Use Terminal on Mac, Command Prompt or PowerShell on Windows and navigate to a project folder -- ideally a GitHub repository you've already cloned or initialized: you can use GitHub Desktop options and select "open project in Terminal/Command Line" to do this directly.

```
cd ~/projects/my-dh-project
```

If you don't have a project folder yet, you can also create one and initialize a git repository from the command line if you have git installed:

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

**Install and activate the "superpowers" workflow** Once inside the Claude Code session, type `/plugin` and select the **superpowers** plugin. This [adds skills](https://github.com/obra/superpowers) to support planning and management of more complex projects. After installation, use the `/brainstorm` command to begin designing a project. Here's an example:

<div class="prompt-block">
/brainstorm I want to build a tool that takes my class video and creates excellent course captions using a local model to process. This tool should also detect filler words (um, uh, etc) and edit the video to remove them before finalize the captions.
</div>

The brainstorming mode will ask questions about architecture, scope, data sources, and implementation strategy before writing code. It will also break the project down into more manageable parts, and deploy subagents to handle tasks.

</li>
<li>

**Build iteratively.** After brainstorming, you can move directly into implementation. Claude Code on the desktop can:

- Create and edit files across your entire project
- Run build tools, linters, and test suites
- Install npm/pip/etc. dependencies
- Debug errors by reading stack traces and fixing code
- Commit and push to GitHub
- Iterate based on your feedback in real time

This is where the workflow shifts from single-prompt generation (as in Examples 1-3) to supervising a developer with direct access to the system.

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

The key difference from the web-based workflow is that Claude Code on the desktop can handle projects with many files, complex dependencies, and iterative development cycles.

---

## Example 5: Searching Your Research Library with the Zotero MCP

<div class="example-card" markdown="1">
<span class="tag">Advanced</span>

### Connecting Claude to Your Zotero Library

This example demonstrates how to extend Claude Code's capabilities by connecting it to external tools through the Model Context Protocol (MCP). Specifically, we connect Claude to [Zotero](https://www.zotero.org/) -- the open-source reference manager widely used in humanities research -- so that Claude can search your library semantically, extract annotations, retrieve full-text content, and work with your citations directly.

This requires Claude Code running on the desktop (see Example 4) and a local installation of Python and Zotero.

</div>

### Prerequisites

- **Claude Code** installed on your machine (see Example 4)
- **Python 3.10+** installed
- **Zotero 7+** installed and running, with the local API enabled:
  - In Zotero, go to Preferences and enable *"Allow other applications on this computer to communicate with Zotero"*
- Optional but recommended: the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin for enhanced annotation and citation export

### Steps

<ol class="steps">
<li>

**Install the Zotero MCP server.** You can do this yourself, or you can direct Claude Code to read the directions on the repository and install it for you. To install it yourself, open your terminal and install the [zotero-mcp](https://github.com/54yyyu/zotero-mcp) package. The recommended method uses `uv`, but `pip` or `pipx` also work:

```
uv tool install zotero-mcp-server
```

or:

```
pip install zotero-mcp-server
```

</li>
<li>

**Run the setup command.** This auto-configures the connection between the Zotero MCP server and Claude:

```
zotero-mcp setup
```

The setup wizard will ask whether to use the local Zotero API (recommended -- requires Zotero to be running) or the web API (requires an API key). It will also configure semantic search settings, including which embedding model to use. The default model (`all-MiniLM-L6-v2`) is free and runs locally.

</li>
<li>

**Build the semantic search database.** This indexes your Zotero library so Claude can perform AI-powered similarity searches, not just keyword matching:

```
zotero-mcp update-db
```

For a more thorough index that includes full-text content of PDFs (slower but much more useful for research queries):

```
zotero-mcp update-db --fulltext
```

</li>
<li>

**Launch Claude Code** and verify the connection. Start Claude Code in any project folder:

```
claude
```

Claude now has access to tools for searching your Zotero library, retrieving item metadata, reading annotations, extracting full text, and browsing collections. Try a research query:

<div class="prompt-block">
Search my Zotero library for papers about procedural rhetoric in video games. Summarize the key arguments across the top results and identify which ones discuss environmental themes.
</div>

</li>
<li>

**Explore what's possible.** With the Zotero MCP connected, you can ask Claude to:

- **Semantic search**: find papers related to a concept even if they don't use the exact keywords
- **Annotation review**: pull all your highlights and notes from a specific PDF
- **Literature mapping**: identify clusters of related work in your library
- **Citation export**: retrieve BibTeX entries for specific items
- **Research synthesis**: summarize findings across multiple papers on a topic
- **Gap analysis**: ask what's missing from your library on a given subject

</li>
</ol>

### Use Cases

Reference management is central to humanities scholarship, but libraries often grow large enough that researchers lose track of what they have. Semantic search means you can ask conceptual questions ("what do I have on affect theory and digital media?") rather than relying on exact keyword matches. 

The MCP architecture is also extensible -- the same pattern of connecting Claude to external tools works for databases, APIs, file systems, and other services. Zotero is one example, but it illustrates the broader principle of bringing domain-specific tools into the AI workflow.

