Name     : jdk-scalariform
Version  : 0.1.7
Release  : 2
URL      : http://repo1.maven.org/maven2/org/scalariform/scalariform_2.11/0.1.7/scalariform_2.11-0.1.7.jar
Source0  : http://repo1.maven.org/maven2/org/scalariform/scalariform_2.11/0.1.7/scalariform_2.11-0.1.7.jar
Source1  : http://repo1.maven.org/maven2/org/scalariform/scalariform_2.11/0.1.7/scalariform_2.11-0.1.7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: jdk-scalariform-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-scalariform package.
Group: Data

%description data
data components for the jdk-scalariform package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/scalariform.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/scalariform.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/scalariform.xml \
%{buildroot}/usr/share/maven-poms/scalariform.pom \
%{buildroot}/usr/share/java/scalariform.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/scalariform.jar
/usr/share/maven-metadata/scalariform.xml
/usr/share/maven-poms/scalariform.pom
