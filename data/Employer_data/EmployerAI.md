# AI Models for Employers: Datasets Overview

This document outlines the datasets compiled for three AI applications designed for enhancing employer hiring processes:

1. **Candidate Screening**: Analyzing applicant profiles, resumes, and blockchain-verified certifications to shortlist candidates based on relevance to the job.
2. **Predictive Hiring**: Leveraging predictive analytics to assess a candidate’s future performance based on historical data, certifications, and skill sets.
3. **Job Description Enhancement**: Generating or refining job descriptions based on roles and responsibilities provided by employers.

Below are the dataset descriptions and their specific usage during training to achieve the project goals.

---

## **1. Candidate Screening**
**Goal**: Automate the analysis of resumes, profiles, and certifications to efficiently shortlist candidates who meet job requirements.

### **Datasets and Usage**:
1. **[Resumes Dataset (Kaggle)](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)**
   This dataset contains anonymized resumes with attributes like skills, education, experience, and certifications. It is ideal for training models to parse and extract relevant candidate information for screening. However, its diversity in industries may be limited, so additional datasets or domain-specific resumes may be needed.

2. **[Huggingface](https://huggingface.co/datasets/cnamuangtoun/resume-job-description-fit)**
   This dataset showcases a candidate’s resume matches a job description. It connects the candidate’s experience, skills, and qualifications (resume_text) against the requirements and responsibilities outlined in the job description (job_description_text). The "label" provides a compatibility score, indicating the degree of alignment.

3. **[Github Profiles Dataset](https://github.com/florex/resume_corpus)**
   multi-labeled dataset of resumes labeled with occupations. The resume files have the extension .txt and the corresponding labels are in a file with the extension .lab.

4. **[Huggingface](https://huggingface.co/datasets/Sachinkelenjaguri/Resume_dataset)**
     This data represents a professional profile of jobs and the skills needed for the roles


---

## **2. Predictive Hiring**
**Goal**: Assess a candidate’s future performance by analyzing historical data, certifications, and skill sets using predictive analytics.

### **Datasets and Usage**:
1. **[Employee Performance Dataset (Kaggle)](https://huggingface.co/datasets/lang-uk/recruitment-dataset-job-descriptions-english)**
   This dataset includes anonymized employee performance reviews, attributes like job role, skills, and education. It is suitable for training models to predict performance based on a candidate’s past evaluations. Its generalizability is limited without supplementary industry-specific performance datasets.

2. **[Kaggle](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)**
     This dataset provides a comprehensive collection of  job postings to facilitate research and analysis in the field of job market trends, natural language processing (NLP), and machine learning. Created for educational and research purposes, this dataset offers a diverse set of job listings across various industries and job types.


---

## **3. Job Description Enhancement**
**Goal**: Generate or refine job descriptions to ensure clarity, attractiveness, and search optimization.

### **Datasets and Usage**:
1. **[HuggingFace](https://huggingface.co/datasets/jacob-hugging-face/job-descriptions)**
   This dataset contains position, job description, keyword etc to help job enhancement. It include information about various job listings and projects, particularly in the tech and blockchain sectors. It highlights key details such as job descriptions, required skills, experience levels, and technologies used.

2. **[Kaggle](https://www.kaggle.com/datasets/kshitizregmi/jobs-and-job-description)**
     This dataset comprises a collection of job titles paired with detailed job descriptions. You can use this dataset for natural language processing (NLP) tasks, offering opportunities for recommendation systems, text classification, information retrieval, and semantic search.

3. **[Kaggle](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)**
     This dataset contains contains jobs, description, salary range etc 
---



