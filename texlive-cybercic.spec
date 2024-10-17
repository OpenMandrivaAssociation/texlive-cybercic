Name:		texlive-cybercic
Version:	37659
Release:	2
Summary:	"Controls in Contents" for the cyber package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cybercic
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cybercic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cybercic.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cybercic.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is used in concert with the cyber package to make
documents with annotations of compliance with cybersecurity
requirements. "cic" stands for "Controls in Contents", and when
you include this package, some notations of compliance are
added to section names as seen in the table of contents of the
final document. It also makes your document more brittle in
unexpected ways: for example, when you use cybercic in the same
document as hyperref, you cannot use any formatting in your
section titles. So don't use cybercic unless you need to.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cybercic
%{_texmfdistdir}/tex/latex/cybercic
%doc %{_texmfdistdir}/doc/latex/cybercic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
