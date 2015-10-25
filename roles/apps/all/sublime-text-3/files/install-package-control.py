#! /usr/bin/env python3
import urllib.request
import os
import hashlib
import sys

h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'
pf = 'Package Control.sublime-package'
ipp = os.getenv("HOME") + '/.config/sublime-text-3/Installed Packages'
urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) )
by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read()
dh = hashlib.sha256(by).hexdigest()
if dh != h:
    print('Error validating download (got %s instead of %s), please try manual install' % (dh, h))
    sys.exit(1)
else:
    open(os.path.join( ipp, pf), 'wb' ).write(by)
    sys.exit(0)
