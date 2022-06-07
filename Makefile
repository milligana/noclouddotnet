VERSION=$(shell python3 setup.py --version)

test:
	tox

# hmmm - release to pypi so rtd can install wheel to correctly generate docs
release: clean
	python3 setup.py sdist bdist_wheel
	twine-3 upload dist/*
	git tag --force -a v$(VERSION) -m "release $(VERSION)"
	git push origin v$(VERSION) 

clean:
	rm -rf dist/*
