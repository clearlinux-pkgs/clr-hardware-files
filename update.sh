#!/usr/bin/bash
git commit -m "device ID updates" pci.ids usb.ids
make bump
make koji-nowait
