# pre-commit-hooks
Pre-commit hooks for PCDS projects (https://pre-commit.com/)


**To install pre-commit on your machine,** use `$ brew install pre-commit` 
OR `$ pip install pre-commit`


### To install pre-commit hooks to a local repository:

If .pre-config-config.yaml does not already exist in the repository, copy
the appropriate file from this repository to the top-level of your local
repository and commit the addition.

Once the file is there, run the following from inside your repository:
```bash
$ pre-commit install          # install for this repo based on the config
$ pre-commit run --all-files  # run on everything
$ pre-commit run              # run on staged
$ git commit -am "test"       # run pre-commit and - if successful - commit
```
