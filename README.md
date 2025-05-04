# RepoAuditTool

RepoAuditTool is a Python application designed to audit code repositories for security vulnerabilities, outdated dependencies, and to generate test stubs. It provides a comprehensive report of the findings, making it easier for developers to maintain secure and up-to-date code.

## Features

- **Security Scanning**: Utilizes Bandit to scan for security vulnerabilities in the codebase.
- **Dependency Checking**: Identifies outdated dependencies to ensure the project uses the latest and most secure versions.
- **Test Stub Generation**: Automatically creates test stubs to facilitate unit testing.
- **HTML Reporting**: Generates a detailed HTML report summarizing the audit results.

## Installation

To get started with RepoAuditTool, clone the repository and set up your environment.

### Using Conda (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RepoAuditTool
   ```

2. Create a new Conda environment:
   ```bash
   conda create -n repo-audit-tool python=3.9 -y
   conda activate repo-audit-tool
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Without Conda

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RepoAuditTool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application from the command line, providing the path to the repository you want to audit. Optionally, specify a directory for the generated test stubs.

```bash
python main.py <repository_path> [test_output_dir]
```

- `<repository_path>`: The path to the repository you want to audit.
- `[test_output_dir]`: (Optional) The directory where test stubs will be generated. Defaults to "tests".

## Requirements

The project requires the following Python packages:

- tqdm: For displaying progress during execution.
- bandit: For security scanning.
- other dependencies as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.