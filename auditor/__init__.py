"""
This file initializes the auditor package.
"""

from .scanner import run_bandit_scan, check_forbidden_patterns
from .dependencies import check_outdated_dependencies
from .test_generator import create_test_stubs
from .reporter import generate_reports