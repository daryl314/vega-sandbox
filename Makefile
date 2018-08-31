# allow bash syntax
SHELL := /bin/bash

# targets without associated files
.PHONY: offline serve clean

# spin up web server on localhost
serve:
	python -c 'import socket, BaseHTTPServer as bhs, SimpleHTTPServer as shs; s=socket.socket(); s.bind(("", 0)); port = s.getsockname()[1]; s.close(); print("Serving on localhost:%d" % port); bhs.HTTPServer(("127.0.0.1", port), shs.SimpleHTTPRequestHandler).serve_forever()'

# create offline version
offline: index.html.bak

# convert hyperlinks to offline references
index.html.bak: jslib
	sed -i.bak -e 's#src="[^"]*/#src="jslib/#' index.html

# download referenced libraries
jslib:
	mkdir -p jslib
	if [[ -f index.html.bak ]]; then INFILE=index.html.bak; else INFILE=index.html; fi; pushd jslib >/dev/null; for SRC in $$(grep "src=" ../$$INFILE | sed -e "s/.*src=\"//" -e "s/\".*//"); do wget $$SRC; done; popd >/dev/null

# cleanup
clean:
	if [[ -f index.html.bak ]]; then command mv index.html.bak index.html; fi
	rm -rf jslib
