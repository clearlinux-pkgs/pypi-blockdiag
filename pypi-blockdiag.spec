#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-blockdiag
Version  : 3.0.0
Release  : 49
URL      : https://files.pythonhosted.org/packages/b4/eb/e2a4b6d5bf7f7121104ac7a1fc80b5dfa86ba286adbd1f25bf32a090a5eb/blockdiag-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/eb/e2a4b6d5bf7f7121104ac7a1fc80b5dfa86ba286adbd1f25bf32a090a5eb/blockdiag-3.0.0.tar.gz
Summary  : blockdiag generates block-diagram image from text
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pypi-blockdiag-bin = %{version}-%{release}
Requires: pypi-blockdiag-license = %{version}-%{release}
Requires: pypi-blockdiag-python = %{version}-%{release}
Requires: pypi-blockdiag-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(funcparserlib)
BuildRequires : pypi(mock)
BuildRequires : pypi(nose)
BuildRequires : pypi(pep8)
BuildRequires : pypi(pillow)
BuildRequires : pypi(py)
BuildRequires : pypi(reportlab)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(webcolors)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
`blockdiag` generate block-diagram image file from spec-text file.
.. image:: https://github.com/blockdiag/blockdiag/actions/workflows/main.yml/badge.svg
:target: https://github.com/blockdiag/blockdiag/actions/workflows/main.yml
:alt: GitHub Action CI build status

%package bin
Summary: bin components for the pypi-blockdiag package.
Group: Binaries
Requires: pypi-blockdiag-license = %{version}-%{release}

%description bin
bin components for the pypi-blockdiag package.


%package license
Summary: license components for the pypi-blockdiag package.
Group: Default

%description license
license components for the pypi-blockdiag package.


%package python
Summary: python components for the pypi-blockdiag package.
Group: Default
Requires: pypi-blockdiag-python3 = %{version}-%{release}

%description python
python components for the pypi-blockdiag package.


%package python3
Summary: python3 components for the pypi-blockdiag package.
Group: Default
Requires: python3-core
Provides: pypi(blockdiag)
Requires: pypi(funcparserlib)
Requires: pypi(pillow)
Requires: pypi(setuptools)
Requires: pypi(webcolors)

%description python3
python3 components for the pypi-blockdiag package.


%prep
%setup -q -n blockdiag-3.0.0
cd %{_builddir}/blockdiag-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641861557
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-blockdiag
cp %{_builddir}/blockdiag-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-blockdiag/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/blockdiag-3.0.0/src/blockdiag/tests/VLGothic/LICENSE %{buildroot}/usr/share/package-licenses/pypi-blockdiag/af07a3a5218239724d3c4ad4f9e4746835129293
cp %{_builddir}/blockdiag-3.0.0/src/blockdiag/tests/VLGothic/LICENSE.en %{buildroot}/usr/share/package-licenses/pypi-blockdiag/25d28628ff8ea8da700469e7b9ce06e5faecfed0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/blockdiag

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-blockdiag/25d28628ff8ea8da700469e7b9ce06e5faecfed0
/usr/share/package-licenses/pypi-blockdiag/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-blockdiag/af07a3a5218239724d3c4ad4f9e4746835129293

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
