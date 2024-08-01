# Getting Started

This page contains a complete tutorial on how to create your project.

## Step 1: Install poetry

To start, we will need to install `poetry`. The instructions to install poetry can be found
[here](https://python-poetry.org/docs/). After installing, it is recommended to run

```bash
poetry config virtualenvs.in-project true
```

which will by default create new virtual environments in `./.venv`
whenever you create them with `poetry init`.

## Step 2: Install pyenv (Optional)

I would recommend to use `pyenv` for managing your different Python versions. However, if you prefer another method of
managing your Python versions, feel free to skip this step and continue to [step 3](#step-3-generate-your-project).

The instructions to install pyenv can be found [here](https://github.com/pyenv/pyenv). The instructions to install
poetry can be found [here](https://python-poetry.org/docs/).

Install a version of Python with pyenv. To see a list of available
versions, run:

```bash
pyenv install --list
```

Select a version and install it with

```bash
pyenv install -v 3.9.7
```

Replacing `3.9.7` with a version of your choosing.

## Step 3: Generate your project

```bash
pip install cookiecutter-poetry
cookiecutter https://github.com/partsnap/partsnap-cookiecutter-poetry.git
```

## Step 4: Set up your Github repository

Create an empty [new repository](https://github.com/new) on Github. Give
it a name that only contains alphanumeric characters and optionally `-`.
DO NOT check any boxes under the option `Initialize this repository
with`.

## Step 5: Upload your project to Github

Run the following commands:

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

## Step 6: Activate your environment

If you are using `pyenv`, you might want to set the local `python` version to be used:

```bash
pyenv local x.y.z
```

Install and activate the `poetry` environment by running:

```bash
make install
poetry shell
```

## Step 7: Sign up to codecov.io

If you enabled code coverage with codecov for your project, you should sign up with your GitHub account at [codecov.io](https://about.codecov.io/language/python/)

## Step 8: Configure your repository secrets

If you want to deploy your project to Pypi or Artifactory using the
Github Actions, you will have to set some repository secrets. For
instructions on how to do that, see [here](../features/publishing.md#set-up-for-pypi) for PyPi, or
[here](../features/publishing.md#set-up-for-artifactory) for Artifactory.

## Step 9: Create a new release

To trigger a new release, navigate to your repository on GitHub, click `Releases` on the right, and then select `Draft
a new release`. If you fail to find the button, you could also directly visit
`https://github.com/<username>/<repository-name>/releases/new`.

Give your release a title, and add a new tag in the form `*.*.*` where the
`*`'s are alphanumeric. To finish, press `Publish release`.

## Step 10: Enable your documentation

In your repository, navigate to `Settings > Code and Automation > Pages`. If you succesfully created a new release,
you should see a notification saying ` Your site is ready to be published at https://<author_github_handle>.github.io/<project_name>/`.

To finalize deploying your documentation, under `Source`, select the branch `gh-pages`.

## Step 11: You're all set!

That's it! I hope this repository saved you a lot of manual configuration. If you have any improvement suggestions, feel
free to raise an issue or open a PR on Github!
