# CIRCUIT GRAPHER

This application is used at Intelline to document circuits and explore the relationships between components.

## Build

1. Fork and clone repo: `https://github.com/chrismathew05/cir`
2. Create and activate python virtual environment `venv`.
3. Create a local `.gitignore` and `.env` file (unused for now).
4. Install requirements: `pip install -r requirements-prod.txt`
5. Provide build script permissions: `chmod -R 777 build.sh`
6. Run the build script and ensure all tests pass: `./build.sh`.

## Usage

1. Save XML (e.g. `test.xml`) + DTD (e.g. `test.dtd`) files in the `circuit` directory.
2. Restart `main.ipynb`.
3. Use the notebook to construct/explore your circuit.

## TODO

- [ ] Complete sphinx documentation
- [ ] Unit test cases
- [ ] Finish constructiong circuit XML + DTD
