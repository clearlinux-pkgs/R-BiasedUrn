#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : R-BiasedUrn
Version  : 2.0.12
Release  : 51
URL      : https://cran.r-project.org/src/contrib/BiasedUrn_2.0.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BiasedUrn_2.0.12.tar.gz
Summary  : Biased Urn Model Distributions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-BiasedUrn-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
univariate and multivariate noncentral hypergeometric distributions, 
  including Wallenius' noncentral hypergeometric distribution and
  Fisher's noncentral hypergeometric distribution. 
  See vignette("UrnTheory") for explanation of these distributions.

%package lib
Summary: lib components for the R-BiasedUrn package.
Group: Libraries

%description lib
lib components for the R-BiasedUrn package.


%prep
%setup -q -n BiasedUrn
pushd ..
cp -a BiasedUrn buildavx2
popd
pushd ..
cp -a BiasedUrn buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718605967

%install
export SOURCE_DATE_EPOCH=1718605967
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BiasedUrn/DESCRIPTION
/usr/lib64/R/library/BiasedUrn/INDEX
/usr/lib64/R/library/BiasedUrn/Meta/Rd.rds
/usr/lib64/R/library/BiasedUrn/Meta/demo.rds
/usr/lib64/R/library/BiasedUrn/Meta/features.rds
/usr/lib64/R/library/BiasedUrn/Meta/hsearch.rds
/usr/lib64/R/library/BiasedUrn/Meta/links.rds
/usr/lib64/R/library/BiasedUrn/Meta/nsInfo.rds
/usr/lib64/R/library/BiasedUrn/Meta/package.rds
/usr/lib64/R/library/BiasedUrn/Meta/vignette.rds
/usr/lib64/R/library/BiasedUrn/NAMESPACE
/usr/lib64/R/library/BiasedUrn/R/BiasedUrn
/usr/lib64/R/library/BiasedUrn/R/BiasedUrn.rdb
/usr/lib64/R/library/BiasedUrn/R/BiasedUrn.rdx
/usr/lib64/R/library/BiasedUrn/demo/ApproxHypergeo.R
/usr/lib64/R/library/BiasedUrn/demo/CompareHypergeo.R
/usr/lib64/R/library/BiasedUrn/demo/OddsPrecision.R
/usr/lib64/R/library/BiasedUrn/demo/SampleWallenius.R
/usr/lib64/R/library/BiasedUrn/demo/UrnTheory.R
/usr/lib64/R/library/BiasedUrn/doc/UrnTheory.Rtex
/usr/lib64/R/library/BiasedUrn/doc/UrnTheory.pdf
/usr/lib64/R/library/BiasedUrn/doc/index.html
/usr/lib64/R/library/BiasedUrn/help/AnIndex
/usr/lib64/R/library/BiasedUrn/help/BiasedUrn.rdb
/usr/lib64/R/library/BiasedUrn/help/BiasedUrn.rdx
/usr/lib64/R/library/BiasedUrn/help/aliases.rds
/usr/lib64/R/library/BiasedUrn/help/paths.rds
/usr/lib64/R/library/BiasedUrn/html/00Index.html
/usr/lib64/R/library/BiasedUrn/html/R.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/BiasedUrn/libs/BiasedUrn.so
/V4/usr/lib64/R/library/BiasedUrn/libs/BiasedUrn.so
/usr/lib64/R/library/BiasedUrn/libs/BiasedUrn.so
