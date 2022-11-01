@echo off
set envs="python36" "python37" "python38"

(for %%a in (%envs%) do ( 
	conda activate %%a
	python --version
	python fullTest.py
))