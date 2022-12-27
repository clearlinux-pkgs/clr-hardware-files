#!/usr/bin/bash
set -e -o pipefail

curl -sSf -L https://pciids.sourceforge.net/v2.2/pci.ids -o pci.ids
curl -sSf -L http://www.linux-usb.org/usb.ids -o usb.ids
curl -sSf -L https://raw.githubusercontent.com/vcrhonek/hwdata/master/pnp.ids -o pnp.ids
git diff --exit-code pci.ids usb.ids pnp.ids && exit

make bumpnogit
git commit -m "device ID updates" pci.ids usb.ids pnp.ids *.spec release
make koji-nowait
