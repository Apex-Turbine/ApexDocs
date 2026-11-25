# Software Maintenance & Technical Support Policy

This policy establishes eligibility, renewal procedures, support access channels, defect severity classifications, and response/resolution commitments for **APEX Testing Technologies, Inc.** (**APEX**) Maintenance Agreement customers.

---

## 1. Software Maintenance Coverage & Lifecycle Terms

1. **Initial Coverage Period (`New Purchases`)**:
   - Unless expressly excluded in the purchase agreement, Software Maintenance is provided for **one (1) year** from the date **Software License Keys** were originally issued in fulfillment of a purchase order or transaction.
2. **Maintenance Renewal & Grace Window**:
   - **Renewal Quotation**: APEX automatically issues a Software Maintenance renewal quote within **90 days** prior to expiration of an active maintenance period.
   - **On-Time Renewal (`<= 30 Days`)**: Customers choosing to renew must complete renewal no later than **30 days after expiration** of the current maintenance period to avoid lapse penalties.
   - **Continuous Term**: Renewed coverage starts on the day immediately following expiration of the prior term and extends for a **one-year minimum** period.
3. **Reinstating Lapsed Maintenance (`Back-Maintenance`)**:
   - Customers wishing to reinstate expired Software Maintenance must purchase **back-maintenance** covering every lapsed month plus **at least one (1) additional forward year** at APEX's then-current standard maintenance rates and calculation methodology. Advance quotes are provided upon request.
