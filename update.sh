#!/usr/bin/bash
set -e -o pipefail

curl -sSf https://pciids.sourceforge.net/v2.2/pci.ids -o pci.ids
curl -sSf http://www.linux-usb.org/usb.ids -o usb.ids
git diff --exit-code pci.ids usb.ids && exit

make bumpnogit
git commit -m "device ID updates" pci.ids usb.ids *.spec release
make koji-nowait
