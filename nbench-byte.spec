Summary:	Port of release 2 of BYTE Magazine's BYTEmark benchmark program
Summary(pl.UTF-8):   Port wydania 2. benchmarka BYTEmark z magazynu BYTE
Name:		nbench-byte
Version:	2.2.2
Release:	2
License:	freely distributable
Group:		Applications/Console
Source0:	ftp://ftp.tux.org/pub/tux/mayer/%{name}-%{version}.tar.gz
# Source0-md5:	174c1917eea8f74bd3e78522592e0658
Patch0:		%{name}-NNET_DAT_path.patch
URL:		http://www.tux.org/~mayer/linux/bmark.html
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
cache running Linux). The original archive contains the complete source,
documentation, and a binary (Linux ELF). The source has been successfully
compiled on various operating systems, including SunOS, DEC Unix 4.0, DEC
OSF1, HP-UX, DEC Ultrix, MS-DOS, and of course Linux.

%description -l pl.UTF-8
Jest to linuksowy/uniksowy port wydania 2. benchmarka magazynu BYTE
(poprzednio znanego jako BYTE's Native Mode Benchmarks). Są to testy
algorytmiczne, zaprojektowane aby sprawdzić możliwości CPU, FPU i
podsystemu pamięci. Można o nich poczytać na stronach BYTE.

Program benchmarka wykonuje się poniżej 10 minut (na większości
maszyn) i porównuje system na którym działa do dwóch innych systemów
(Della z Pentium 90, 256KB cache pod MS DOS-em oraz AMD K6/233 z 512KB
cache pod Linuksem). Oryginalne archiwum zawiera pełne źródła,
dokumentację oraz binarkę (Linux ELF). Źródła kompilują się na wielu
różnych systemach, w tym SunOS, DEC Unix 4.0, DEC OSF1, HP-UX, DEC
Ultrix, MS-DOS i oczywiście Linux.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LINKFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install nbench $RPM_BUILD_ROOT%{_bindir}
install *.DAT $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changes RESULTS bdoc.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
