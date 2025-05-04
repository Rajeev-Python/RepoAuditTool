import os
import ast

def create_test_stubs(repo_path, output_dir):
    """
    Creates test stubs for the given repository path and saves them in the specified output directory.

    Parameters:
    - repo_path (str): The path to the repository for which to create test stubs.
    - output_dir (str): The directory where the test stubs will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=file_path)
                        test_stub_path = os.path.join(output_dir, f"test_{file}")
                        with open(test_stub_path, "w", encoding="utf-8") as test_file:
                            test_file.write(f"# Test stubs for {file}\n")
                            for node in ast.walk(tree):
                                if isinstance(node, ast.FunctionDef):
                                    test_file.write(f"def test_{node.name}():\n")
                                    test_file.write("    pass\n\n")
                    except SyntaxError as e:
                        print(f"Skipping {file_path} due to syntax error: {e}")

    print(f"Test stubs created in {output_dir}.")