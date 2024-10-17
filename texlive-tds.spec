Name:		texlive-tds
Version:	64477
Release:	2
Summary:	The TeX Directory Structure standard
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/tds
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tds.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Defines a structure for placement of TeX-related files on an
hierarchical file system, in a way that is well-defined, and is
readily implementable.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/tds
%doc %{_texmfdistdir}/doc/info/*.info*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
