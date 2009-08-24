Summary:	FUSE filesystem using MySQL as a storage
Name:		fuse-mysqlfs
Version:	0.4.0
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/project/mysqlfs/mysqlfs/%{version}/mysqlfs-%{version}.tar.bz2
# Source0-md5:	7998aa0e11fc50e50b54c02994110e72
URL:		http://sourceforge.net/projects/mysqlfs/
BuildRequires:	libfuse-devel
BuildRequires:	mysql-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQLfs is Linux userspace filesystem which stores data in a MySQL
database. It uses FUSE to interface with the kernel.

%prep
%setup -q -n mysqlfs-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mysqlfs
%{_datadir}/mysqlfs-%{version}/install.sql
%{_datadir}/mysqlfs-%{version}/schema.sql
