### python-documentation-test

This is a test repository to experiment with python documentation generation tools.

#### Installing:

To create sphinx documentation from scratch:
```bash
sphinx-quickstart
```

#### Prerequisites:

Virtual python environment suggested:

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
sudo apt install python3-sphinx-autobuild
```

```bash
python3 -m pip install docs/requirements.txt --break-system-packages
```

#### Usage:

Build locally with sphinx-autobuild:

```bash
sphinx-autobuild docs docs/_build
```

This way you can see the changes in real time.
