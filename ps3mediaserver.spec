# RPM4 "junk" should be kept in this spec for 2010.2 backports sake,
# please do not remove it

Name:		ps3mediaserver
Version:	1.52.1
Release:	1
Summary:	DLNA compliant Upnp Media Server for the PS3
Source0:	http://ps3mediaserver.googlecode.com/files/pms-generic-linux-unix-%{version}.tgz
Source1:	%{name}.png
License:	propriteary
Group:		Video
URL:		http://code.google.com/p/ps3mediaserver/
BuildArch:	noarch
BuildRequires:	imagemagick
Requires:	jre
Requires:	mencoder
Requires:	ffmpeg
Requires:	mplayer

%description
PS3 Media Server is a DLNA compliant UPnP Media Server for the PS3,
written in Java, with the purpose of streaming or transcoding any kind
of media files, with minimum configuration. It's backed up with the
powerful Mplayer/FFmpeg packages.

%prep
%setup -q -n pms-%{version}

%build
echo "Hi, i'm a fake build"

%install
%__rm -rf %{buildroot}
%__install -dm 755 %{buildroot}%{_datadir}/%{name}
%__cp -af * %{buildroot}%{_datadir}/%{name}

%__mkdir -p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec ./PMS.sh
EOF
%__chmod +x %{buildroot}%{_bindir}/%{name}

#icons
%__mkdir_p %{buildroot}{%{_iconsdir},%{_liconsdir},%{_miconsdir}}
%__install -m 0644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
%__install -m 0644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
convert %{buildroot}%{_miconsdir}/%{name}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
%__install -m 0644 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png
convert %{buildroot}%{_iconsdir}/%{name}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png

# menu-entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=PS3 Media Server
Comment=Media Server for the PS3
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;X-MandrivaLinux-Multimedia-Video;
EOF

%files
%doc CHANGELOG
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
