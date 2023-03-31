%define rname lz11

Summary:	Printer Drivers for the Lexmark Z11 and Compaq IJ300 printer
Name:		cups-drivers-%{rname}
Version:	1.2
Release:	24
License:	GPLv2
Group:		System/Printing
URL:		http://sourceforge.net/projects/lz11/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/lz11/lz11-V2-%{version}.tar.gz
Patch0:		lz11-V2-1.2-format_not_a_string_literal_and_no_format_arguments.diff

%description
A Linux printer driver/filter for the Lexmark Z11 and the Compaq IJ300 printer,
supporting color and b/w printing, variable page size and more.

This package contains CUPS drivers (PPD) for the following printers:

 o Compaq IJ300
 o Lexmark Z11

%prep

%setup -qn lz11-V2-%{version}
%patch0 -p0

%build
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_sysconfdir}/LexmarkZ11
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/cups/model

install -m0755 cZ11-V2 %{buildroot}%{_bindir}/
install -m0755 cZ11 %{buildroot}%{_bindir}/
install -m0755 cZ11-bit* %{buildroot}%{_bindir}/
install -m0755 lz11.[^c]* %{buildroot}%{_bindir}/
install -m0644 lz11.conf %{buildroot}/etc/LexmarkZ11/
install -m0644 *.ppd %{buildroot}%{_datadir}/cups/model/

%files
%doc ChangeLog README release-notes-*
%attr(0644,root,sys) %config(noreplace) %{_sysconfdir}/LexmarkZ11/lz11.conf
%{_bindir}/*
%{_datadir}/cups/model/Lexmark-Z11-lz11-V2.ppd*
%{_datadir}/cups/model/Compaq-IJ300-lz11-V2.ppd*

