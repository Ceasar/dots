
================================================================================
dots
================================================================================

**dots** is package manager for dotfiles; it automates installing, upgrading,
configuring, and removing dotfiles.

A *package* is simply a directory from which dotfiles can be imported.

Motivation
================================================================================

Historically, dotfiles have been anti-modular; they have been difficult to
separate and recombine.

At the macro level, this was so because people stored all of their dotfiles in a
single repository. This meant that any given repository contained many files
which were irrelevant to someone browsing them; no Emacs user has an interest in
a ``.vimrc``.

At the micro level, 

Benefits
================================================================================

- **Never lose a dotfile again.** As parts of packages, dotfiles are always
  in version control.

- **Customize your dotfiles by cherry-picking the good parts of dotfiles you
  like.** It's as easy as ``dots install X``.

- **Collaborate on and share dotfiles liberally.** By working with cohesive
  *parts* of dotfiles, there is less risk in making a change that someone might
  not like.

Installation
================================================================================

To install dots, simply::

    pip install dots

Quickstart
================================================================================

We can see how dots works by means of a simple example.

First we will create a simple plugin and then link it::

    cd dots
    mkdir plugins
    cd plugins
    mkdir example
    echo "hello!" > example/.examplerc
    echo "shows off how to make a plugin" > example/README.md

Next, we can link it to our ``$HOME`` directory::

    fab link:plugins

If you check your home directory, ``.examplerc`` should exist.

Usage
================================================================================

dots relies on fabric. Therefore all commands are of the form::

    fab COMMAND:ARG1,ARG2,..

Use ``fab --list`` to see all commands and ``fab -d COMMAND`` for detailed help.

Available commands::

    link               Install each of the dotfiles from each repo or a single one.
    repos.from_config  Install git repos from a config file in the directory.
    repos.install      Install a git repo in the directory.
    repos.uninstall    Uninstall a git repo in the directory.
    repos.update       Update a git repo in the directory or all of them.

Remarks
================================================================================

Naturally, what you'll want to do in the future is to clone git repos into
``plugins`` and write more complex dotfiles. See `Ceasar/dot_gitconfig` as an
example.

If you already have a dotfiles repo, the easiest way to get started is just to
clone or move your repo into plugins and link it until you have time to factor
everything out.

If you do not already have a dotfiles repo, dots allows you to clone other
people's entire dotfiles and use them as your own! Github has kindly compiled
many `fantastic dotfiles`_ that may be useful to get started.

You can also keep track of different sets of dotfiles by keeping different
configurations in different folders.

.. _fantastic dotfiles: http://dotfiles.github.com/

.. _Ceasar/dot_gitconfig: https://github.com/Ceasar/dot_gitconfig
