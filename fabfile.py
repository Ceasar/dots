"""
Install, update, link, and uninstall dotfiles repos.
"""
from os import listdir, getenv, getcwd
from os.path import join, isdir

from fabric.api import local, settings, task
from fabric.contrib.console import confirm
import repos


# do not install these files
IGNORE = set(['.git', '.gitignore'])


def symlink(src, dest):
    """
    Create a symlink in the home directory to the target file.
    """
    source, dest = join(getcwd(), src), join(getenv("HOME"), dest)
    with settings(warn_only=True):
        result = local('ln -s %s %s' % (source, dest), capture=True)
    if result.failed:
        if confirm("%s exists. Replace it?" % dest):
            local('ln -Ffs %s %s' % (source, dest), capture=True)


@task
def link(path, repo=None):
    """
    Install each of the dotfiles from each repo in the directory.

        path: path of directory to search
        repo: optional. name of specific repo to search
    """
    if repo is None:
        repos_path = join(getcwd(), path)
        for repo in listdir(repos_path):
            if isdir(join(repos_path, repo)):
                link(path, repo)
    else:
        repo_path = join(path, repo)
        for filename in listdir(repo_path):
            if filename.startswith('.') and filename not in IGNORE:
                symlink(join(repo_path, filename), filename)
