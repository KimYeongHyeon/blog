---
title: "Research Projects"
layout: "projects"
url: "/projects/"
summary: "Current and Past Research Projects"
---

## Current Projects

### TELOS - Target-trial Emulation & Learning-Oriented System

**Duration:** 2025  
**Role:** Team Lead  
**Recognition:** Grand Prize, Korea Clinical Datathon 2025

**Description:**  
TELOS is a multi-agent framework for emulating registered clinical trials using observational clinical datasets. Built for KCD2025 on MIMIC-IV, it connects clinical trial design, information extraction, statistical analysis, and reporting into a reproducible evidence-generation workflow.

**Key Achievements:**
- Won the Grand Prize at KCD2025
- Designed the overall multi-agent architecture
- Integrated agents for trial protocol extraction, cohort selection from MIMIC-IV, statistical analysis, and automated reporting
- Demonstrated trial emulation for steroid treatment in severe septic shock
- Identified high-acuity data limitations and scalability paths to other diseases

**Technologies:** Python, LLM agents, MIMIC-IV, target-trial emulation, statistical analysis

---

### Iterative Target Trial Emulation Using Real-World Medical Data

**Duration:** 2026  
**Role:** Team3  
**Recognition:** Excellence Award, President of the Korea Institute of Science and Technology Award, 2026 AI Co-Scientist Challenge Korea

**Description:**  
This project develops a multi-agent AI framework for automated target trial emulation using real-world medical data. The workflow decomposes trial emulation into cohort extraction, causal inference, propensity score matching, and clinical report generation.

**Key Achievements:**
- Placed 4th overall at the 2026 AI Co-Scientist Challenge Korea
- Built OMOP-CDM-compatible workflows for potential deployment across Korean university hospitals
- Reproduced trends from PLATO, LEADER, and ARISTOTLE using Synthea-based synthetic data
- Conducted the work through collaboration among BiLab, PILL, and Pathfinder Lab

**Technologies:** Python, LLM agents, OMOP-CDM, causal inference, propensity score matching, clinical report generation

---

### mimic-iv-omop-pg

**Duration:** 2026  
**Role:** Open-source developer

**Description:**  
mimic-iv-omop-pg is a PostgreSQL port of the OHDSI/MIMIC ETL. It lets MIMIC-IV run on an existing OHDSI Broadsea stack with Postgres, WebAPI, and ATLAS, without a separate BigQuery project.

**Key Achievements:**
- Ported 39 BigQuery SQL files to PostgreSQL
- Converted 92% automatically and patched edge cases manually
- Verified 24/24 OHDSI unit tests, 38/38 view creation, and integrity checks
- Documented limitations around row identity, MIMIC-IV version support, OMOP CDM version, and waveform modules

**Technologies:** PostgreSQL, OHDSI, OMOP CDM, MIMIC-IV, Broadsea, SQL

---

### LangGraph-based CT Metal Artifact Reduction

**Duration:** Dec 2024 – Present  
**Role:** Independent Researcher  
**Advisors:** Prof. Kyungsang Kim (Harvard Medical School, Massachusetts General Hospital), Prof. Dongheon Lee

**Description:**  
This project implements LangGraph-MAR, a graph-based framework for CT metal artifact reduction. The framework combines sinogram inpainting, L1-based metal soft-thresholding, reconstruction, and automated image quality assessment.

**Key Objectives:**
- Adapt metal thresholds to variations in artifact severity across materials, sizes, and locations
- Improve structural restoration compared with representative MAR baselines
- Support robust artifact mitigation across body and head CT protocols

**Technologies:** Python, PyTorch, LangGraph, Medical Imaging (DICOM), CT Image Processing

---

## Past Projects

### CT Metal Artifact Reduction for AAPM Grand Challenge

**Duration:** Dec 2023 – Dec 2024  
**Role:** Visiting Researcher  
**Institution:** Biomedical Engineering Research Institute, Chungnam National University  
**Supervisor:** Prof. Kyungsang Kim, Prof. Dongheon Lee

**Description:**  
Developed a CT metal artifact reduction and enhancement model specifically for the AAPM Grand Challenge competition. The project focused on creating robust algorithms that can handle various types of metal artifacts in CT scans.

