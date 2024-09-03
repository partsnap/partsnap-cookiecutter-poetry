# Docker Credential Setup

Instructions on how to run docker makefile commands.

Create a `.env` file in the root directory.
Add these two lines into the `.env` file and make sure to change out `your password` with the PS token.

```bash
PS_DOCKERHUB_TOKEN=(--your password goes here--)
PS_PUSH_DOCKERHUB_TOKEN=(--your password goes here--)
```

`PS_DOCKERHUB_TOKEN` is the read only token
`PS_PUSH_DOCKERHUB_TOKEN` is the read and push token

`Note`: The workflow by default will do the push to docker, this is just in case the workflow is breaking and you need a docker push now then later.

Now run the following in the terminal to export the username and token to make it available to the makefile.

```bash
export $(grep -v '^#' .env | xargs)
```

To push the docker image for release you need to do these commands.

```bash
make docker-push-login
make docker-push tag-1.0.0.devX
```
