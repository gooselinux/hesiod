Name: hesiod
Version: 3.1.0
Release: 19%{?dist}
Source: ftp://athena-dist.mit.edu/pub/ATHENA/hesiod/hesiod-%{version}.tar.gz
Patch1: hesiod-3.1.0-env.patch
Patch2: hesiod-3.1.0-str.patch
Patch3: hesiod-3.1.0-dnsparse.patch
Patch4: hesiod-3.1.0-libresolv.patch
Patch5: hesiod-3.1.0-perms.patch
Summary: Shared libraries for querying the Hesiod naming service
Group: System Environment/Libraries
License: MIT
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, automake, libtool

%description
Hesiod is a system which uses existing DNS functionality to provide access
to databases of information that changes infrequently.  It is often used to
distribute information kept in the /etc/passwd, /etc/group, and /etc/printcap
files, among others.

%package devel
Summary: Development libraries and headers for Hesiod
Group: Development/Libraries
Requires: hesiod = %{version}-%{release}

%description devel
Hesiod is a system which uses existing DNS functionality to provide access
to databases of information that changes infrequently.  It is often used to
distribute information which might otherwise kept in the /etc/passwd,
/etc/group, and /etc/printcap files over a network, eliminating the need to
ensure the files are synchronized among multiple hosts.  This package contains
the header files and libraries required for building programs which use Hesiod.

%changelog
* Fri Feb 19 2010 Nalin Dahyabhai <nalin@fedoraproject.org> - 3.1.0-19
- fix the release number noted for the previous changelog entry (#225884)
- remove unapplied "classes" patch (#225884)

* Wed Jan 13 2010 Nalin Dahyabhai <nalin@fedoraproject.org> - 3.1.0-18
- adjust buildroot location (guidelines)
- disable static libraries (guidelines)
- tweak default payload attributes (guidelines)

* Tue Oct 13 2009 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-17
- add a disttag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  2 2008 Nalin Dahyabhai <nalin@fedoraproject.org> - 3.1.0-14
- adjust the package summary

* Tue Jul 22 2008 Nalin Dahyabhai <nalin@fedoraproject.org> - 3.1.0-13
- rebuild

* Thu Jun 12 2008 Nalin Dahyabhai <nalin@fedoraproject.org> - 3.1.0-12
- call aclocal directly, because autoreconf didn't see the magic comment in
  the distributed version of aclocal.m4 which made it look like it was safe
  to generate a new one (#449550)

* Mon Jun  2 2008 Nalin Dahyabhai <nalin@fedoraproject.org> - 3.1.0-11
- force autoreconf to overwrite files (should fix #449550)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1.0-10
- Autorebuild for GCC 4.3

* Wed Aug 22 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-9
- rebuild

* Mon Jul 17 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-8
- rebuild

* Fri Jul  7 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-7
- use the system libtool to consistently link libhesiod.la with libresolv

* Fri Jul  7 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-6
- run autoreconf instead of autoconf after untarring so that we get a
  config.h.in which suits the changes we make to configure.in (part of #197938)

* Tue Jun 20 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-5
- don't override libtool's defaults for permissions on its .la file, because
  we don't get debuginfo if the execute bit isn't set (pjones, in #190219)

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 3.1.0-4
- rebuild for -devel deps

* Thu Mar 30 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-3
- no, we really did need that patch

* Thu Mar 30 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-2
- drop a no-longer-needed patch for detecting libresolv properly

* Thu Mar 30 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-1
- update to 3.1.0 (#187372)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0.2-31.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0.2-31.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-31
- rebuild

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Oct 19 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add a %%clean specfile target

* Mon Jun 16 2003 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-28
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 27 2003 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-26
- link libhesiod with libresolv on all platforms

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 3.0.2-25
- rebuilt

* Fri Jan 10 2003 Phil Knirsch <pknirsch@redhat.com> 3.0.2-24
- Fixed wrong .so name for s390/s390x.

* Fri Jan 10 2003 Phil Knirsch <pknirsch@redhat.com> 3.0.2-23
- Build shared lib correctly on s390 and s390x (with gcc -shared -fPIC).

* Wed Sep 24 2002 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-22
- look harder for res_mkquery() in libresolv

* Wed Aug 21 2002 Nalin Dahyabhai <nalin@redhat.com>
- don't choke on large response packets

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 16 2002 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-19
- rebuild in new environment

* Mon Apr 15 2002 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-18
- add missing post/postun calls to ldconfig

* Wed Feb 20 2002 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-17
- rebuild in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Oct 26 2001 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-15
- actually set the soname in the shared library (ld doesn't automatically
  set the soname to the output file's name, oops)

* Fri Oct  5 2001 Nalin Dahyabhai <nalin@redhat.com> 3.0.2-14
- on second thought, put the shared library back in, using a soversion of 0
  to have a chance at providing compatibility with apps linked dynamically
  on other distributions
- make -devel depend on the same version of the main package

* Wed Oct  3 2001 Nalin Dahyabhai <nalin@redhat.com>
- remove the shared library patch -- different packages with shared libraries
  tend to use different sonames, so we'd run inevitably run into problems

* Thu Aug 21 2001 Nalin Dahyabhai <nalin@redhat.com>
- remove pre and post scripts -- authconfig handles that stuff now
- add the hesiod man page back in, as bind-devel doesn't provide it any more

* Wed Jan 17 2001 Jeremy Katz <jlkatz@eos.ncsu.edu>
- hesiod-devel requires hesiod (bug #128)

* Thu Sep 14 2000 Jeremy Katz <jlkatz@eos.ncsu.edu>
- remove hesiod man page from hesiod-devel as it conflicts with the one 
  from bind-devel

* Thu Sep 14 2000 Jeremy Katz <jlkatz@eos.ncsu.edu>
- use rpm macros where possible and FHS-ify
- split into main and devel packages
- add back requires for nscd

* Fri Jul 28 2000 Jeremy Katz <jlkatz@eos.ncsu.edu>
- rebuild in new environment

* Thu Mar 16 2000 Jeremy Katz <jlkatz@unity.ncsu.edu>
- rebuild in new environment

* Thu Sep  2 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- removed dependency on nscd
- changed requires: nscd back to caching-nameserver

* Mon May 17 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- started changelog
- moved addition of hesiod to nsswitch.conf to this package because we
  no longer use a separate libnss_hesiod.so
- changed requires: caching-nameserver to nscd
- added post-install script snippet to activate nscd on install

%prep
%setup -q
%patch1 -p1 -b .env
%patch2 -p1 -b .str
%patch3 -p1 -b .dnsparse
%patch4 -p1 -b .libresolv
%patch5 -p1 -b .perms
libtoolize -f -i
aclocal
autoconf -f -i

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README NEWS
%{_libdir}/libhesiod.so.*
%{_mandir}/man5/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libhesiod.so
%{_includedir}/hesiod.h
%{_mandir}/man3/*
