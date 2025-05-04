import sys
import json
from subprocess import check_output, CalledProcessError

def check_outdated_dependencies(repo_path):
    """
    Checks for outdated dependencies in the current Python environment.

    Parameters:
    - repo_path (str): The path to the repository (not used in this function).

    Returns:
    - list: A list of tuples containing the package name and the current version.
    """
    outdated_packages = []
    try:
        # Use pip to check for outdated packages in JSON format
        output = check_output([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=json']).decode('utf-8')
        outdated_list = json.loads(output)
        for package in outdated_list:
            package_name = package["name"]
            current_version = package["version"]
            outdated_packages.append((package_name, current_version))
    except CalledProcessError as e:
        print(f"Error checking outdated dependencies: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing pip output: {e}")

    return outdated_packages