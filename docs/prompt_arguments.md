# Prompt arguments

When running the command `ccp` a prompt will start which enables you to configure your repository. The
prompt values and their explanation are as follows:

---

**author**

Your full name.

**email**

Your email address.

**project_name**

Your project name. Should be equal to the name of your repository
and it should only contain alphanumeric characters and `-`'s.

**project_slug**

The project slug, will default to the `project_name` with all `-`'s
replaced with `_`. This will be how you import your code later, e.g.

```python
from <project_slug> import foo
```

**project_caps**

The project caps, will default to the `project_slug` with all caps.
This will be how you import your code later, e.g.

```python
from <project_caps> import foo
```

**project_description**

A short description of your project.

**publish_to**

`"pypi"`, `"artifactory"`, or `"none"`. Adds functionality to the
`Makefile` and Github workflows to make publishing your code as
simple as creating a new release release on Github. For more info,
see
[Publishing to Pypi or Artifactory](./features/publishing.md).

**port**
The port to be used for your library or service.

**database**
`"y"` or `"n"`. Adds a database template to the project.

**devcontainer**

`"y"` or `"n"`. Adds a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) specification to the project along with pre-installed pre-commit hooks and VSCode python extension configuration.

---
