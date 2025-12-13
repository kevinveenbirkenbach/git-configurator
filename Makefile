# ------------------------------------------------------------
# GitCon – Makefile (unittest-based)
# Robust: uses a dedicated virtualenv for install/lint/test
# ------------------------------------------------------------

SHELL := /usr/bin/env bash

# Virtualenv (override with: make VENV=/path/to/venv install)
VENV        ?= .venv
PYTHON      := $(VENV)/bin/python
PIP         := $(PYTHON) -m pip
UNITTEST    := $(PYTHON) -m unittest
RUFF        := $(PYTHON) -m ruff

SRC_DIR     := src
TEST_DIR    := tests

# Ensure src/ is on PYTHONPATH
export PYTHONPATH := $(SRC_DIR)

.DEFAULT_GOAL := help

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

$(PYTHON):
	@test -x "$(PYTHON)" || { \
		echo "[make] Creating virtualenv at '$(VENV)'..."; \
		python3 -m venv "$(VENV)"; \
	}
	@echo "[make] Ensuring pip is up to date in '$(VENV)'..."
	@"$(PYTHON)" -m pip install -U pip

# ------------------------------------------------------------
# Targets
# ------------------------------------------------------------

help:
	@echo "Available targets:"
	@echo "  make install        Install package in editable mode (venv)"
	@echo "  make test           Run unit tests (unittest, venv)"
	@echo "  make test-verbose   Run unit tests with verbose output (venv)"
	@echo "  make lint           Run ruff (venv; installs if missing)"
	@echo "  make clean          Remove Python cache files"
	@echo ""
	@echo "Notes:"
	@echo "  - This Makefile is venv-first to avoid PATH/Nix python issues."
	@echo "  - Override venv path via: make VENV=/tmp/gitcon-venv install"

test: $(PYTHON)
	@echo "[make] Running unit tests..."
	@"$(UNITTEST)" discover -s "$(TEST_DIR)" -p 'test_*.py'

test-verbose: $(PYTHON)
	@echo "[make] Running unit tests (verbose)..."
	@"$(UNITTEST)" discover -v -s "$(TEST_DIR)" -p 'test_*.py'

lint: $(PYTHON)
	@echo "[make] Ensuring ruff is installed in venv..."
	@command -v "$(VENV)/bin/ruff" >/dev/null 2>&1 || { \
		"$(PIP)" install -U ruff; \
	}
	@echo "[make] Running ruff..."
	@"$(RUFF)" check "$(SRC_DIR)" "$(TEST_DIR)"

clean:
	@echo "[make] Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "[make] Done."

.PHONY: help install test test-verbose lint clean
