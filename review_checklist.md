# Reproducibility review — Lab 4

- Reviewer: Nasma Drissi
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

- [ ] Required dependencies are documented.
- [ ] Core functionality is documented.
- [x] Example commands are provided.
- [x] The documented commands execute successfully.
- [x] The software produces the expected outputs.
- [ ] Performance claims are verified, or none are made.
- [ ] Results can be reproduced using only the repository instructions.

### Commands executed

    uv sync
    uv run download-data
    uv run preprocess-data
    uv run analyze-data

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

- [ ] Public and iterative development is visible through issues,
      pull requests and commits.

## Community guidelines

- [ ] Contribution instructions are provided.
- [ ] Instructions for reporting problems are provided.
- [ ] Instructions for requesting support are provided.

## Issues and contributions

- Issue: TO COMPLETE
- Pull request: TO COMPLETE

## Final assessment

TO COMPLETE BY THE REVIEWER