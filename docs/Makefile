# Minimal Sphinx Makefile for HTML build

SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: html clean

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)
