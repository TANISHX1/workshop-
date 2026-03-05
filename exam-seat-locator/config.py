"""
config.py - Central configuration for Exam Seat Locator.
All path constants and app-level settings live here.
"""

import os

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
# PLAN_FILE removed — the system now supports multiple plan files.
# The summary index (data/summary_index.json) maps roll numbers → filenames.

# ── Flask ────────────────────────────────────────────────────────────────────────────
SECRET_KEY  = "exam-seat-locator-secret-key-2026"
DEBUG       = False
HOST        = "0.0.0.0"
PORT        = 5000

# Allowed extensions for plan file uploads
ALLOWED_EXTENSIONS = {"json"}

# ── Data Retention ───────────────────────────────────────────────────────────
# How old a PLAN-*.json file must be (in days) before the cleanup daemon
# removes it from disk. Change this single value to adjust retention globally.
PLAN_RETENTION_DAYS   = 15   # delete plan files older than this many days

# How often the cleanup daemon wakes up to scan for stale files.
# Keeping it equal to PLAN_RETENTION_DAYS means a file is never more than
# 2 × PLAN_RETENTION_DAYS old before it is guaranteed to be removed.
CLEANUP_INTERVAL_DAYS = 15   # run cleanup every this many days
