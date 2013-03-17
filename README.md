# dots

Modular dotfile manager.

# rationale

Sharing dotfiles as a team is a nice idea, but in practice to do so requires solving several problems:

- Not everyone uses the same apps. Vim users don't want your emaces dotfiles and vice-versa.
    - This makes forking far less useful. People tend to just cherry-pick.
- Putting all dotfiles in one repo makes history less useful.
- Decisions to change dotfiles must be conservative.

What we want is a way to split up dotfiles by app. We want a git repo for each app, with meaning history for each and easy fork-ability.

dots solves this problem by letting you easily install dotfile plugins, where a plugin is simply a directory from which dotfiles can be pulled.

# installation

`git clone git@github.com:Ceasar/dots.git`

# quickstart

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

Naturally, what you'll want to do in the future is to clone git repos into `plugins` and write more complex dotfiles.

# usage

Install all plugins via `fab install_all`.

Install an individual plugin via: `fab install_plugin:PLUGIN_NAME`
