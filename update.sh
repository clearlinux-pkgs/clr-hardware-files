#!/usr/bin/bash
make bumpnogit
git commit -m "device ID updates" pci.ids usb.ids *.spec release
make koji-nowait
