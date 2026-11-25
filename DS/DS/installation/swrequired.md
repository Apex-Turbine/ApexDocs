# Software Requirements

APEX supports running software on all listed operating systems. It is
recommended that users select an operating system that is used extensively in
our QA process. These are listed in the tables below.

Keep in mind that many DS supported acquisition devices need the installation
of third party driver packages. In some cases the OS requirements of these
may restrict the range of usable releases.

## Windows Support Matrix

The following Windows releases were tested for compatibility with recent APEX DS
releases. The DS software will run on the versions listed below but was not
necessarily QA tested under all of them.

| Windows Version | Bits | QA Tested | Remarks |
| --- | --- | --- | --- |
| Windows 11 | 64 | No | Untested, but **should** work |
| Windows 11 | 32 | No | Untested, but **should** work |
| Windows 10 | 64 | Yes | Development platform |
| Windows 10 | 32 | No | API Development platform |
| Windows 8.x | 64 | No | End of MS support: January 9, 2018 (8.1) |
| Windows 8.x | 32 | No | End of MS support: January 9, 2018 (8.1) |
| Windows 7 | 64 | Yes | End of MS support: January 20, 2020 |
| Windows 7 | 32 | Yes | End of MS support: January 20, 2020 |
| Windows Vista | 64 | No | End of MS support: April 11, 2017 |
| Windows Vista | 32 | No | End of MS support: April 11, 2017 |
| Windows XP | 64 | No | API only, no DS GUI, EOL: April 8, 2014 |
| Windows XP | 32 | No | API only, no DS GUI, EOL: April 8, 2014 |

## Windows Libraries

All APEX DS suite applications are built to use Microsoft's "win32" API (as
opposed to the "universal application" API introduced with Windows 8). No
additional software packages or libraries are required on any version of Windows
starting with Vista. That OS version introduced some significant additions to
the "win32" API (gdiplus, etc..), these are **required** to run any GUI
application of the DS suite.

Windows versions earlier than Vista may still be found in some hard to upgrade
embedded applications. Users of such systems may still be able to run on such
systems their own applications built against the APEX DS API libraries. However,
this practice is neither encouraged nor supported by APEX, Inc.

## Linux Support Matrix

The following Linux distributions were tested for compatibility with recent APEX
DS releases. For 32 bit platforms only API compatibility was tested. The DS
software will run on the versions listed below but was not necessarily QA tested
under all of them. One representative member of each distribution family is
included below, users of other distros  can verify compatibility by comparing
related releases (Fedora versus RHEL, Debian versus Ubuntu, etc..).

| Linux Distribution | Bits | QA Tested | Remarks |
| --- | --- | --- | --- |
| Slackware 15.0 | 64 | Yes | Development platform |
| Slackware 15.0 | 32 | No |  |
| Slackware >13.0 | 64 | No |  |
| Slackware >13.0 | 32 | No |  |
| RHEL/Centos >6.10 | 64 | Yes | EOL Nov 2020. Release build platform |
| RHEL/Centos >6.10 | 32 | API | EOL Nov 2020. API release build platform |
| Ubuntu LTS >14.04 | 64 | No | 14.04.04 EOL: Apr 2019 |
| Ubuntu LTS >14.04 | 32 | No | 14.04.04 EOL: Apr 2019 |

> [!NOTE]
> Some DS device driver packages include sources for kernel modules that
> need to be built and installed under the user's Linux distribution.
> Currently kernel versions up to 5.15.x (this is an LTS kernel) are
> supported. Generally, APEX only tests compatibility with LTS kernel
> releases, but not ones between these.

> [!WARNING]
> In case a Linux distribution is used that automatically updates its
> kernel, the APEX installed device driver modules **will** become unusable.
> In such cases the modules will have to be recompiled (**make**) and
> reinstalled (**make install**) from source (typically under
> /opt/apex/ds/modules) after each kernel upgrade.

## Linux Libraries

To ensure maximum compatibility DS releases are built on a Red Hat Enterprise
Linux 6 (RHEL6) compatible system. Therefore the minimum supported operating
system component versions are the same as used by the RHEL6 distribution. Below
is a list of these required operating system components and their minimum
versions:

|  |  |  |
| --- | --- | --- |
|  | kernel | Linux 2.6.32 |
|  | gcc | 4.4.7 |
|  | X11 | X.org 7.1.1 |
|  | glibc | 2.5 |
|  | fontconfig | 2.4.1 |
|  | freetype | 2.2.1 |
|  | libcairo | 1.2.4 |
|  | libjpeg | 1.2.1 |
|  | libpng | 2.1.2 |
|  | libXrender | 0.9.1 |
|  | libXinerama | 1.0.1 |
|  | libXft | 2.1.10 |
|  | libXpm | 3.5.5 |
|  | libstdc++ | 4.1.2 |
|  | zlib | 1.2.3 |
