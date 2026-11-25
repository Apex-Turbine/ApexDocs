# Install APEX DX

## Linux Installation

### Installer (.run)

Download the Apex DX Installer (.run file).
Packages are installed by running the .run file. Make sure the .run package
has execute permissions by running chmod +x DXInstaller.run. You
can then run the installer and follow the instructions. The installer needs
sudo permissions to install in the default directory of /opt/Apex.
The installer will prompt you to enter your password if necessary.

The Linux Installer uses the Qt Installer Framework. The requirements
for running this are listed in the Qt5 documentation
[http://doc.qt.io/qt-5/linux-requirements.html](http://doc.qt.io/qt-5/linux-requirements.html)

### Tar gzip (.tgz)

Download the gzipped Apex DX (.tgz file).
Packages are installed by extracting them with the 'tar' utility into
the root (/) directory. If the package contains an installer script,
it will be located under /install/doinst.sh. It should be executed
with the current directory being root (/).

IMPORTANT:
Please be sure to copy all files from the gzipped package. DX
relies on all of the provided files, from documentation to plugins and filters.

NOTE:
DX requires licensing to run, see the licensing section in the documentation.

NOTE:
The packages are built using the Slackware Linux
distribution's package format. Reason for this is that this format
is the easiest to install into other Linux distributions. Under
native Slackware systems there are package management utilities:
installpkg, removepkg, upgradepkg, etc.. Check their man pages for
usage details. For non Slackware systems we recommend downloading
and installing the Slackware package management tools. (It is the
"pkgtools" package found in the "a" package series. Check the main
Slackware site, www.slackware.com, for download mirrors.) The
Slackware installer system is implemented in the form of shell
scripts only, and it will work fine on other Linux systems. Using
it will allow not just the installation of the Apex packages but
also their proper removal or upgrade.

## Windows Installation

Download the main Apex DX package (.exe or .zip file).
Generally, the ".exe" installers should be used as these set up the
proper Start Menu items, system files, etc.. However, in corporate
environments users may not have the necessary administrator
permissions to run a proper installer. For such users we also
provide a ZIP archive that contains all the files needed to run the
product.
