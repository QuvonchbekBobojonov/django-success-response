# Create virtual environment
venv:
	python -m venv venv
	source venv/bin/activate && pip install --upgrade pip

# Install dependencies
install:
	pip install -e .

# Build the package
build:
	python setup.py sdist bdist_wheel

# Upload to PyPI (requires twine)
upload:
	twine upload dist/*

# Clean build artifacts
clean:
	rm -rf build/ dist/ your_package.egg-info/

.PHONY: venv install test build upload clean
