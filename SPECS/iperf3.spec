Name:           iperf3
Version:        3.5
Release:        7%{?dist}
Summary:        Measurement tool for TCP/UDP bandwidth performance

Group:          Applications/Internet
License:        BSD
URL:            http://github.com/esnet/iperf
Source0:        http://downloads.es.net/pub/iperf/iperf-%{version}.tar.gz
BuildRequires:  libuuid-devel git-core gcc make
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel

Patch0002:	0002-udp-counters-manpage.patch
Patch0003:	0003-covscan-sctp.patch
Patch0004:	0004-memory-crash.patch

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, data-gram loss.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git -n iperf-%{version}

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall -C src INSTALL_DIR="%{buildroot}%{_bindir}"
mkdir -p %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_libdir}/libiperf.la

%files
%defattr(-,root,root,-)
%doc README.md LICENSE RELEASE_NOTES
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz
%{_bindir}/iperf3
%{_libdir}/*.so.*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files          devel
%defattr(-,root,root,-)
%{_includedir}/iperf_api.h
%{_libdir}/*.so

%changelog
* Wed Jul 26 2023 Michal Ruprich <mruprich@redhat.com> - 3.5-7
- Resolves: #2224443 - memory allocation hazard and crash

* Tue May 05 2020 Michal Ruprich <michalruprich@gmail.com> - 3.5-6
- Related: #1665142 - Fixing a couple of covscan issues

* Fri Mar 13 2020 Michal Ruprich <michalruprich@gmail.com> - 3.5-5
- Related: #1665142 - Removing patch that deletes sctp from manpage

* Mon Mar 09 2020 Michal Ruprich <mruprich@redhat.com> - 3.5-4
- Resolves: #1665142 - [RFE] enable SCTP support in iperf3
- Resolves: #1656429 - option --udp-counters-64bit shown in --help output but not in man page
- Resolves: #1700497 - [RFE] enable SSL support in iperf3

* Sun Dec 16 2018 Michal Ruprich <mruprich@redhat.com> - 3.5-3
- Related: #1647413 - Removing nstreams and xbind from man since these are SCTP-related options

* Thu Nov 22 2018 Michal Ruprich <mruprich@redhat.com> - 3.5-2
- Related: #1647413 - adding some BuildRequires

* Thu Nov 22 2018 Michal Ruprich <mruprich@redhat.com> - 3.5-2
- Resolves: #1647413 - iperf3 with option --sctp in client mode fails with error 'iperf3: unrecognized option --sctp'

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 3.5-1
- Update to 3.5. Fixes bug #1551166

* Fri Feb 16 2018 Kevin Fenzi <kevin@scrye.com> - 3.4-1
- Upgrade to 3.4. Fixes bug #1545468

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Kevin Fenzi <kevin@scrye.com> - 3.3-1
- Update to 3.3. Fixes bug #1508669

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Kevin Fenzi <kevin@scrye.com> - 3.2-1
- Update to 3.2. Fixes bug #1465195

* Wed Mar 08 2017 Kevin Fenzi <kevin@scrye.com> - 3.1.7-1
- Update to 3.1.7. Fixes bug #1429901

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Kevin Fenzi <kevin@scrye.com> - 3.1.6-1
- Update to 3.1.6. Fixes bug #1418879

* Fri Jan 13 2017 Kevin Fenzi <kevin@scrye.com> - 3.1.5-1
- Update to 3.1.5. Fixes bug #1412848

* Sat Nov 05 2016 Kevin Fenzi <kevin@scrye.com> - 3.1.4-1
- Update to 3.1.4. Fixes bug #1390396

* Wed Jun 08 2016 Kevin Fenzi <kevin@scrye.com> - 3.1.3-1
- Update to 3.1.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Susant Sahani <ssahani@gmail.com> 3.1b3
- Update to 3.1b3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Susant Sahani <ssahani@gmail.com> 3.0.11-1
- Update to 3.0.11

* Sat Dec 20 2014 Susant Sahani <ssahani@redhat.com> 3.0.10-1
- Update to 3.0.10

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Susant Sahani <ssahani@redhat.com> 3.0.6-1
- Update to 3.0.6

* Thu Jun 19 2014 Susant Sahani <ssahani@redhat.com> 3.0.5-1
- Update to 3.0.5

* Tue Jun 10 2014 Susant Sahani <ssahani@redhat.com> - 3.0.3-5
- fix compilation BZ #1106803

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 2 2014 François Cami <fcami@fedoraproject.org> - 3.0.3-3
- Drop static library support (#1081486).
- iperf3-devel subpackage must require iperf3.
- iperf3-devel should only contain the unversioned shared library.
- Call ldconfig since we are installing a shared library now.
- Removed INSTALL file.

* Wed Apr 2 2014 Susant Sahani <ssahani@redhat.com> 3.0.3-2
- Moved static library to devel section only .

* Sun Mar 30 2014 Susant Sahani <ssahani@redhat.com> 3.0.3-1
- Update to 3.0.3 and added devel rpm support

* Tue Mar 11 2014 Susant Sahani <ssahani@redhat.com> 3.0.2-1
- Update to 3.0.2

* Tue Jan 14 2014 Susant Sahani <ssahani@redhat.com> 3.0.1-1
- Update to 3.0.1

* Fri Oct 25 2013 Steven Roberts <strobert@strobe.net> 3.0-1
- Update to 3.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.5.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 Kevin Fenzi <kevin@scrye.com> 3.0-0.4.b5
- Update to 3.0b5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.3.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.2.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.1.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 06 2011 G.Balaji <balajig81@gmail.com> 3.0b4-2
- Changed the Spec name, removed static libs generation and devel
- package.

* Sat Mar 26 2011 G.Balaji <balajig81@gmail.com> 3.0b4-1
- Initial Version
