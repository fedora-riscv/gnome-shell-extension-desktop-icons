%global extid   %{extname}@csoriano
%global extname desktop-icons
%global uuid    org.gnome.shell.extensions.%{extname}

%global commit  a1e9fd5af4e8e2df561d0882e7c68d11b497c93e

Name:           gnome-shell-extension-%{extname}
Version:        19.01.4
Release:        4%{?dist}
Summary:        GNOME Shell extension for providing desktop icons

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/ShellExtensions/desktop-icons
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  meson
Requires:       gnome-shell
Requires:       nautilus >= 3.30.4
Requires:       xdg-desktop-portal-gtk

%description
This package provides a GNOME Shell extension for showing the contents
of ~/Desktop on the desktop of the Shell. Common file management operations
such as launching, copy/paste, rename and deleting are supported.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-shell-extension-tool -e %{extid}

%prep
%autosetup -n %{extname}-%{version}-%{commit}
sed -e "/meson_post_install/d" -i meson.build

%build
%meson --localedir=%{_datadir}/locale
%meson_build

%install
%meson_install
%find_lang %{extname}

%files -f %{extname}.lang
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-shell/extensions/%{extid}

%changelog
* Sun Sep 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.01.4-4
- Initial package

