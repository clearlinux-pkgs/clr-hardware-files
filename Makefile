PKG_NAME := clr-hardware-files
VERSION := 1

include ../common/Makefile.common

update:
	echo Downloading new content
	curl -sSf http://pciids.sourceforge.net/v2.2/pci.ids -o pci.ids
	curl -sSf http://www.linux-usb.org/usb.ids -o usb.ids
	git diff --exit-code pci.ids usb.ids || bash ./update.sh
