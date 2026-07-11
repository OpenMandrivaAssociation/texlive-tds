%global tl_name tds
%global tl_revision 64477

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	The TeX Directory Structure standard
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tds
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tds.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines a structure for placement of TeX-related files on an
hierarchical file system, in a way that is well-defined, and is readily
implementable.

