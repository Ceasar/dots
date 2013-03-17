# dots

Modular dotfile manager. Symlinks dotfiles from plugins to HOME.

# Rationale

Sharing dotfiles as a team is a nice idea, but in practice to do so requires solving several problems:

- Not everyone uses the same apps. Vim users don't want your emacs dotfiles and vice-versa.
    - Consequently, forking is not very useful. Anecdotally, people seem to just cherry-pick.
- Putting all dotfiles in one repo makes history and documentation less useful.
- If dotfiles are shared, decisions to change them must be conservative. It makes the most sense to have dotfiles as decentralized as possible to commit to the fewest decision-makers.
- Many dotfiles themselves tend to be antimodular. By putting them in their own project, they can be organized (and then generated) in a more meaningful way.

What we want is a way to split up dotfiles by app, giving us meaningful history and fork-ability.

dots solves this problem by letting you easily install dotfile plugins, where a plugin is simply a directory from which dotfiles can be imported.

# Installation

```
git clone git@github.com:Ceasar/dots.git
cd dots
pip install -r requirements.txt
```

# Quickstart

We can see how dots works by means of a simple example. We'll create a simple plugin and then link it.

```
cd dots
cd plugins
mkdir example
echo "hello!" > example/.examplerc
echo "shows off how to make a plugin" > example/README.md
```

Great! We've made our first plugin!

Now we can link it to our `HOME` directory.

```
fab install_all
```

That's it! Check your home directory. `.examplerc` should exist.

# Remarks

Naturally, what you'll want to do in the future is to clone git repos into `plugins` and write more complex dotfiles. See [Ceasar/dot_gitconfig](https://github.com/Ceasar/dot_gitconfig) as an example.

If you already have a dotfiles repo, the easiest way to get started is just to clone or move your repo into plugins and link it until you have time to factor everything out.

If you do not already have a dotfiles repo, dots allows you to clone other people's entire dotfiles and use them as your own! Github has kindly compiled many fantastic [dotfiles](http://dotfiles.github.com/) that may be useful to get started.

# Usage

Install all plugins via `fab install_all`.

Install an individual plugin via: `fab install_plugin:PLUGIN_NAME`
