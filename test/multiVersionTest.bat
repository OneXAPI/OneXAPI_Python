@echo off
set envs="python36" "python37" "python38" "python39" "python310"

(for %%a in (%envs%) do ( 
	conda activate %%a
	python --version
	python fullTest.py
))