**Key Achievements:**
- Ranked 21st overall in the AAPM Grand Challenge
- Developed CT metal artifact reduction and enhancement model
- Designed graph-based approach for out-of-distribution challenges using LangGraph
- Successfully handled diverse artifact patterns in clinical CT images

**Technologies:** Python, PyTorch, Medical Imaging, CT Reconstruction, Deep Learning

---

### Left Ventricular Mass Quantification using Meta-Learning

**Duration:** May 2022 – Nov 2022  
**Role:** Team Leader  
**Program:** Medical AI Expert Training, Korea Human Resource Development Institute for Health & Welfare  
**Advisor:** Prof. Dongheon Lee (Chungnam National University)

**Description:**  
Led a collaborative project with professors and doctors to develop a MAML-based segmentation model for accurate left ventricular mass quantification from multi-view echocardiograms in few-shot settings. This research addresses the challenge of limited labeled medical imaging data.

**Key Achievements:**
- Published in PeerJ Computer Science (2025)
- Successfully applied meta-learning to medical image segmentation
- Achieved accurate quantification with minimal training samples
- Collaborated with medical professionals to define research objectives

**Technologies:** Model-Agnostic Meta-Learning (MAML), PyTorch, Echocardiography, Few-shot Learning

[[Publication]](https://scholar.google.co.kr/citations?view_op=view_citation&hl=ko&user=cLAlajcAAAAJ&citation_for_view=cLAlajcAAAAJ:W7OEmFMy1HYC)

---

### Computer Vision Research

**Duration:** March 2018 – Aug 2020  
**Role:** Graduate Researcher  
**Lab:** Intelligent Technology Lab, Inha University  
**PI:** Phillkyu Lee

**Description:**  
Conducted comprehensive research in computer vision, focusing on hierarchical learning, object detection, and active learning methods. The project resulted in multiple publications in peer-reviewed journals.

**Key Achievements:**
- 6 research papers published in computer vision field (1 as first author)
- Designed hierarchical feature model for learning new classes using sampling
- Implemented multi-object detection model using hierarchical knowledge transfer
- Developed EER-ASSL (Expected Error Reduction Active Semi-Supervised Learning) framework
- Enabled adaptation to new object classes and unseen distributions

**Research Areas:**
- Hierarchical feature learning
- Open-set object detection
- Active semi-supervised learning
- Knowledge transfer and adaptation

**Technologies:** Python, TensorFlow, OpenCV, Computer Vision, Deep Learning

**Selected Publications:**
- [Hierarchical open-set object detection in unseen data](https://scholar.google.co.kr/citations?view_op=view_citation&hl=ko&user=cLAlajcAAAAJ&citation_for_view=cLAlajcAAAAJ:UeHWp8X0CEIC) (2019, First Author)
- [EER-ASSL: Combining Rollback Learning and Deep Learning for Rapid Adaptive Object Detection](https://scholar.google.co.kr/citations?view_op=view_citation&hl=ko&user=cLAlajcAAAAJ&citation_for_view=cLAlajcAAAAJ:zYLM7Y9cAGgC) (2020)
- [Dynamic MLML-tree based adaptive object detection using heterogeneous data distribution](https://scholar.google.co.kr/citations?view_op=view_citation&hl=ko&user=cLAlajcAAAAJ&citation_for_view=cLAlajcAAAAJ:IjCSPb-OGe4C) (2020)

---

## Research Collaborations

I actively collaborate with researchers from:
- **Harvard Medical School / Massachusetts General Hospital** - Medical Imaging Lab
- **Chungnam National University** - Biomedical Engineering Research Institute
- **Inha University** - Intelligent Technology Lab

---

## Research Interests & Future Directions

My research focuses on developing AI solutions for medical imaging challenges, with particular emphasis on:

- **Medical Image Analysis:** CT artifact reduction, echocardiography analysis
- **Few-shot Learning:** Adapting models to work with limited medical data
- **Meta-Learning:** Rapid adaptation to new medical imaging tasks
- **Clinical Evidence Generation:** Multi-agent workflows for observational clinical data and target-trial emulation
- **Graph-based Methods:** Leveraging graph structures for medical image processing
- **Clinical Informatics:** OMOP-CDM and MIMIC-IV workflows for reproducible real-world evidence
- **Out-of-distribution Generalization:** Ensuring robust performance across diverse datasets

---

*For collaboration inquiries or more information about these projects, please [contact me](/about/).*
