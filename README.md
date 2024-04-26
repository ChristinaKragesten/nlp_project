# REPO containing small NLP projects

## Text Summarization
Create environment

    create python environment
    conda create -n nlp_env
    conda activate ./nlp_env
    pip install . (ensure pip is pointing to environment nlp_env/bin/pip)

To run text summarizer, use the command:
- python application.py --txt_filepath 'path to text file' summarize --above_avg_factor 'float factor to adjust final summarization'
