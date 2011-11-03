# revision 15878
# category Package
# catalog-ctan /tds
# catalog-date 2009-10-10 00:51:28 +0200
# catalog-license other-free
# catalog-version 1.1
Name:		texlive-tds
Version:	1.1
Release:	1
Summary:	The TeX Directory Structure standard
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/tds
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tds.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines a structure for placement of TeX-related files on an
hierarchical file system, in a way that is well-defined, and is
readily implementable.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/tds/ChangeLog
%doc %{_texmfdistdir}/doc/generic/tds/Makefile
%doc %{_texmfdistdir}/doc/generic/tds/README
%doc %{_texmfdistdir}/doc/generic/tds/index.html
%doc %{_texmfdistdir}/doc/generic/tds/tds.dvi
%doc %{_texmfdistdir}/doc/generic/tds/tds.html
%doc %{_texmfdistdir}/doc/generic/tds/tds.pdf
%doc %{_texmfdistdir}/doc/generic/tds/tds.sed
%doc %{_texmfdistdir}/doc/generic/tds/tds.tex
%doc %{_texmfdistdir}/doc/generic/tds/tds2texi.el
%doc %{_texmfdistdir}/doc/generic/tds/tdsguide.cls
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
