# LIC25 — End of Module Assignment

> **Due:** Monday, 19 October 2026, 11:55 PM

## Overview

This End of Module Assignment has two parts (Parts A and B, weighted at 40% each). Submit both parts by the end of Unit 12.

## Submission Ready Files

### Part A Files (`part_a/`):
- Modified source code: `part_a/bubsort2.c` (C program reading from CPUPI.txt; compiled and timed with MSVC 2022)
- Modified source code: `part_a/bubsort.py` (Python program reading from CPUPI.txt with efficient Timsort)
- Sorted data output: `part_a/sorted_data_full.txt` (all 838,861 values sorted into ascending order by the Python implementation)
- Evaluation report: `part_a/Part_A_Evaluation_Report.md` (approx. 3,000 words, with a populated results table for both languages)

### Part B Files (`part_b/`):
- Presentation deck: `part_b/Part_B_Presentation_Deck.pptx` (PowerPoint, 10 slides, in-slide citations + full Harvard reference list)
- Presentation outline: `part_b/Presentation_Slides.md`
- Presentation transcript: `part_b/Presentation_Transcript.md` (spoken content for the 15-minute recording)
- Human-authored research: `part_b/AI_Research_Notes.md`
- AI-generated response: `part_b/AI_Generated_Response.md` (clearly marked as AI-generated)
- Critical comparison: `part_b/AI_Human_vs_AI_Comparison.md`
- Bibliography: `part_b/AI_Sources_Bibliography.md` (18 sources, incl. 9 peer-reviewed)

All written components are ready for submission; the audio recording of the oral presentation remains to be produced (see roadmap). The roadmap below shows completed tasks.

| Part | Format | Weighting | Length |
| :--- | :----- | :-------- | :----- |
| **Part A** | Individual programming exercise — comparing programming languages | 40% | 3,000 words equivalent |
| **Part B** | Individual reflection presentation with Gen-AI comparison | 40% | 15-minute presentation (1,000 words equivalent) |

> Guidance on the use of AI, particularly within summative assessments, can be found in the *Student Information* area.

## Repository Layout

```
end_of_module_assignements/code/
├── readme.md                  - this brief + progress roadmap
├── SUMMARY.md                 - implementation summary
├── part_a/                    - Part A submission (self-contained; zip this folder)
│   ├── bubsort2.c             - modified C program (reads CPUPI.txt)
│   ├── bubsort.py             - modified Python program (efficient Timsort)
│   ├── CPUPI.txt              - data set to sort (838,861 values)
│   ├── sorted_data_full.txt   - sorted output (the submitted data file)
│   └── Part_A_Evaluation_Report.md
├── part_b/                    - Part B submission (self-contained; zip this folder)
│   ├── Part_B_Presentation_Deck.pptx
│   ├── slides/                - Reveal.js deck (open slides/index.html in a browser; S = speaker notes)
│   ├── Presentation_Slides.md
│   ├── Presentation_Transcript.md
│   ├── AI_Research_Notes.md
│   ├── AI_Generated_Response.md
│   ├── AI_Human_vs_AI_Comparison.md
│   └── AI_Sources_Bibliography.md
└── scratch/                   - working files only (not for submission; git-ignored)
```

Both programs locate `CPUPI.txt` next to their own source file, so they can be run from any working directory.

## How to Build and Run

**Python** (from any directory):

```
python part_a/bubsort.py
```

**C** with MSVC (from a Visual Studio Developer Command Prompt, any directory):

```
cl /O2 part_a\bubsort2.c /Fe:bubsort2.exe
bubsort2.exe          -> sorts the full data set
bubsort2.exe 100000   -> sorts the first 100,000 values (for timing)
```

**Presentation** (Reveal.js - no install, no server needed): double-click `part_b/slides/index.html`, then:

```
F11 / F5  = full screen          S = speaker view (your script + timings)
arrows    = navigate slides      ESC = overview mode (all slides as grid)
```

## Contents

