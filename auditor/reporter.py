def generate_html_report(scan_results, forbidden_patterns, outdated_dependencies, output_file):
    with open(output_file, 'w') as f:
        f.write("<html><head><title>Audit Report</title></head><body>")
        f.write("<h1>Audit Report</h1>")
        
        f.write("<h2>Scan Results</h2>")
        f.write("<pre>{}</pre>".format(scan_results))
        
        f.write("<h2>Forbidden Patterns</h2>")
        f.write("<pre>{}</pre>".format(forbidden_patterns))
        
        f.write("<h2>Outdated Dependencies</h2>")
        f.write("<pre>{}</pre>".format(outdated_dependencies))
        
        f.write("</body></html>")