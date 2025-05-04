import os
import ast

def create_test_stubs(repo_path, output_dir):
    """
    Creates test cases for the given repository path and saves them in the specified output directory.

    Parameters:
    - repo_path (str): The path to the repository for which to create test cases.
    - output_dir (str): The directory where the test cases will be saved.
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
                            # Write the test file header
                            test_file.write(f"# Test cases for {file}\n")
                            test_file.write("import unittest\n")
                            test_file.write("from unittest.mock import patch, MagicMock\n")
                            test_file.write(f"from {os.path.splitext(file)[0]} import *\n\n")
                            test_file.write(f"class Test{os.path.splitext(file)[0].capitalize()}(unittest.TestCase):\n\n")

                            # Generate test cases for each function
                            for node in ast.walk(tree):
                                if isinstance(node, ast.FunctionDef):
                                    test_file.write(f"    def test_{node.name}(self):\n")
                                    
                                    # Analyze function arguments
                                    if node.args.args:
                                        args = ", ".join(arg.arg for arg in node.args.args)
                                        test_file.write(f"        # TODO: Replace with actual test logic for {node.name}\n")
                                        test_file.write(f"        result = {node.name}({args})\n")
                                        test_file.write(f"        self.assertIsNotNone(result)\n\n")
                                    else:
                                        test_file.write(f"        # TODO: Replace with actual test logic for {node.name}\n")
                                        test_file.write(f"        result = {node.name}()\n")
                                        test_file.write(f"        self.assertIsNotNone(result)\n\n")

                                    # Mock external dependencies if detected
                                    for child in ast.walk(node):
                                        if isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute):
                                            if child.func.attr in ["PlaySound", "sleep"]:
                                                test_file.write(f"        # Mock external dependency: {child.func.attr}\n")
                                                test_file.write(f"        with patch('{child.func.attr}') as mock_{child.func.attr.lower()}:\n")
                                                test_file.write(f"            mock_{child.func.attr.lower()}.return_value = None\n")
                                                test_file.write(f"            result = {node.name}()\n")
                                                test_file.write(f"            self.assertIsNotNone(result)\n\n")

                            # Add a main block to run the tests
                            test_file.write("\nif __name__ == '__main__':\n")
                            test_file.write("    unittest.main()\n")
                    except SyntaxError as e:
                        print(f"Skipping {file_path} due to syntax error: {e}")

    print(f"Test cases created in {output_dir}.")