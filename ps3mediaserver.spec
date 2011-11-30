Summary:	DLNA compliant Upnp Media Server for the PS3
Name:		ps3mediaserver
Version:	1.50.0
Release:	1
Source0:	http://ps3mediaserver.googlecode.com/files/pms-generic-linux-unix-%{version}.tgz
Source1:	%{name}.png
License:	propriteary
Group:		Video
URL:		http://code.google.com/p/ps3mediaserver/
BuildArch:	noarch
Requires:	jre
Requires:	mencoder
Requires:	ffmpeg
BuildRequires:	imagemagick
Requires:	mplayer
Obsoletes:	%{name} < %{version}



%description
PS3 Media Server is a DLNA compliant Upnp Media Server for the PS3, written in Java, 
with the purpose of streaming or transcoding any kind of media files, with minimum 
configuration. It's backed up with the powerful Mplayer/FFmpeg packages. 

%prep
%setup -q -n pms-linux-%{version}

%build
echo "Hi, i'm a fake build"

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -af * %{buildroot}%{_datadir}/%{name}

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec ./PMS.sh
EOF
chmod +x %{buildroot}%{_bindir}/%{name}


#icons
mkdir -p %buildroot{%_iconsdir,%_liconsdir,%_miconsdir}
install -m 0644 %{SOURCE1} %{buildroot}%_liconsdir/%{name}.png
install -m 0644 %{SOURCE1} %{buildroot}%_miconsdir/%{name}.png
convert %{buildroot}%_miconsdir/%{name}.png -resize 16x16 %{buildroot}%_miconsdir/%{name}.png 
install -m 0644 %{SOURCE1} %{buildroot}%_iconsdir/%{name}.png
convert %{buildroot}%_iconsdir/%{name}.png -resize 32x32 %{buildroot}%_iconsdir/%{name}.png 

# menu-entry
mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/%{name}.desktop <<EOF
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

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc README CHANGELOG 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
