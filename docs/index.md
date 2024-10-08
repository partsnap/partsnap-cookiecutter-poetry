<p align="center">
<div class="row">
  <div class="column">
    <img width="100" src="static/partsnap-woman.png">
  </div>
  <div class="column">
  <img width="600" src="static/cookiecutter.svg">
  </div>
</div>
</p style = "margin-bottom: 2rem;">

---

[![Documentation Status](https://readthedocs.com/projects/partsnap-llc-partsnap-cookiecutter-poetry/badge/?version=latest&token=fbd35572c635fc26d72e64f71a1b36006f1d65c3a70a5fa09bcfdfabc64da3d4)](https://partsnap-llc-partsnap-cookiecutter-poetry.readthedocs-hosted.com/en/latest/?badge=latest)
[![Space Metric](https://partsnap.testspace.com/spaces/281541/badge?token=d5cdcee51a222bddbda4b92735465fdd55fe244f)](https://partsnap.testspace.com/spaces/281541?utm_campaign=metric&utm_medium=referral&utm_source=badge "Test Cases")
[![Space Metric](https://partsnap.testspace.com/spaces/281541/metrics/643202/badge?token=26b7878c42df6234bc06187d572092e99b032866)](https://partsnap.testspace.com/spaces/281541/current/Code%20Coverage?utm_campaign=metric&utm_medium=referral&utm_source=badge "Code Coverage (lines)")

<!-- [![Space Metric](https://partsnap.testspace.com/spaces/281541/metrics/643202/badge?token=ed02f64788f25309f24a951cf3cae40e97c41487)](https://partsnap.testspace.com/spaces/276170/current/Code%20Coverage?utm_campaign=metric&utm_medium=referral&utm_source=badge "Code Coverage (branches)") -->

> This is the latest version that is supporting web services and library projects for PARTSNAP LLC.
> To use the original version, invoke cookiecutter with template version 1.0.0

`cookiecutter git@github.com:partsnap/partsnap-cookiecutter-poetry.git -c 1.0.0`

> For more information or to report any bug, see [DOPS-19 PartSnap Cookie Cutter Improvements](https://partsnap.atlassian.net/browse/DOPS-19)

**NOTE**

This version is a fork from https://github.com/fpgmaas/cookiecutter-poetry. See [Acknowledgements](#acknowledgements)

To view the original documentation click [here](https://fpgmaas.github.io/cookiecutter-poetry/)

---

- **Github repository**: <https://github.com/partsnap/partsnap-cookiecutter-poetry/>
- **Documentation** <https://partsnap-llc-partsnap-cookiecutter-poetry.readthedocs-hosted.com/en/latest/>

## System Configuration (One Time)

[NIX Installation and Setup](https://partsnap.atlassian.net/wiki/spaces/SD/pages/113410049/NIX)

install cookiecutter

```bash
pipx install cookiecutter
```

## Quickstart

---

**NOTE**: Make sure you have performed the
[initial system configuration](#system-configuration-one-time) **once**.

---

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```
cookiecutter https://github.com/partsnap/partsnap-cookiecutter-poetry.git
```

Create a repository on GitHub, and then run the following commands:

```bash
cd <project_name>
git init -b main
git add .
```

After project creation open your project and install the environment and run the pre-commit hooks:

```bash
make install
make check
make check
make test
make docs
```

`make check` will need to be run twice since file linting pre-commit will change files based on how long your project_slug will be.
This is mainly due to imports being too long or name of project_slug being used within code.

To check if Docker is setup properly run these commands:

```bash
make docker-build
make docker-start
make docker-stop
```

Once you have installed the environment and run the pre-commit hooks,
run the following commands, replacing `<project-name>`, with the name that you gave the Github repository:

```bash
git add poetry.lock
git commit -am "Init commit"
git remote add origin git@github.com:partsnap/<project_name>.git
```

Before pushing your code, you will need to setup Testspace for the project. You just need to go to [Testspace PartSnap LLC](https://partsnap.testspace.com/).
Top right "+ New Project" button and tie the repository you just created with Testspace. Your github repository for this project must be created within
our Github Partsnap Org before you can link Testspace. If you don't see the "+ New Project" button at the top right, you will need to be given admin access
to your Testspace account.

Once you link your repository to Testspace next you need to go and get your Testspace Access Token.
To do this go to the top right where your name is, click your name and then click edit.
Below your github username is your Access Token from Testspace.
Keep this open so you can copy the Access Token to your clipboard for the next step.

Lastly go to the repository you just created and go to the Settings tab.
On the left hand side there should be a Security section with a "Secrets and variables" dropdown.
Once the dropdown is open go to Actions, you want to click "New repository secret" in green.
For the name of the secret it needs to be called:

```
TESTSPACE_TOKEN
```

For the secret place the Access Token you got from Testspace here. Click "Add secret" when you are done.

Once you have tied Testspace to your project, now you are ready to push:

```bash
git push -u origin main
```

By default this template supports github workflows and one of the workflows is Testspace.
This means if you don't have Testspace linked, the push will work, the problem happens for
future pushes when you do PR requests on the repository, it will not let you merge into main.

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](./features/publishing.md#set-up-for-pypi). For activating the automatic documentation with MkDocs, see [here](./features/mkdocs.md#enabling-the-documentation-on-github). To enable the code coverage reports, see [here](./features/codecov).

## Testspace Integration

This template supports Testspace from the start. [Testspace PartSnap LLC](https://partsnap.testspace.com/)
Make sure your project github repository is on our Testspace.

(Optional): Documenation in the README.md for Testspace badges on project creation is commented out by default and will have to be manually updated once you connect the new repoistory to Testspace. You will want to update the `index.md` file as well in the `docs folder` with the badges if you decide to add them.

## Read the Docs Support

Read the Docs support are included in this template. Once you create your project,
go to this link [PartSnap LLC Read the Docs Dashboard](https://readthedocs.com/dashboard/)
Make sure you are logged in with your partsnap.io google account. Click the import button to import your repository.
You will need to make sure you sync with your github account that is tied with the PartSnap LLC Org.
Once all the Org repositories are in sync, find the respository you created with the template.
Go through the options just clicking continue for everything.
Once done run a build on the doc and it will build the Read the Doc for you.

(Optional): Documentation in the README.md for the Read the Docs badge on project creation is commented out by default and will have to be manually updated after you run the build for Read the Docs. You will want to update the `index.md` file as well in the `docs folder` with the badges if you decide to add them.

## Useful Tutorials

### In Depth Setup

If you want more configuration to your project on initial creation, check this [tutorial](./tutorials/bootstrap.md)

### Integration with PyCharm

If you are using NixOS and Pycharm, check this [tutorial](./tutorials/pycharm_nixos.md)
for setting things up.

### Mermaid Diagram and Charting System

Check this [tutorial](./tutorials/mermaid.md)

## Features

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/fpgmaas/deptry/) and [prettier](https://prettier.io/)
- Publishing to [Pypi](https://pypi.org) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)
- Containerization with [Docker](https://www.docker.com/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

An example of a repository generated with this package can be found [here](https://github.com/fpgmaas/cookiecutter-poetry-example).

## Reference

- [Developing Python and Rust projects on NixOS using IntelliJ IDEA and PyCharm](https://o.librepush.net/solutions/nix/developing-python-rust-projects-on-nixos/)
- [Package and deploy Python apps faster with Poetry and Nix](https://www.youtube.com/watch?v=TbIHRHy7_JM)

## Acknowledgements

This project is a fork from [Florian Maas](https://github.com/fpgmaas) which is
partially based on [Audrey Feldroy's](https://github.com/audreyfeldroy) great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
