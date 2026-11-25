# Software Installation

Once the hardware and software requirements described in the previous
sections are met it is time to install the necessary DS and plugin
packages. These can be downloaded from the APEX support site,
[https://www.apexturbine.com/users](https://www.apexturbine.com/users). The following packages are available:

| Item | Details |
| --- | --- |
| **apexds-{version}-{arch}-*.{ext}** | The APEX data system (DS) package. |
| **apexdv-{version}-{arch}-*.{ext}** | The free data viewer (APEX DV) package. |
| **apexdr-{version}-{arch}-*.{ext}** | The client user interface (APEX DR) package. |
| **drv-{device}-{version}-{arch}-*.{ext}** | Device specific driver plugin packages. |
| **dsapi-{version}-*.zip** | DS API package. (For all architectures.) |

The version ({version}) part of the package names identifies the DS software
version. APEX version strings are of the form: **YYYY.WW[.PATCH][BUILD]**.
Meaning of the version string fields is as follows:

> - **YYYY**: Four digit year of the release date.
> - **WW**: Week of the year when the release was built.
> - **PATCH**: Additional decimal point and digits following the week number.
>   If present, this indicates a maintenance release based on the  initial major
>   release indicated by the year and week fields. This field is optional.
> - **BUILD**: Indicates the "quality" of the software at the time the
>   package was built. This field is optional and **is always absent** for
>   official release builds. Otherwise it is a string whose first character
>   indicates some "non release" build quality: "a" for alpha, "b" for beta,
>   "r" for release candidate.

The architecture ({arch}) part of the package name determines the supported
operating system and processor model. Options are:

| Item | Details |
| --- | --- |
| **win32** | 32 bit Windows package. (Requires at least Pentium III or compatible CPU) |
| **win64** | 64 bit Windows package. |
| **i686** | 32 bit Linux package. (Requires at least Pentium III or compatible CPU) |
| **x86_64** | 64 bit Linux package. |

The extension of the package determines the installation method:

| Item | Details |
| --- | --- |
| **.tgz** or **.txz** | Linux packages built using the Slackware distribution's packaging method. |
| **.exe** | Self-installing Windows executable. Requires administrator privileges. |
| **.zip** | Windows package that has to be installed manually. |

## Installation under Windows

Download the main DS or DV package (.exe or .zip file). Also download any driver
packages (.zip files) you may need for your hardware. Starting with version 2.12
we provide two alternate installation methods for the "main" packages (DS, DR
and DV). Generally, the ".exe" installers should be used as these set up the
proper "Start Menu" items, system files, etc.. However, in corporate
environments users may not have the necessary administrator permissions to run a
proper installer. For such users we also provide a ZIP archive that contains all
the files needed to run the product.

Plugin driver packages come only in the ZIP format. The contents of these ZIP
archives should be extracted into the DS installation folder. That is, the files
and folders provided the the driver plugin package should "integrate" into the
existing folder structure created by the installation of the "main" package.

Some plugin driver packages require the installation (and possibly download) of
third party software. Consult the README file of these plugin packages for
further details.

> [!NOTE]
> - If DS was installed using the ".exe" installer then -- unless overridden
>   during installation -- the installation folder will be located under:
>
>   ```
>   C:\Program Files\APEX
>   ```
> - If a 32 bit package was installed on a 64 bit system then this will change
>   to:
>
>   ```
>   C:\Program Files (x86)\APEX
>   ```
> - If a ".zip" file was used then the installation folder is the location
>   where the contents of the archive was extracted.
> - If DS was installed using the ".exe" installer then adding plugin packages
>   will also require administrator privileges.

## Installation under Linux

Download the main DS, DR or DV package (.tgz file). Also download any driver
package(s) you may need for your hardware. Packages are installed by extracting
them with the 'tar' utility into the root (/) directory. Perform this as the
super user (root). If the package contains an installer script, it will be
located under /install/doinst.sh. This should be executed with the current
directory being root (/). Afterward the entire /install directory can be
deleted.

Packages of the APEX DS suite always install into directories under the
'/opt/apex' path. Also, some desktop environment (KDE, Gnome, XFCE, etc..)
integration symbolic links are placed under '/us/share' during the installation.

Use the commands below on a non Slackware based system. All examples assume
package is in the current directory and commands are executed from a shell as
the root user.:

```
tar -xvf apexds-2020.15-x86_64-1.tgz -C /
[ -x /install/doinst.sh ] && bash -c "cd /; source install/doinst.sh"
rm -rf /install
```

Below are the steps to install the same package on a Slackware based system.:

```
installpkg apexds-2020.15-x86_64-1.tgz
```

The next example will reinstall or upgrade the same package on a Slackware based
system. This will also remove any files or links that were present in the old
package but are no longer part of the new one.:

```
upgradepkg apexds-2020.15-x86_64-1.tgz
```

Steps are identical for other packages or releases, just replace the package
name in the above examples. The installation of plugin driver packages may
require additional steps beyond adding the contents of the package to the
target's file system. Some of these packages contain kernel module sources that
need to be compiled for the running kernel. Generally, the installer script will
attempt to build these modules, but this may fail on badly configured systems,
requiring user interaction. Some other plugins may require the installation (and
possibly download) of third-party vendor software. Consult the README file of
the APEX plugin packages for further details.

> [!NOTE]
> - The packages are built using the Slackware Linux distribution's package
>   format. Reason for this is that this format is the easiest to install into
>   other Linux distributions.
> - Under Slackware based Linux systems there are native package management
>   utilities that handle this package format: **installpkg**, **removepkg**,
>   **upgradepkg**, etc.. Check their man pages for usage details.
> - For non Slackware systems the example commands shown above are an option
>   -- possibly even as the base for a user's own "installer" script. An
>   additional alternative is downloading and installing the Slackware package
>   management tools. It is the "pkgtools" package found in the "a" package
>   series. For a list of download mirrors visit the main Slackware site:
>   [http://www.slackware.com](http://www.slackware.com). The Slackware installer system is implemented in
>   the form of shell scripts only, and these will work fine on other Linux
>   systems. Using these scripts will allow not only the installation of the
>   APEX packages but also their proper removal or upgrade.
