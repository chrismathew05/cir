.. Circuit Grapher documentation master file, created by
   sphinx-quickstart on Tue Jul 19 12:40:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Circuit Grapher's documentation!
===========================================
**Circuit Grapher** is a tool used at Intelline to document circuits and explore the relationships between components.

The code for this project is available on `Github <https://github.com/chrismathew05/cir>`_.

.. note::

   This project is under active development.

Build
-----

1. Fork and clone repo: `https://github.com/chrismathew05/cir <https://github.com/chrismathew05/cir>`_
2. Create and activate python virtual environment `venv`.
3. Create a local `.gitignore` and `.env` file (unused for now).
4. Provide build script permissions: `chmod -R 777 build.sh`
5. Run the build script and ensure all tests pass: `./build.sh`.

Usage
-----

1. Save XML (e.g. `test.xml`) + DTD (e.g. `test.dtd`) files in the `circuit` directory.
2. Restart `main.ipynb`.
3. Use the notebook to construct/explore your circuit.


Code
-----

.. toctree::
   :maxdepth: 2

   graph
   parse