4. **Alignment with the 18-Month Release Maintenance Policy**:
   - As governed by the **[Software Release Policy](README.md#2-18-month-release-lifecycle-update-requirement)**, **every APEX software version is maintained for no more than 18 months** from its release date.
   - Active Maintenance customers are entitled to download all minor/major updates and receive updated `ApexLM` Format Version 2 license files (`YYYY.MM` ceiling bumps) to stay within the mandatory **18-month update cycle**. Backported fixes for versions older than 18 months are not available.
5. **Maintenance Status Records**:
   - Customers can view maintenance coverage dates, registered products, and active licenses online through the **[APEX User Portal](https://users.apexturbine.com/)**.

---

## 2. Maintenance Customer Benefits

During an active **Software Maintenance Agreement**, customers receive:

- **Official Software Updates & Upgrades**: Access via **[https://apexturbine.com/](https://apexturbine.com/)** and **[https://users.apexturbine.com/](https://users.apexturbine.com/)** to feature enhancements, defect fixes, OS/driver compatibility updates, and new major versions of licensed APEX products.
- **Updated Format v2 License Keys (`ApexLM`)**: New signed JSON keys when software upgrades exceed the previous version ceiling, when hardware/channel entitlements change, or during migration from legacy FlexNet (`lmgrd`) ahead of its **October 2027** discontinuation.
- **Node-Locked License Transfers (Re-Hosting)**: Under active Maintenance, node-locked `LOCAL` or `SERVER` licenses can be transferred to replacement hardware upon formal request *(accompanied by `license-request.json` from the new host)*. Without an active Maintenance Agreement, APEX may issue replacement keys at its sole discretion for an administrative fee.
- **Priority Engineering Support & Ticket Resolution**: Full access to Web Portal ticketing, FAQ knowledge base, and direct telephone engineering support per Section 3 & Section 4 below.

---

## 3. Technical Support Channels & Availability

| Support Channel | Access Details | Operating Hours & Routing |
| :--- | :--- | :--- |
| **APEX User Portal (Tickets & Downloads)** | **[https://users.apexturbine.com/](https://users.apexturbine.com/)** | **24/7 online submission** for non-emergency defect **Tickets**, feature requests, maintenance status checks, FAQ lookup, and official software downloads. Ticket submissions automatically notify and assign the appropriate engineering team. |
| **Direct Engineering Telephone Support** | **+1 (931) 486-0082** | **Monday – Friday, 08:00 – 17:00 US Central Time**. Connects directly with APEX engineering support personnel for interactive troubleshooting and emergency triage. |
| **After-Hours & Critical Test-Cell Escalation** | **+1 (931) 486-0082** | Outside business hours:<br>• **CRITICAL issues** *(test-cell acquisition down)* are routed by the **APEX Help Call-Center** directly to on-call APEX personnel.<br>• **Non-critical voicemails** are returned by APEX personnel within **24 hours**. |

### Preparing Diagnostic Packages Before Contacting Support

To accelerate root-cause analysis when submitting a ticket or calling support:
1. Confirm your software version is within the **18-month maintenance window** and verify your workstation passes **`AVX2`** and **RAM** requirements ([System Requirements](system-requirements.md)).
2. Attach relevant diagnostic artifacts:
   - **DX+ Applications**: Generated `CrashReporter.exe` forensic `.rpt` bundle and minidump.
   - **APEX License Manager (`ApexLM`)**: Downloaded `apexlm-log.txt` and `apexlm.crash.dmp` (from the **Log** tab or `ApexLM_CLI crash-dump`) plus `ApexLM_CLI status` output.
   - **Exact Reproduction Steps**: Product name/version, setup files (`.dspro`, `.dxt`, `.dpd`, `.gmp`), and screenshot/error text.

---

## 4. Software Error Classifications & Resolution Schedule

Reported defects in supported software versions (within 18 months of release) are classified into three severity tiers:

### `CRITICAL` *(Real-Time Acquisition & Monitoring Software Only)*
- **Scope**: Applies strictly to real-time test-cell acquisition and monitoring applications (for example `APEX DS`, `APEX DR`, `DX+ DAQ`, `DX+ Online Analysis`). Does **not** apply to pre-test (`GageMap`, `SdrConverter`, `SDRFM`) or post-test (`APEX DX`, `DX+ Offline Analysis`, `DX+ Data Viewer`, `DX+ DB Manager`) applications.
- **Definition**: Errors preventing test work from continuing — including:
  - System aborts preventing data acquisition,
  - Uncommanded overwrite or loss of already-recorded test data, or
  - Failure of real-time monitoring, recording control, or signal-health limit functionality.
- **Customer Action**: Call **+1 (931) 486-0082** immediately and identify the issue as **CRITICAL**.
- **APEX Response & Resolution Procedure**:
  1. Immediate interactive triage with APEX engineers to rule out hardware faults (failed disk drives, digitizers, cables — hardware repairs use customer spares).
  2. Work interactively to identify an immediate operational workaround avoiding the defect.
  3. Apply reasonable commercial effort to supply an urgent software relief build as rapidly as possible if no workaround exists (customer may be asked to run an interim diagnostic/relief build).
  4. Issue a formal verified **maintenance release** correcting the defect within **1 week (7 calendar days)**.

### `SEVERE`
- **Definition**: Errors causing the operating system to lock up or abort, repeatable application crashes, or major functional impairments that prevent using the software for its intended as-designed purpose without a viable workaround.
- **APEX Response & Resolution Schedule**:
  - Diagnosed and corrected within **48 hours** of defect confirmation *(an interim non-release build may be provided for immediate operational relief and joint validation)*.
  - Incorporated into a formal **maintenance release** within **2 weeks (14 calendar days)**.

### `IMPORTANT`
- **Definition**: Functional defects or operator nuisances for which a practical operational workaround exists, allowing continued use of the software as designed.
- **APEX Response & Resolution Schedule**: Diagnosed, corrected, and delivered in the **next scheduled software release**.

---

## 5. Exclusions from Maintenance Obligations

APEX has no obligation to provide Maintenance benefits, updates, or defect corrections if a defect results from:
1. Using APEX software outside published specifications, system requirements (including non-`AVX2` hardware or unsupported OS versions), or operating software beyond the **18-month version maintenance window** without APEX's written authorization;
2. Customer altering, modifying, reverse engineering, decompiling, or converting APEX software, libraries, or license files inconsistent with official documentation without written permission from APEX;
3. Malfunction of customer computer hardware, storage media, network infrastructure, third-party acquisition chassis/drivers, or customer OS misconfiguration; or
4. Any other cause within Customer's control and outside APEX's control.

See also: [Software Release Policies & 18-Month Lifecycle](README.md) · [Software License Agreement (SLA)](software-license-agreement.md)
