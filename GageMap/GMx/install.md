# Install APEX GageMap

## Linux Installation

Download the main GageMap (.tgz file).
Packages are installed by extracting them with the 'tar' utility into
the root (/) directory. If the package contains an installer script,
it will be located under /install/doinst.sh. It should be executed
with the current directory being root (/).

NOTE: The packages are built using the Slackware Linux
distribution's package format. The reason for this is that this format
is the easiest to install into other Linux distributions. Under
native Slackware systems there are package management utilities:
installpkg, removepkg, upgradepkg, etc.. Check their man pages for
usage details. For non Slackware systems we recommend downloading
and installing the Slackware package management tools. (It is the
"pkgtools" package found in the "a" package series. Check the main
Slackware site, www.slackware.com, for download mirrors.) The
Slackware installer system is implemented in the form of shell
scripts only, and it will work fine on other Linux systems. Using
it will allow not just the installation of the APEX packages but
also their proper removal or upgrade.

## Windows Installation

Download the main GageMap package (.exe or .zip file).
Generally, the ".exe" installers should be used as these set up the
proper Start Menu items, system files, etc.. However, in corporate
environments users may not have the necessary administrator
permissions to run a proper installer. For such users we also
provide a ZIP archive that contains all the files needed to run the
product.

## Other Installations

Other packages may be available independent of the main GageMap
package. These may include:

- ansys2sdr     Ansys converter
- aba2sdr       Abaqus converter

The same procedures described above should be used for installation on
the desired operating system.
