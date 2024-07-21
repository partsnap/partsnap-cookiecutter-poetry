# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## System Configuration (One Time)

install [NixOS](https://nixos.org/) if you don't have NixOS installed yet
install [direnv](https://direnv.net/). On the latest OSX version do:

```bash
  $ brew install direnv
  $ echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```

configure [direnv](https://direnv.net/man/direnv.toml.1.html) toml file to trust our org

```bash
  $ mkdir -p ~/.config/direnv/
  $ touch ~/.config/direnv/config.toml
```

copy the following in your `config.toml` file (you can change the path to wherever your GitHub root is. Note that this will trust `ALL` directories underneath)

```
  [global]
  warn_timeout="20s"
  [whitelist]
  prefix = ["~/github/partsnap"]
```

We want to make sure Nix OS doesn't break if you update your Mac OS to the newest version.
To do this we need to edit the .zshrc with nano.

```bash
  $ nano ~/.zshrc
```

Make sure everything is here. (your_user) is going to depend on your system user you are using located on that export PATH.

```
    export PATH="$PATH:/Users/(your_user_)/.local/bin"
    eval "$(direnv hook zsh)"
    # Nix
    if [ -e '/nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh' ]; then
    . '/nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh'
    fi
    # End Nix
```

After closing nano and returning to bash make sure to source the changes.

```bash
  $ source ~/.zshrc
```

Now Nix-OS should be properly set for any projects located in the specified location you put.

## Getting started with your project

---

**NOTE**: Make sure you have performed the
[initial system configuration](#system-configuration-one-time) **once**.

---

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

{% if cookiecutter.database == "y" -%}
## Database CLI Useful Commands
Use these commands to populate and clear the database:
{{cookiecutter.project_slug}} db populate
{{cookiecutter.project_slug}} db clear
{%- endif %}

## Releasing a new version

{% if cookiecutter.publish_to == "pypi" -%}

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).
{%- elif cookiecutter.publish_to == "artifactory" -%}

- Add the `ARTIFACTORY_URL`, `ARTIFACTORY_USERNAME`, and `ARTIFACTORY_PASSWORD` to your projects secrets by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).
{%- endif %}

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
