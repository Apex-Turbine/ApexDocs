# FLEX Licensing

> [!WARNING]
> **Legacy FLEXlm / FlexNet Discontinuation — October 2027**
> Legacy licensing using **FLEXlm / FlexNet** (`lmgrd`, `lmtools`, `lmutil`, `.lic` files, and `27000@host` servers) will be **discontinued as of October 2027**. All product versions going forward will exclusively use **[APEX License Manager](../License%20Manager/README.md)** (`ApexLM`), powered by the **APEX LM Daemon (`ApexLM_Service`)** and **APEX LM Server Daemon (`ApexLM_Server_Service`)**. Plan migrations using the [APEX License Manager Quick Start](../License%20Manager/quick-start.md), [Workstation & Server Setup](../License%20Manager/setup-and-server.md), and [Software Release Policies](../Release%20Policies/README.md).

The full FLEXnet Licensing - End User Guide is installed when the APEX supplied LMUtils software is installed. The FLEXnet Licensing - End User Guide can be viewed by clicking Start->All Programs->APEX->LMUtils->PDF Documentation on Windows or opening opt/apex/doc/LicensingEndUserGuide.pdf on Linux.

The manual contains detailed information on configuring, starting and running a license server. The manual also contains instructions for using the license utilities included in LMUtils.

The following is an overview of the commonly used utilities included in LMUtils: These utilities are available for both Windows and Linux systems, except where noted otherwise. Chapter 4 of the End Users Guide contains detailed instructions for each of the utilities.

- lmborrow -- Supports license borrowing.
- lmdiag -- Diagnoses license checkout problems.
- lmdown -- Shuts down license server.
- lmgrd -- Used to start license server.
- lmhostid -- Reports the hostid of a system.
- lminstall -- Converts license files between different formats.
- lmpath -- Allows users direct control over license file path settings.
- lmremove -- Releases a hung license to the pool of free licenses.
- lmreread -- Causes the license daemon to reread the license file and start any new vendor daemons.
- lmstat -- Display the status of the license server system.
- lmswitch(Linux only) -- Control debug log location and size.
- lmswitchr -- Switches the report log to a new file name.
- lmtools (Windows only) -- Graphical program for managing all aspects of license server system, including creating a Windows Service to run the license server system automatically at startup.
- lmutil -- Package of all FLEXnet Licensing Utilities.
- lmver -- Reports the FLEXnet Licensing version of a library or binary file.

> [!NOTE]
> APEX products use FLEXnet version 11.4. Those using an earlier version of FLEXnet may be required to update their 'lmgrd' utility in order to run the APEX vendor daemon. The 'lmgrd' installed with APEX applications, located in the applications 'licenses' directory, will run the APEX vendor daemon and all vendor daemons who's version is 11.4 or lower.
