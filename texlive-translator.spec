%global tl_name translator
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12d
Release:	%{tl_revision}.1
Summary:	Easy translation of strings in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/translator
License:	lppl gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translator.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translator.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides a flexible mechanism for translating
individual words into different languages. For example, it can be used
to translate a word like "figure" into, say, the German word
"Abbildung". Such a translation mechanism is useful when the author of
some package would like to localize the package such that texts are
correctly translated into the language preferred by the user. This
package is not intended to be used to automatically translate more than
a few words.

