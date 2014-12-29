PKG_NAME := clr-hardware-files
VERSION := 1

include ../common/Makefile.common

update:
	echo Downloading new content
	curl http://pciids.sourceforge.net/v2.2/pci.ids	-o pci.ids 
	curl http://www.linux-usb.org/usb.ids -o usb.ids 
	