# pre-commit-hooks
Pre-commit hooks for PCDS projects (https://pre-commit.com/)


### To install pre-commit on your machine:

**On Linux,** use `$ pip install pre-commit` or `conda install pre-commit -c conda-forge` from your favorite python environment.
**On Mac,** use `$ brew install pre-commit`, or follow the Linux instructions.
**On Windows,** set up python either your favorite way or by using https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html, and then follow the Linux instructions.

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

### Issues and client integration

If pre-commit is not an available command, you may need to look into platform-specific configuration. Generally, you'll need to be in a shell environment that has access to python and with pre-commit installed as directed in the above sections. Typical issues include a misconfigured PATH variable and not having python available. For specific help on integrating with various clients and on various operation systems, see the sections below. If you solve other client integration problems for your favorite workflow, please expand this section in a pull request.

#### Shell Integration on Windows

- Make sure git is set up for normal shell use (a git installation option) if you want to use cmd or powershell
- I have had success using the Anaconda Powershell Prompt and a conda environment with pre-commit installed

#### Git Bash Integration on Windows

- Add the following to your `~/.bash_profile`: `alias python='winpty python'`, to allow python to run without hanging.
- If using conda, run `$ conda init bash`, using the conda.exe in your `~/miniconda3/scripts` folder. You may also want to set this up to `conda activate` your `pre-commit` environment.
- restart your shell after doing the above

#### TwinCAT Integrated Git on Windows

- Someone needs to investigate this one. I don't have this running locally yet and am happy enough with the shells for now.

#### VSCode Integration on Windows

- Someone needs to figure out how to get the git extension to work here.
- If your shell integration works, you can connect to this in the integrated terminal by setting `terminal.integrated.shellArgs.windows` to the same same arguments as used in the Anaconda Powershell prompt shortcut's properties.
