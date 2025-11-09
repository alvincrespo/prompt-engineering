#!/usr/bin/env python3
"""
Simple launcher script to run examples with proper Python path setup.
Usage: python run_example.py examples/code-generation/code-explanation-detailed.py
"""
import sys
import os
import subprocess

if len(sys.argv) != 2:
    print("Usage: python run_example.py <path_to_example_script>")
    sys.exit(1)

script_path = sys.argv[1]
if not os.path.exists(script_path):
    print(f"Error: Script {script_path} not found")
    sys.exit(1)

# Add current directory to PYTHONPATH and run the script
env = os.environ.copy()
current_dir = os.getcwd()
if 'PYTHONPATH' in env:
    env['PYTHONPATH'] = f"{current_dir}:{env['PYTHONPATH']}"
else:
    env['PYTHONPATH'] = current_dir

subprocess.run([sys.executable, script_path], env=env)
