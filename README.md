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
    * Put data to be referenced from editor in editor/public

## Copying to a new location ##

* `make clean && cp index.html NEW_LOCATION`
* execute following script to render `bar.json`

```bash
#!/bin/bash
PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
python2 -c "import BaseHTTPServer as bhs, SimpleHTTPServer as shs; bhs.HTTPServer(('127.0.0.1', $PORT), shs.SimpleHTTPRequestHandler).serve_forever()" &
sleep 1
open "http://localhost:$PORT/?spec=bar.json"
```
