import os
from datetime import datetime

def generate_reports(scan_results, forbidden_patterns, outdated_dependencies, base_output_dir):
    """
    Generates both HTML and Markdown reports for the audit process.

    Parameters:
    - scan_results (str): The results of the scan.
    - forbidden_patterns (str): The forbidden patterns detected.
    - outdated_dependencies (str): The outdated dependencies detected.
    - base_output_dir (str): The base directory where the reports will be saved.
    """
    # Create a directory for the date (YYYYMMDD)
    date_str = datetime.now().strftime("%Y%m%d")
    date_dir = os.path.join(base_output_dir, date_str)
    os.makedirs(date_dir, exist_ok=True)

    # Generate filenames with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_report_path = os.path.join(date_dir, f"report_{timestamp}.html")
    markdown_report_path = os.path.join(date_dir, f"report_{timestamp}.md")

    # Generate HTML report
    with open(html_report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Audit Report</title></head><body>")
        f.write("<h1>Audit Report</h1>")
        f.write(f"<h2>Date: {date_str}</h2>")
        f.write(f"<h2>Time: {timestamp.split('_')[1]}</h2>")
        
        f.write("<h2>Scan Results</h2>")
        f.write(f"<pre>{scan_results}</pre>")
        
        f.write("<h2>Forbidden Patterns</h2>")
        f.write(f"<pre>{forbidden_patterns}</pre>")
        
        f.write("<h2>Outdated Dependencies</h2>")
        f.write(f"<pre>{outdated_dependencies}</pre>")
        
        f.write("</body></html>")

    # Generate Markdown report
    with open(markdown_report_path, "w", encoding="utf-8") as f:
        f.write("# Audit Report\n\n")
        f.write(f"**Date:** {date_str}\n\n")
        f.write(f"**Time:** {timestamp.split('_')[1]}\n\n")
        
        f.write("## Scan Results\n")
        f.write(f"```\n{scan_results}\n```\n\n")
        
        f.write("## Forbidden Patterns\n")
        f.write(f"```\n{forbidden_patterns}\n```\n\n")
        
        f.write("## Outdated Dependencies\n")
        f.write(f"```\n{outdated_dependencies}\n```\n")

    print(f"Reports generated:\n- {html_report_path}\n- {markdown_report_path}")