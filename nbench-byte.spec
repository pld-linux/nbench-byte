Summary:	test
Summary(pl):	test
Name:		nbench-byte
Version:	2.2.1
Release:	0
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Applications/Console
#Vendor:		-
#Icon:		-
Source0:	ftp://ftp.tux.org/pub/tux/mayer/%{name}-%{version}.tar.gz
#Source0-md5:	92694db00b9698f4f7525e0580ed876b
URL:		 http://www.tux.org/~mayer/linux/bmark.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is port to Linux/Unix of release 2 of BYTE Magazine's BYTEmark benchmark 
program (previously known as BYTE's Native Mode Benchmarks). These are Native 
Mode (a.k.a. Algorithm Level) tests; benchmarks designed to expose the capabi-
lities of a system's CPU, FPU, and memory system. Read all about it at BYTE's
benchmark page.

The benchmark program takes less than 10 minutes to run (on most machines)
and compares the system it is run on to two benchmark systems (a Dell
Pentium 90 with 256 KB cache running MSDOS and an AMD K6/233 with 512 KB
cache running Linux). The archive contains the complete source,
documentation, and a binary (Linux elf). The source has been successfully
compiled on various operating systems, including SunOS, DEC Unix 4.0, DEC
OSF1, HP-UX, DEC Ultrix, MS-DOS, and of course Linux.

%description -l pl
Jest to Linuksowy/Uniksowy port wydania 2 benchmarka magazunu BYTE. To s± 
testy algorytmiczne, zaprojektowane aby sprawdziæ mo¿liwo¶ci CPU, FPU i pod-
systemu pamiêci.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/usr/bin/

install nbench $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changes RESULTS bdoc.txt
%attr(755,root,root) %{_bindir}/*
