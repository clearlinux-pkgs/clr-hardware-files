Name:       clr-hardware-files
Summary:    Clear Linux container for pci.ids and similar files
Version:    1
Release:    25
Group:      Development/System
License:    GPL-2.0+
URL:        http://www.clearlinux.org
Source0:    pci.ids
Source1:    usb.ids
AutoReqProv: No

%description
pci.ids and usb.ids files



%prep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/hwdata
cp %{SOURCE0} %{buildroot}/usr/share/hwdata
cp %{SOURCE1} %{buildroot}/usr/share/hwdata

%files
%defattr(-,root,root,-)
/usr/share/hwdata/pci.ids
/usr/share/hwdata/usb.ids

