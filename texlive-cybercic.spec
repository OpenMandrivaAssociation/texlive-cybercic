%global tl_name cybercic
%global tl_revision 37659

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Controls in Contents for the cyber package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cybercic
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cybercic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cybercic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cybercic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is used in concert with the cyber package to make documents
with annotations of compliance with cybersecurity requirements. "cic"
stands for "Controls in Contents", and when you include this package,
some notations of compliance are added to section names as seen in the
table of contents of the final document. It also makes your document
more brittle in unexpected ways: for example, when you use cybercic in
the same document as hyperref, you cannot use any formatting in your
section titles. So don't use cybercic unless you need to.