- [Part A: Individual programming exercise](#part-a-individual-programming-exercise--comparing-programming-languages)
  - [Learning outcomes](#learning-outcomes)
  - [Tutor-provided scripts](#tutor-provided-scripts)
  - [Submission summary](#submission-summary)
  - [Table example](#table-example)
- [Part B: Individual reflection presentation with Gen-AI comparison](#part-b-individual-reflection-presentation-with-gen-ai-comparison)
  - [Learning outcomes](#learning-outcomes-1)
  - [Assessment brief](#assessment-brief)
  - [Tutor-specified presentation question](#tutor-specified-presentation-question)
  - [Notes on using Generative AI](#notes-on-using-generative-ai)
  - [Further instructions](#further-instructions)
- [Before you submit](#before-you-submit)
  - [Turnitin originality check](#turnitin-originality-check)
  - [Academic integrity and plagiarism](#academic-integrity-and-plagiarism)
  - [Word count](#word-count)
  - [Departmental guidelines on preparation and submission of coursework](#departmental-guidelines-on-preparation-and-submission-of-coursework)
  - [Submission instructions](#submission-instructions)

---

## Part A: Individual programming exercise – comparing programming languages

### Learning outcomes

- Critically evaluate appropriate methodologies, tools and techniques to mitigate and/or solve computing issues and their business impact.
- Articulate the legal, social, ethical, and professional issues faced by computing professionals.

**Title:** Evaluating the development models of two programming languages

In Part A of this assignment, you will explore two modern programming languages through basic code experimentation.

You will work with two tutor-provided scripts that perform a basic function (e.g. sorting a list). You will test, modify, and compare the scripts, then write a report evaluating your observations and reflecting on professional issues in programming.

### Tutor-provided scripts

You have been supplied with two source code files — one in Python and one in C — and a data file for you to sort. You will need to amend both code files.

| File | Language | Required change |
| :--- | :------- | :-------------- |
| `bubsort2.c` | C | Allow the program to read in the data file (`CPUPI.txt`) to provide it with data to sort. |
| `bubsort.py` | Python | Read in the same data file, **and** change the sorting algorithm to make the sort operation more efficient. |
| `CPUPI.txt` | Data | The data set to be sorted into ascending order. |

You will need to run both applications on your system to determine comparative timings — those given in the seminar are only applicable to my system, and may be different on yours.

The data file (`CPUPI.txt`) is a text file generated by calculating Pi to approximately a million decimal places, ensuring random distribution as much as possible. The numbers have been gathered into sets of 10 digits, meaning you have over 800,000 sets of numbers. These need to be sorted into ascending order.

You will also need a compiler to be able to translate your C source code into an executable — and there is an embarrassment of choices to do this.

#### Windows

The default programming environment for Windows is the `dotnet` suite — unfortunately `dotnet` is **NOT** a compiler — it "translates" code from various sources/languages into something called MSIL/CIL (common intermediate language) that runs on top of the `dotnet` engine — in effect it is a fancy interpreter. However, the full suite does include a C compiler in the form of Visual C/C++. The `dotnet` IDE (Visual Studio / Visual Studio Code) also works with TCC (see below). Look at *C and C++ in Visual Studio*.

#### Mac

The default programming environment on the Mac is Xcode — this is a nice environment, but it does take up a minimum of 40 GB of space, which is quite a lot just for this assessment.

#### Linux

If we use the system's proper name – GNU/Linux – then it is obvious what the default programming environment is: Gnu Compiler Collection, or GCC. Some distributions have GCC installed as standard, and it is easy to install it from the package manager — but some may see it as overkill just for an assessment. From an open-source perspective, there is also Clang which works (as default) on Linux and Mac OS. Both Clang and GCC are also available for Windows. TCC is another option (see below).

> **In summary:** if you have the default development environment installed for your platform, please feel free to use that to compile the C code. However, if you do not have those environments installed, please consider the options below.

#### Tiny C Compiler (TCC)

TCC is a small, cross-platform compiler that works on **all** platforms. However, the default repository is no longer available from the UK, which means that you must use alternative mechanisms to access it.

- **Windows:** look at the add-in for Visual Studio Code that allows you to use TCC on Windows (or Linux). Also, on Linux you can usually install TCC from the default package manager.
- **Mac:** unfortunately, Mac is the outlier. You can install TCC using Homebrew, but that doesn't work on the most recent versions of Mac OS, nor does it provide a native "Apple Silicon" version. An alternative that is available for all platforms is CodeLite.

### Submission summary

- Submit your modified source code (both C and Python) for the applications you used, together with a data file that contains the sorted data (knowledge and understanding, **30%**).
- Include a table populated with your results (see table example below).
- Include an explanation for why you selected the algorithm you did, why it sorts the data faster than some (all?) of the alternatives (hint: look at the big O discussion in the seminar).
- Answer the question — were you able to sort the data in Python faster than the compiled bubble sort in C? Did it work for all the data sizes listed?
- Ensure your submission is written in a language and style suitable for business applications, and that has been properly proofread and spell checked.
- Include suitable references, in the required UoE style (as a minimum I would expect that you provide a reference for the algorithm you eventually selected, as well as for the tools and compilers you used).

### Table example

### Results table (measured on this machine: Windows 11; MSVC 2022 v14.44 x64, `/O2`; Python 3.12.10)

| Data size | C bubble sort time | Python bubble sort time | Python sort time (Timsort) |
| ---------: | :------------------: | :----------------------: | :--------------------------: |
| 100 000 | 4.115 s (measured) | ~477 s (~8 min, extrapolated) | 0.0174 s (measured) |
| 200 000 | 36.211 s (measured) | ~1 910 s (~32 min, extrapolated) | 0.0393 s (measured) |
| 500 000 | 249.627 s (measured) | ~11 940 s (~3.3 h, extrapolated) | 0.1231 s (measured) |
| 800 000 | 645.251 s (measured) | ~30 600 s (~8.5 h, extrapolated) | ~0.23 s |
| 838 861 (full set) | 711.551 s (measured) | ~33 600 s (~9.3 h, extrapolated) | 0.2394 s (measured) |

> Values marked "~" are extrapolated from the measured quadratic growth of bubble sort; all other values are measured single runs. The Python bubble sort is extrapolated at large sizes because an 800 000-value O(n^2) run in the interpreter would take most of a day. Diagrams/charts can also be used to illustrate the answers if wished.

---

## Part B: Individual reflection presentation with Gen-AI comparison

### Learning outcomes

- Gather and synthesise information from multiple sources (including internet resources and business publications) to aid in the systematic design and analysis of computing challenges.
- Critically evaluate appropriate methodologies, tools and techniques to mitigate and/or solve computing issues and their business impact.
- Articulate the legal, social, ethical, and professional issues faced by computing professionals.

### Assessment brief

In Part B of the End of Module assignment, you will deliver a recorded presentation that critically evaluates one emerging computing technology, focussing on ethical and security challenges.

In this version of the assessment, you are encouraged to make active use of Generative AI tools (e.g. ChatGPT, Bard, Copilot) to support your preparation. You will:

- Research and develop your own human-authored response to the presentation question using academic and industry sources.
- Use a Generative AI tool to answer the same presentation question.
- Compare and critically evaluate the strengths and weaknesses of both approaches, human and AI-generated, as part of your presentation.

This task helps you explore both the context of the topic and the practical use of Generative AI in professional and academic contexts, in line with current workplace realities.

### Tutor-specified presentation question

> Emerging technologies such as AI, Quantum Computing, and Blockchain offer tremendous potential but also introduce significant ethical and security risks. Critically evaluate one of these technologies and discuss how enterprises can balance innovation with security and ethical considerations.

Your presentation should cover:

1. **Your research-based response**
   - Technical overview of the selected emerging technology.
   - Real-world enterprise applications.
   - Ethical and security concerns.
   - Regulatory and governance frameworks.
   - Use at least 6–8 academic or reputable industry sources.
2. **Generative AI response**
   - Present a summary of the output generated using a Generative AI tool (e.g. ChatGPT) when given the same brief.
   - You may include direct excerpts in your slides or transcript.
3. **Critical comparison**
   - Evaluate the strengths and limitations of the Generative AI response vs. your own.
   - Consider:
     - Accuracy and reliability of sources.
     - Depth and nuance of analysis.
     - Ethical issues (e.g. bias, transparency, hallucinations).
     - Professional appropriateness.
   - Reflect on how Generative AI can support (or hinder) professional computing work.

### Students should

Deliver a 15-minute presentation covering:

- The technical aspects, real-world applications, ethical concerns, and security risks of the chosen technology.
- Provide an in-depth analysis of regulatory and governance frameworks (e.g. GDPR for AI, NIST for Quantum Computing, Blockchain compliance standards).
- Use real-world case studies to illustrate key challenges and proposed solutions.
- Ensure proper referencing and use at least eight peer-reviewed sources.
- The presentation should consist of a PowerPoint deck of up to 10 slides.
- Please ensure that your citations and list of references are included in the slides and citations mentioned in your transcript.
- An audio recording and accompanying transcript.

> **Please note:** the maximum file upload size is 500 MB.

### Notes on using Generative AI

- You are permitted to use tools such as ChatGPT, Copilot, or similar to generate content for the purposes of comparison only.
- You must clearly indicate any content in your presentation that was AI-generated.
- Do not submit an AI-generated script as your own work, this will be treated as academic misconduct.
- This task allows you to evaluate how such tools work, not to rely on them fully.

### Further instructions

The presentation should include your demonstration. Your slides should not be wordy or repeat, verbatim, the oral presentation. Visuals, illustration, statistics, charts, tables and indication of key pointers are welcome. In assessing the presentation for marking, emphasis will be placed on the oral content. However, clarity of the visual presentation will also be considered.

It is strongly recommended that, to record your presentation, you use a headset with a microphone.

> **Please note:** Appendices should not be used to extend the report as reports should stand alone, complete and concise, without the appendices. They should only be used if required, and only for supplementary and/or supporting information. One key part of the assessment is the need to be to be able to express ideas succinctly, concisely and with necessary brevity.

---

## Roadmap and Progress Tracking

### Part A: Programming Exercise - Current Status
- [x] Environment setup and verification
- [x] Analyze tutor-provided files (bubsort2.c, bubsort.py, CPUPI.txt)
- [x] Modify bubsort2.c to read from CPUPI.txt
- [x] Test and validate C implementation (compiled with MSVC 2022; timed at all required sizes; verified SORTED OK)
- [x] Modify bubsort.py to read from CPUPI.txt
- [x] Implement more efficient sorting algorithm in Python (Timsort via list.sort())
- [x] Test and validate Python implementation (verified ascending; 838,861 values written)
- [x] Execute timing tests for different data sizes (C: 100k-800k measured; Python: all sizes measured)
- [x] Complete results table
- [x] Write evaluation report (approx. 3,000 words)
- [x] Prepare submission package

### Part B: Reflection Presentation - Current Status
- [x] Select emerging technology (AI, Quantum Computing, or Blockchain) - COMPLETED: Selected AI
- [x] Conduct human-authored research (6-8 sources) - COMPLETED (18 sources, 9 peer-reviewed)
- [x] Generate AI response using Generative AI tool - COMPLETED
- [x] Analyze both responses (human vs AI) - COMPLETED
- [x] Create presentation slides (up to 10 slides) - COMPLETED: outline + PowerPoint deck with in-slide citations and full Harvard reference list
- [x] Prepare 15-minute presentation content - COMPLETED: Presentation_Transcript.md
- [ ] Record presentation with headset and microphone - PENDING (demo + delivery)
- [ ] Final review and submission - PENDING

## Before you submit

### Turnitin originality check

Before submitting your assignment, it is important to check the originality of your work by submitting your assignment to Turnitin.

By submitting your assignment to this tool you will receive an originality report which can be used to check that you have not included other authors work without correct citation. It is important to note that submitting your work to the Turnitin Originality Check tool does not count as a submission of your final work. You must still submit your assignment below.

### Academic integrity and plagiarism

We take academic integrity very seriously. Academic integrity means acting with fairness and honesty, giving credit to others where you are referring to their ideas or research and respecting the work of others. Plagiarism is defined as: 'Using or copying the work of others (whether written, printed or in any other form) without proper acknowledgement'. Before you finalise your assignment take time to check that all your statements are backed up with supporting evidence, that all sources you use — whether referring to their ideas, quoting directly or paraphrasing — are correctly referenced in the text. Correct use of referencing acknowledges the academic whose work has informed yours, enables the reader to find the sources you have used and demonstrates your ability to find and analyse relevant information.

Failure to properly acknowledge the work of others is an academic offence and may result in your work incurring a penalty or, in the most serious cases, you being removed from the course for academic dishonesty.

If you are unsure about referencing or plagiarism there are useful resources available in the Study Skills Hub which is accessible from the menu on the left hand side. If you are still experiencing difficulties with academic integrity then you can contact the Study Skills Team for individualised support.

### Word count

> **Please note:** a word count penalty applies to this assessment.
>
> If your assessment exceeds the word count limit or range by more than 10% then your awarded grade will be reduced by 10% grade points. For more information please see your student handbook.

**Not meeting the word count:** There is no grade reduction applied if your assignment does not meet the word count range or limit, but to maximise your opportunity to achieve the highest grade possible, you should aim to meet the word count or range as closely as possible.

### Departmental guidelines on preparation and submission of coursework

- Assignments should be submitted in either MS Word or Open Office format unless stated otherwise on the assignment submission page.
- Use standard margins: 1" (2.5 cm) on all sides.
- Use standard Arial 12-point font size.
- Use double-line spacing.
- Pages should be numbered consecutively.
- Your work should be correctly referenced using the Harvard Referencing style.

### Submission instructions

- Please ensure that you do not include your name on your work, in line with the anonymous marking policy.
- Submit your saved documents below before the end of Unit 12.
- Zipped files are acceptable for submission.
- After the deadline, the submission page will be locked.
- If you need to apply for Late Submission, please complete the late submission of coursework form.
