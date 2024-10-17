Name:		texlive-translator
Version:	59412
Release:	2
Summary:	Easy translation of strings in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/translator
License:	lppl gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translator.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translator.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides a flexible mechanism for
translating individual words into different languages. For
example, it can be used to translate a word like "figure" into,
say, the German word "Abbildung". Such a translation mechanism
is useful when the author of some package would like to
localize the package such that texts are correctly translated
into the language preferred by the user. This package is not
intended to be used to automatically translate more than a few
words.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/translator
%doc %{_texmfdistdir}/doc/latex/translator

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
