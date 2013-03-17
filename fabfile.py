"""
Installer for dotfiles.

Install all plugins via `fab install_all`.

Install an individual plugin via: `fab install_plugin:PLUGIN_NAME`
"""
import os
from os.path import join, isdir

from fabric.api import local, settings
from fabric.contrib.console import confirm

HOME = os.getenv("HOME")
PWD = os.getcwd()

PLUGINS_DIR = "plugins"

# do not install these files
IGNORE = set(['.git', '.gitignore'])


def install(src, dest):
    """
    Create a symlink in the home directory to the target file.
    """
    source = join(PWD, src)
    dest = join(HOME, dest)
    with settings(warn_only=True):
        result = local('ln -s %s %s' % (source, dest), capture=True)
    if result.failed:
        if confirm("%s exists. Replace it?" % dest):
            local("rm %s" % dest)
            install(src, dest)


def install_plugin(plugin_name):
    """
    Attempt to install each of the dotfiles in a plugin.
    """
    plugin_path = join(PLUGINS_DIR, plugin_name)
    for filename in os.listdir(plugin_path):
        if filename.startswith('.') and filename not in IGNORE:
            install(join(plugin_path, filename), filename)


def install_all():
    """
    Attempt to install each of the dotfiles from each plugin.
    """
    plugins_path = join(PWD, PLUGINS_DIR)
    for plugin in os.listdir(plugins_path):
        if isdir(join(plugins_path, plugin)):
            install_plugin(plugin)
