# Test coverage with codecov

A `codecov.yaml` file is created, with the following defaults:

```yaml
# Badge color changes from red to green between 70% and 100%
# PR pipeline fails if codecov falls with 1%

coverage:
  range: 70..100
  round: down
  precision: 1
  status:
    project:
      default:
        target: auto
        threshold: 1%

# Ignoring Paths
# --------------
# which folders/files to ignore
ignore:
  - "foo/bar.py"
```
