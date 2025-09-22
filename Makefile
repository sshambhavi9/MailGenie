# Makefile for MailGenie

# Virtual environment path
VENV := venv

# Default shell
SHELL := /bin/bash

.PHONY: demo setup clean

# Run the project in Demo Mode
demo: $(VENV)/bin/activate
	@echo ">>> Running MailGenie in Demo Mode..."
	@echo "LLM_MODE=mock" > .env
	@echo "GMAIL_MODE=mock" >> .env
	@$(VENV)/bin/python mailgenie/gmail_fetch.py

# Setup dependencies
setup:
	@echo ">>> Creating virtual environment and installing dependencies..."
	python3 -m venv $(VENV)
	@$(VENV)/bin/pip install --upgrade pip
	@$(VENV)/bin/pip install -r requirements.txt
	@echo ">>> Setup complete! Run 'make demo' to test the project."

# Clean virtualenv and cache files
clean:
	@echo ">>> Cleaning up..."
	rm -rf $(VENV) .env __pycache__ */__pycache__ *.pyc *.pyo
	@echo ">>> Done."
