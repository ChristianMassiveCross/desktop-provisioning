#! /usr/bin/env python3
import urllib.request
import os
import hashlib

h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'
pf = 'Package Control.sublime-package'
ipp = os.getenv("HOME") + '/.config/sublime-text-3/Installed Packages'
urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) )
by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read()
dh = hashlib.sha256(by).hexdigest()
print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
