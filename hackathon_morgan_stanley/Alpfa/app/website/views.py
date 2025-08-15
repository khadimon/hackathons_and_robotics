from django.shortcuts import render
from job.models import Job, ApplyJob
from .filter import Jobfilter
from resume.models import Resume
from django.contrib.staticfiles.storage import staticfiles_storage




def home(request):
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter':filter}
    return render(request, 'website/home.html', context)

def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    resume = Resume.objects.get(user = request.user)
    jobs, scores = get_matching_jobs(jobs, resume)
    context = {'jobs_scores': zip(jobs, scores)} 
    return render(request, 'website/job_listing.html', context)    

def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    if request.user.is_authenticated and request.user.is_applicant and request.user.is_verified:
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            has_applied = True 
        else:
            has_applied = False
        context = {'job':job, 'has_applied':has_applied}
        return render(request, 'website/job_details.html', context)
    else:
        context = {'job':job,}
        return render(request, 'website/job_details.html', context) 




from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from numpy.linalg import norm
from termcolor import colored
# import pandas as pd
import numpy as np
import requests
import PyPDF2
import re
# import plotly.graph_objects as go
import nltk
# from glob import glob


def get_matching_jobs(jobs, resume):

    jds_vec = []

    resume_content = read_resume_from_model(resume)
    resume_content = preprocess_text(resume_content)
    


    model = Doc2Vec.load(staticfiles_storage.path('cv_job_maching.model'))

    v1 = model.infer_vector(resume_content.split())

    for i in range(len(jobs)): # Only matching a 100 jobs with a 100 candidates

        jd = jobs[i].requirements
        

        jd = preprocess_text(jd)
        
        v2 = model.infer_vector(jd.split())

        jds_vec.append(v2)

    score_matrix = match([v1], jds_vec)

    top_k_jobs_for_candidates, top_k_scores_for_candidates = top_k_matches(score_matrix, k=2, threshold=0.3)

    # Step 1: Convert the QuerySet to a list to access specific indices
    selected_jobs_list = [list(jobs)[i] for i in top_k_jobs_for_candidates[0] if i < len(jobs)]


    # Step 2: Get the primary keys of the selected jobs
    selected_job_pks = [job.pk for job in selected_jobs_list]

    # Step 3: Use pk__in to filter the original queryset to return only the selected jobs
    selected_jobs_queryset = Job.objects.filter(pk__in=selected_job_pks)

    return selected_jobs_queryset, top_k_scores_for_candidates[0]

def normalize_scores(score_matrix):
    # Normalize the scores to be between 0 and 1
    min_val = np.min(score_matrix)
    max_val = np.max(score_matrix)
    return (score_matrix - min_val) / (max_val - min_val)


def top_k_matches(score_matrix, k=3, threshold=0.4):
    # Normalize scores
    norm_scores = normalize_scores(score_matrix)
    
    # Threshold mask to filter out scores below the threshold
    threshold_mask = norm_scores >= threshold
    
    # Top k jobs for candidates
    top_k_jobs_for_candidates = []
    top_k_scores_for_candidates = []

    for candidate_scores in norm_scores:
        # Get the indices of the top k jobs for each candidate
        top_k_indices = np.argsort(candidate_scores)[::-1][:k]
        top_k_filtered = [idx for idx in top_k_indices if candidate_scores[idx] >= threshold]
        top_k_filtered_scores = [candidate_scores[idx] for idx in top_k_filtered]


        top_k_jobs_for_candidates.append(top_k_filtered)
        top_k_scores_for_candidates.append(top_k_filtered_scores)
    

    return top_k_jobs_for_candidates, top_k_scores_for_candidates


def read_pdf(fname):    
    pdf = PyPDF2.PdfReader(fname)
    resume = ""
    for i in range(len(pdf.pages)):
        pageObj = pdf.pages[i]
        resume += pageObj.extract_text()
    return resume
def read_resume_from_model(resume_instance):
    # Check if the resume file exists
    if resume_instance.upload_resume:
        file_path = resume_instance.upload_resume.path  # Get the file path of the uploaded resume
        with open(file_path, 'rb') as f:  # Open the file in binary mode
            resume_content = read_pdf(f)  # Call the read_pdf function with the file object
            return resume_content
    else:
        return None
def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove punctuation from the text
    text = re.sub('[^a-z]', ' ', text)
    
    # Remove numerical values from the text
    text = re.sub(r'\d+', '', text)
    
    # Remove extra whitespaces
    text = ' '.join(text.split())
    
    return text

def compute_score(v1, v2):
    return 100*(np.dot(np.array(v1), np.array(v2))) / (norm(np.array(v1)) * norm(np.array(v2)))

def match(resumes, jds):
    matrix = np.zeros((len(resumes), len(jds)))
    for i, v1 in enumerate(resumes):
        for j, v2 in enumerate(jds):            
            score = compute_score(v1, v2)
            matrix[i, j] = score
    return matrix