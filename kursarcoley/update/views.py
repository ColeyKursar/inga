from django.shortcuts import render
from os import path
import subprocess


class UpdateView(request):
    git_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    git_pull = ['git', 'pull']

    subprocess.run(git_pull, cwd=git_dir, universal_newlines=True)
