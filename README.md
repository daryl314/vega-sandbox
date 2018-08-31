# Vega Sandbox #

This is a basic "hello world" for using vega.  A sample specification `bar.json`
is provided from the vega site.  Copy your own specification to this directory
to use it.

Usage:

* Start web server on localhost with `make serve` or just `make`.  Note the
  address in the console.  Browse to `localhost:PORT?spec=bar.json` to show the
  example specification
* View multiple specifications with `?spec=spec1.json,spec2.json,spec3.json`
* Create an offline version with `make offline`.  Revert with `make clean`
* Launch the web-based editor with `make edit` (requires yarn to be installed)
