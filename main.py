# filepath: d:\Projects\RepoAuditTool-1\main.py
import os
import sys
from auditor.scanner import run_bandit_scan, check_forbidden_patterns
from auditor.dependencies import check_outdated_dependencies
from auditor.test_generator import create_test_stubs
from auditor.reporter import generate_reports
from tqdm import tqdm

def main(repo_path, test_output_dir="tests"):
    print("Starting audit...")
    scan = run_bandit_scan(repo_path)
    forbidden = check_forbidden_patterns(repo_path)
    dependencies = check_outdated_dependencies(repo_path)

    print("Generating test stubs...")
    create_test_stubs(repo_path, test_output_dir)
    
    print("Generating report...")
    # Ensure the reports folder exists
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    generate_reports(scan, forbidden, dependencies, reports_dir)

    print(f"Audit complete. Reports saved to the 'reports' folder.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <repository_path> [test_output_dir]")
        sys.exit(1)

    repository_path = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "tests"
    main(repository_path, output_directory)