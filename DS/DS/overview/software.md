# Software

The APEX DS software suite is available for 64 bit x86 family Intel or
compatible processors running the Windows or Linux operating systems. Support
for 32 bit is limited. Under Linux only the Application Program Interface (API)
package supports building 32 bit binaries. At the time of the current release 32
bit packages are still available for Windows, but they are deprecated.

The software is distributed in the form of *install packages*, the use of these
will be covered in the next Chapter. Once installed, the various APEX DS suite
packages provide the following software components:

## APEX DS

The APEX DS (Data System) application is used to acquire, process and store
dynamic data. It also performs real-time analysis of the acquired data via its
powerful graphical user interface. This interface provides various data displays
representing different views (time domain, spectrum, summary, order domain,
etc..) of the input. Additionally, APEX DS contains an interactive configuration
editor that is used to set up the necessary data acquisition and processing
parameters.

## APEX DV

The APEX DV (Data Viewer) application is used to replay data recorded using DS.
It supports the same visualization environment as the original recording
application.

## APEX DR

The APEX DR (Data Remote) application is used to add additional real-time
monitoring interfaces to a running APEX DS acquisition system over a network
connection. It supports the same visualization environment as the main DS
acquisition application. In addition (unlike the DS systems providing the data),
DR allows connecting to multiple running DS configurations and selectively
monitoring data from all of them.

## Device Driver Plugins

The APEX DS installer packages do not contain support for any
acquisition device. These are supported by hardware-specific plugin
modules, each of which is contained in a separate install package.

The device driver packages typically contain two components:

> - A plugin module (DLL or shared library module) that is loaded by APEX
>   DS upon start-up.
> - A kernel mode device driver that is loaded by the operating system at boot
>   time. For some devices this is provided by the manufacturer of the device,
>   for others it is supplied by APEX.

> [!NOTE]
> Due to the availability of hardware information or vendor provided drivers,
> some devices are supported only under a subset of the platforms
> (Windows/Linux, 32/64 bit) for which APEX DS is available.*

## Data Processing Plugins

The data processor used by APEX DS is highly customizable. It is possible to
insert optional "plugin" steps at various places of the "standard" processing
sequence. Some of the available plugins are built into APEX DS, but it is also
possible for users to create custom ones using the API package described below.

## Application Program Interface

Several Application Program Interfaces (APIs) are provided to help custom user
code interact with APEX DS. These APIs are available as shared
libraries (DLLs) with C or C++ callable entry points declared in C header
files. The API libraries are available for the Linux and Windows operating
systems running on the Intel architecture. Both 32 and 64 bit versions are
provided.

Consult the manuals available in the DS API package for further
details.
