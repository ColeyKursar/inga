from django.shortcuts import render
import os
import subprocess


def UpdateView(request):
    git_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    git_pull = "git pull"

    identity = subprocess.check_output("whoami", cwd=git_dir, stderr=subprocess.STDOUT, universal_newlines=True, shell=True).__dict__

    subprocess.check_output(git_pull, cwd=git_dir, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
