""" This module is used to check a C file in a given directory"""
from python_modules.Verify_files.compile_file import compile_c
from python_modules.Verify_files.verify_file import verify_file

def check_file(absolute_path_to_c_file, temp_folder, solvers):
    """Check a C file in a given directory
    
    Args:
        absolute_path_to_c_file: The absolute path to the C file
        temp_folder: The temporary folder to store the compiled file
        solvers: the solvers that are used byu frama_C
    Returns:
        result: True if the file is compiled, False otherwise
        output: The output of the compilation
        verified_goals: The number of verified goals
        verification_time_taken: The time taken to verify the file
    """
    # Compile the file
    result, output = compile_c(absolute_path_to_c_file, temp_folder)

    # If the compilation failed, return False and the output
    if result is False:
        return False, output, None, 0
    # Verify the file and return it
    verified, error_cause, verified_goals_amount, elapsed_time = verify_file(absolute_path_to_c_file, solvers)

    return verified, error_cause, verified_goals_amount, elapsed_time
