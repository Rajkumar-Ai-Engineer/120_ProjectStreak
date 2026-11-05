# Data Analytics Folder Audit

**Repository:** [Rajkumar-Ai-Engineer/120_ProjectStreak](https://github.com/Rajkumar-Ai-Engineer/120_ProjectStreak)  
**Branch inspected:** `master`  
**Audited path:** `da/`  
**Audit date:** 2026-11-05  
**Audit type:** Static repository inventory and source-artifact review

## 1. Executive summary

The `da/` directory contains **21 files**:

- **5 PDF artifacts**
- **16 PNG screenshots**
- **0 visible source-code files**
- **0 notebooks**
- **0 project-specific README files before this documentation pass**
- **0 dependency manifests or dashboard/application source files**

The filenames indicate five Data Analytics project/source topics: World Wildlife, Job, Churn Analysis, Geospatial Coffee Sales, and Retail Sales. The labels 118 and 120 are preserved from the corresponding filenames. The remaining three artifacts have no project IDs visible in their filenames.

**Important:** The repository evidence currently establishes the presence of these source files, not the technical contents or implementation status of the projects. The PDFs and screenshots were not content-inspected in this pass. Therefore, no algorithm, dataset, visualization, metric, finding, or tool is attributed to any project.

## 2. Repository evidence

| Artifact | Type | Path | Evidence |
|---|---|---|---|
| World Wildlife | PDF | `da/118-world wildlife.pdf` | File exists in the audited directory; filename includes label 118 |
| Job | PDF | `da/120-job.pdf` | File exists in the audited directory; filename includes label 120 |
| Churn Analysis | PDF | `da/churn-analysis.pdf` | File exists in the audited directory |
| Geospatial Coffee Sales | PDF | `da/geospatial-coffee-sales.pdf` | File exists in the audited directory |
| Retail Sales | PDF | `da/retail-sales.pdf` | File exists in the audited directory |
| Screenshot evidence | PNG | 16 files listed in [da/README.md](da/README.md) | Visual assets exist; content-to-project mapping not established |

The directory listing was checked recursively. It returned 21 entries and was not truncated.

## 3. Project-level findings

### 3.1 Project/source 118 — World Wildlife

- **Source:** `da/118-world wildlife.pdf`
- **Domain:** Data Analytics (directory-level classification)
- **Project ID:** 118 (filename-derived; preserved, not independently verified against a master catalogue)
- **Known:** A PDF with a World Wildlife-themed filename exists.
- **Unknown:** Research question, data source, data schema, data cleaning, analytical approach, charts, results, conclusions, and tools.
- **Implementation status:** Not verifiable. No code or notebook is present in `da/` for this entry.
- **Required next step:** Extract and review the PDF before writing a technical project README.

### 3.2 Project/source 120 — Job

- **Source:** `da/120-job.pdf`
- **Domain:** Data Analytics (directory-level classification)
- **Project ID:** 120 (filename-derived; preserved, not independently verified against a master catalogue)
- **Known:** A PDF with a Job-themed filename exists.
- **Unknown:** Exact job-market use case, data source, fields, analysis, visualizations, findings, and tools.
- **Implementation status:** Not verifiable. No code or notebook is present in `da/` for this entry.
- **Required next step:** Extract and review the PDF before writing a technical project README.

### 3.3 Churn Analysis

- **Source:** `da/churn-analysis.pdf`
- **Project ID:** Unassigned.
- **Known:** The filename identifies a churn-analysis topic.
- **Unknown:** Industry, churn definition, target variable, dataset, cohort/time window, segmentation, statistical or predictive methods, evaluation metrics, and recommendations.
- **Implementation status:** Not verifiable from the directory contents.
- **Required next step:** Review the PDF and any mapped screenshots; do not assume that a predictive model was implemented merely because the filename contains “analysis”.

### 3.4 Geospatial Coffee Sales

- **Source:** `da/geospatial-coffee-sales.pdf`
- **Project ID:** Unassigned.
- **Known:** The filename identifies a geospatial coffee-sales topic.
- **Unknown:** Geographic unit, source data, coordinate/geocoding process, sales measures, spatial operations, map type, dashboard/tooling, and conclusions.
- **Implementation status:** Not verifiable from the directory contents.
- **Required next step:** Review the PDF and screenshots to determine whether the work is exploratory analysis, GIS analysis, dashboarding, or a combination.

### 3.5 Retail Sales

- **Source:** `da/retail-sales.pdf`
- **Project ID:** Unassigned.
- **Known:** The filename identifies a retail-sales topic.
- **Unknown:** Dataset, business questions, data preparation, metrics, time-series or customer analysis, visualizations, results, and tools.
- **Implementation status:** Not verifiable from the directory contents.
- **Required next step:** Review the PDF and any mapped screenshots before documenting analytical workflow or conclusions.

## 4. Screenshot inventory

There are 16 PNG assets dated 2026-11-03. Their exact filenames are listed in [da/README.md](da/README.md).

The screenshots are not assigned to any one of the five PDFs because their visual contents have not been inspected. They may be project outputs, intermediate evidence, or unrelated captures; the current evidence does not distinguish these possibilities.

## 5. Matching and inventory reconciliation

The current root `PROJECT_INVENTORY.md` and `documentation_inventory.json` do not identify the five DA PDF artifacts as canonical project entries. The existing root README also does not include a Data Analytics domain count.

| Source artifact | Canonical inventory match | Current classification |
|---|---|---|
| 118-world wildlife.pdf | Not established | Source artifact; reconciliation pending |
| 120-job.pdf | Not established | Source artifact; reconciliation pending |
| churn-analysis.pdf | Not established | Source artifact; reconciliation pending |
| geospatial-coffee-sales.pdf | Not established | Source artifact; reconciliation pending |
| retail-sales.pdf | Not established | Source artifact; reconciliation pending |

These are **not classified as confirmed missing projects**. A project may be represented elsewhere in the repository or in another reference source under a different name. The current evidence is insufficient to establish either a match or a missing status.

## 6. Risks and documentation gaps

1. **PDF content gap:** Project objectives, methodology, datasets, results, and tool choices cannot be safely documented from filenames.
2. **Screenshot mapping gap:** The 16 images have not been visually reviewed or linked to source PDFs.
3. **Implementation gap:** No source code or notebook is visible in `da/`; the PDF files may be reports or project evidence rather than executable projects.
4. **ID gap:** Only 118 and 120 appear in filenames. IDs for the other three topics must not be invented.
5. **Canonical inventory gap:** The current project inventory does not include these artifacts; reconciliation against the full reference catalogue remains open.

## 7. Recommended completion checklist

- [ ] Extract text and inspect every page of all five PDFs.
- [ ] Visually inspect all 16 screenshots.
- [ ] Map screenshots to source projects using explicit evidence.
- [ ] Record each project's objective, dataset, columns, cleaning, analysis, visualizations, results, tools, and limitations.
- [ ] Determine whether source code/notebooks exist elsewhere in the repository.
- [ ] Search the full repository and reference catalogue for aliases and duplicate entries.
- [ ] Assign project IDs only when supported by the original catalogue.
- [ ] Create one project-specific README per verified project.
- [ ] Update `PROJECT_INVENTORY.md`, `documentation_inventory.json`, and the root README only after reconciliation.

## 8. Verification boundary

This audit confirms directory structure, filenames, file types, and the absence of visible code/notebook files in the audited `da/` directory. It does **not** verify PDF contents, screenshot contents, analytical correctness, reproducibility, dashboard behavior, or implementation completeness. No project result or metric is certified.

The audit intentionally leaves unresolved questions visible rather than filling them with assumptions.
