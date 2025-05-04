# filepath: d:\Projects\RepoAuditTool-1\main.py
import os
import sys
from auditor.scanner import run_bandit_scan, check_forbidden_patterns
from auditor.dependencies import check_outdated_dependencies
from auditor.test_generator import create_test_stubs
from auditor.reporter import generate_html_report
from tqdm import tqdm

def main(repo_path, test_output_dir="tests"):
    print("Starting audit...")
    scan = run_bandit_scan(repo_path)
    forbidden = check_forbidden_patterns(repo_path)
    dependencies = check_outdated_dependencies(repo_path)

    print("Generating test stubs...")
    create_test_stubs(repo_path, test_output_dir)
    
    print("Generating report...")
    generate_html_report(scan, forbidden, dependencies, "report.html")

    print("Audit complete. Report saved to report.html.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <repository_path> [test_output_dir]")
        sys.exit(1)

    repository_path = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "tests"
    main(repository_path, output_directory)