# Reproducibility review — Lab 4

- Reviewers: Nasma Drissi and Ronald Sim
- Repository: https://github.com/Antetokounpo/corset-correction
- Review date: 3 November 2026
- Operating system: Windows 11
- uv version: 0.13.7
- Tested commit: 7252d310c6616dd07e82c5d5c2c6674ba9628d78

## AI usage

AI assistance included explanations of commands and installation support.

I also used ChatGPT to help commit the checklist, set up the origin and upstream remotes, and push my branch to my fork. It helped me handle repeated “Deletion of directory failed” prompts by stopping the command and checking the remotes before continuing. I ran the commands myself in PowerShell.

## Code of Conduct

- [x] The repository contains a Code of Conduct.
- [x] I have read it and will follow it.

## General checks

- [x] The source code is publicly available.
- [x] An open-source license is provided.
- [x] Instructions for citing the project are provided.
- [x] The repository structure is clear.
- [x] The README explains the project and installation.
- [x] Research artifacts are openly available.

## Reproducibility

- [x] Required dependencies are documented.
- [x] Core functionality is documented.
- [x] Example commands are provided.
- [x] The documented commands execute successfully.
- [x] The software produces the expected outputs.
- [x] Performance claims are verified, or none are made.
- [x] Results can be reproduced using only the repository instructions.

### Commands executed

>`uv sync`

>`uv run download-data`

>`uv run preprocess-data`

>`uv run analyze-data`

### Execution notes

The commands completed without errors after installing uv and
running them from the corset-correction directory.

Downloaded files:
- data/raw/P2_donnees.tab
- data/raw/README.md
- data/raw/dataset_selection_report.md

Generated outputs:
- results/regression_results.csv
- figures/pression_vs_tension.png
- figures/cobb_vs_tension.png

### Comparison notes

I opened the report and terminal side by side to compare the values
in the three tables, taking rounding into account.

I visually compared the generated figures with those in the report
and found them similar.

These checks concern execution and agreement of outputs.
I have not yet assessed the scientific interpretations.

## Open-source development history

- [x] Public and iterative development is visible through issues,
      pull requests and commits.

## Community guidelines

- [x] Contribution instructions are provided.
- [x] Instructions for reporting problems are provided.
- [ ] Instructions for requesting support are provided.

## Issues and contributions

- Issues:
    
    - [Issue #18](https://github.com/Antetokounpo/corset-correction/issues/18) : Adding uv installation steps for Windows: The problem 
    
      >`The term 'uv' is not recognized as the name of a cmdlet, function, script file, or operable program.`
      
      was encountered after installing `uv` and running the command `uv sync`. The fix was printed in the terminal after installation, but mentioning it in the README could
      be useful for users relying entirely on the README's instructions and might miss the instructions printed in the terminal.
    - [Issue #20](https://github.com/Antetokounpo/corset-correction/issues/20) : Instructions for requesting support are not explicitly provided. The repo lists
    administrator email addresses for reporting violations of community guidelines in `CODE_DE_CONDUITE.md`, and guidelines to raise an Issue on GitHub in
    `CONTRIBUTIONS.md`. However, there are no explicit guidelines for users looking for technical support.
- Pull requests:
    - [PR #17](https://github.com/Antetokounpo/corset-correction/pull/17) : Add reproducibility review checklist
    - [PR #19](https://github.com/Antetokounpo/corset-correction/pull/19) : Document uv installation on Windows
    - [PR #21](https://github.com/Antetokounpo/corset-correction/pull/21) : Add support section to README
 

## Final assessment

Overall, the repository is well organized and provides easy-to-follow instructions. The project is reproducible, with only minor improvements needed in the documentation. These improvements have been documented in GitHub Issues, and proposed changes have been submitted through pull requests.
