Name:       clr-hardware-files
Summary:    Clear Linux container for pci.ids and similar files
Version:    1
Release:    433
Group:      Development/System
License:    GPL-2.0+
URL:        https://clearlinux.org
Source0:    pci.ids
Source1:    usb.ids
Source2:    pnp.ids
Source3:    hwdata.pc
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
cp %{SOURCE2} %{buildroot}/usr/share/hwdata
mkdir -p %{buildroot}/usr/share/pkgconfig
cp %{SOURCE3} %{buildroot}/usr/share/pkgconfig

%check
[ -s %{SOURCE0} ]
[ -s %{SOURCE1} ]
[ -s %{SOURCE2} ]
[ -s %{SOURCE3} ]

%files
%defattr(-,root,root,-)
/usr/share/hwdata/pci.ids
/usr/share/hwdata/usb.ids
/usr/share/hwdata/pnp.ids
/usr/share/pkgconfig/hwdata.pc
