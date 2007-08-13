%define rname lz11

Summary:	Printer Drivers for the Lexmark Z11 and Compaq IJ300 printer
Name:		cups-drivers-%{rname}
Version:	1.2
Release:	%mkrel 1
License:	GPL
Group:		File tools
URL:		http://sourceforge.net/projects/lz11/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/lz11/lz11-V2-%{version}.tar.gz
Conflicts:	cups-drivers-2006 cups-drivers-2007
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A Linux printer driver/filter for the Lexmark Z11 and the Compaq IJ300 printer,
supporting color and b/w printing, variable page size and more.

This package contains CUPS drivers (PPD) for the following printers:

 o Compaq IJ300
 o Lexmark Z11

%prep

%setup -q -n lz11-V2-%{version}

%build
make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/LexmarkZ11
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/cups/model

install -m0755 cZ11-V2 %{buildroot}%{_bindir}/
install -m0755 cZ11 %{buildroot}%{_bindir}/
install -m0755 cZ11-bit* %{buildroot}%{_bindir}/
install -m0755 lz11.[^c]* %{buildroot}%{_bindir}/
install -m0644 lz11.conf %{buildroot}/etc/LexmarkZ11/
install -m0644 *.ppd %{buildroot}%{_datadir}/cups/model/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog README release-notes-*
%attr(0644,root,sys) %config(noreplace) %{_sysconfdir}/LexmarkZ11/lz11.conf
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_datadir}/cups/model/Lexmark-Z11-lz11-V2.ppd
%attr(0644,root,root) %{_datadir}/cups/model/Compaq-IJ300-lz11-V2.ppd
