# Software License Agreement (SLA)

This **Software License Agreement ("Agreement" / "SLA")** governs end-user and developer use of all software, developer APIs/SDKs, proprietary file formats, and documentation provided by **APEX Testing Technologies, Inc.**

> [!IMPORTANT]
> **Notice Regarding APEX APIs, SDKs, and Proprietary Data Formats**
>
> All **APEX**-provided application programming interfaces (`DS-API`, `Phoenix API`, `GmScript`, device/DSP plugin SDKs), proprietary data formats (`.rwx`, `.rwz`, `.pkx`, `.dxdb`, `.sdr`, `.gmp`, `.h5`, `.datx` extensions, `.dspro`, `.dxt`, `.dpd`), database schemas, and wire protocols are licensed **strictly for internal end-user use** by licensed Customers. **They MUST NOT be used for commercial means** — including third-party software products, OEM integrations, SaaS platforms, commercial file translators, or paid third-party service bureaus — **unless explicitly authorized in advance by APEX Testing Technologies, Inc. through a separate, duly executed formal written agreement.**

---

## 1. Definitions

- **1.1. `APEX`**: **APEX Testing Technologies, Inc.**, a corporation incorporated under the laws of the State of Tennessee, United States of America.
- **1.2. `CUSTOMER`**: The person, government entity, or organization purchasing, licensing, or using APEX Software and Licensed Materials.
- **1.3. `Maintenance Agreement`**: A written agreement between APEX and CUSTOMER under which APEX provides technical support, software upgrades/updates, updated license keys, and correction of software defects under agreed terms and conditions ([Software Maintenance & Support Policy](maintenance-and-support.md)).
- **1.4. `Software and Licensed Materials`**: Any materials APEX provides to CUSTOMER, including executable applications, background services/daemons (**APEX License Manager**), device drivers, SDKs, APIs, scripts, libraries, training materials, technical specifications, and reference documentation.
- **1.5. `APEX APIs and SDKs`**: All developer-facing programming interfaces, C/C++ headers, static/shared libraries, MATLAB wrappers, Python modules (`dsapi.py`, `phoenixpy`), Lua scripting modules (`GmScript`), device/DSP plugin ABIs (`PluginDev`, `DspPlugin`, `PhoenixCore`), sample programs, and API documentation.
- **1.6. `APEX Formats and Protocols`**: All proprietary and APEX-documented file formats, database table schemas, JSON schemas, and binary/ZeroMQ/TCP wire protocols (including `.rwx`, `.rwz`, `.pkx`, `.raw`, `.pks`, `.datx`, `.dxdb`, `APEX-H5`, `.sdr`, `.gmp`/`.gms`/`.gmg`/`.gma`/`.gmo`/`.gml`/`.gmm`/`.gmf`/`.sga`/`.gbf`, `.dspro`/`.drpro`/`.srpro`, `.dxt`, `.dpd`, `GraphJson`, `TableJson`, `DXPNet`, and DS Parameter Server protocols).

---

## 2. Software License Grant, Distribution, Payment & Activation

- **2.1. License Grant**: Upon full payment and compliance with this Agreement, APEX grants CUSTOMER a **nonexclusive, non-sublicensable, nontransferable license** to install and use the Software and Licensed Materials on compliant computational hardware solely for CUSTOMER's **internal business use**, together with permitted Enhancements provided under an active Maintenance Agreement.
- **2.2. Official Distribution Channels**: APEX delivers Software and Licensed Materials exclusively through official APEX websites (**`https://apexturbine.com/`**, **`https://users.apexturbine.com/`**) or authorized physical distribution media. CUSTOMER is responsible for ensuring target machines meet published **64-bit `x86-64` + `AVX2`**, RAM, OS, and GPU requirements ([System Requirements](system-requirements.md)).
- **2.3. Payment Terms**: Unless otherwise agreed in writing, payment is **NET 30** in **U.S. Dollars**. CUSTOMER is solely responsible for applicable duties, value-added or sales taxes, import/export fees, and currency exchange charges.
- **2.4. License Keys & Activation Mechanisms**: APEX issues software license keys matching CUSTOMER's purchase (temporary acceptance keys may be issued prior to final payment at APEX's discretion):
  - **2.4.1. Node-Locked (`LOCAL`) Licenses**: Authorize Software on a single designated host identified by physical MAC address (`host`), configured either as Perpetual or Temporary (expiring on the stated `expires` date). Re-hosting node-locked keys to replacement hardware is included under an active Maintenance Agreement and may incur an administrative fee otherwise.
  - **2.4.2. Floating Network (`SERVER` / `PASSTHROUGH`) Licenses**: Managed centrally via an APEX-configured license server (`ApexLM_Server_Service`) accessible over local network/VPN by local workstation **APEX LM Daemons** (`PASSTHROUGH` mode). Concurrent active usage is capped at licensed seat/token counts.
  - **2.4.3. Offline Reservations (`Reserve`)**: Where supported by the floating **APEX LM Server Daemon**, a workstation in `PASSTHROUGH` mode may reserve eligible features, token pools, and hardware entitlements for disconnected operation up to **30 days**. Reserved seats are deducted from the server pool until returned manually online or automatically reclaimed upon reservation expiration.
  - **2.4.4. Legacy FLEXlm Discontinuation**: Licensing methods using **FLEXlm / FlexNet Publisher (`lmgrd`, `.lic` files, OpenCode Trusted Storage)** are **discontinued as of October 2027**. All product releases going forward exclusively use **[APEX License Manager (`ApexLM`)](../License%20Manager/README.md)**.
- **2.5. 18-Month Release Lifecycle**: Every released Software version is maintained for **no more than 18 months** from initial release. CUSTOMER acknowledges that an **18-month update cycle** (upgrading to a supported release within 18 months) is required to maintain technical support, driver compatibility, and defect maintenance ([Release Policies](README.md)).
- **2.6. Internal Business Use & Affiliate Scope**: CUSTOMER may permit its Affiliates, leased employees, or on-site outsourced contractors to use the Software **solely for CUSTOMER's direct internal benefit**, provided CUSTOMER ensures such personnel comply with all terms herein and bind them to confidentiality obligations at least as protective as this Agreement.
- **2.7. Prohibited Software Uses**: CUSTOMER shall NOT:
  1. Use the Software in a service bureau, hosting, SaaS, time-sharing, or outsourced testing capacity for the benefit of third parties (other than explicitly licensed Affiliates);
  2. Rent, lease, lend, resell, distribute, or sublicense the Software or license keys;
  3. Circumvent, bypass, forge, share credentials/app identities across, or tamper with `ApexLM`, Ed25519 signatures, hardware serial checks, or version limits.

---

## 3. End-User License Terms for Developer APIs, SDKs & Plugins

- **3.1. End-User Internal Scope Only**: Access to **APEX APIs and SDKs** (including `DS-API`, `Phoenix API`, `GmScript`, custom device driver SDKs, and custom DSP/component plugin interfaces) is granted **exclusively to properly licensed end-user CUSTOMERs** solely to:
  1. Integrate APEX acquisition hardware and software into CUSTOMER's own internal test stands and internal laboratory workflows;
  2. Read, convert, or analyze CUSTOMER's own internal test telemetry; and
  3. Author custom internal device drivers, internal DSP statistics/components, or internal automation scripts for use on CUSTOMER's licensed APEX installations.
- **3.2. Strict Prohibition on Commercial Use Without Formal Written Agreement**:
  - **Any commercial use of APEX APIs, SDKs, headers, binaries, wrappers, or documentation is strictly prohibited unless explicitly authorized in advance by APEX Testing Technologies, Inc. through a separate, duly executed formal written commercial/OEM agreement.**
  - Prohibited unapproved commercial activities include, without limitation:
    - Incorporating APEX APIs, DLLs/shared libraries, or SDK code into commercial software products or commercial hardware bundles distributed or sold to third parties;
    - Offering commercial cloud, SaaS, subscription, or consulting software built upon `DS-API` or `Phoenix API`;
    - Using APEX APIs or automation scripts to operate a commercial testing or data-conversion service bureau for unaffiliated third parties; or
    - Distributing modified or standalone wrappers/bindings exposing APEX libraries without a formal written OEM/ISV license from APEX.
- **3.3. Mandatory Runtime Licensing Compliance**: Custom applications using `DS-API` network sessions or `Phoenix API` (`PhoenixLic`) must connect legitimately to an authorized **APEX License Manager** service using their assigned end-user client identity and valid CUSTOMER license seats. Any attempt to spoof internal APEX application identities or bypass feature/hardware licensing checks constitutes a material breach of this Agreement.

---

## 4. End-User License Terms for APEX Formats, Database Schemas & Wire Protocols

- **4.1. Proprietary Rights & End-User Purpose**: Technical documentation describing **APEX Formats and Protocols** (including binary container structures, database tables/columns, project JSON schemas, and ZeroMQ/TCP streaming packet layouts) is published solely to assist licensed end-user CUSTOMERs in interoperability, archiving, internal validation, and custom end-user post-processing of **their own data**.
- **4.2. Strict Prohibition on Commercial Format Exploitation**:
  - **Any use of APEX-provided file formats, database schemas, or network protocol specifications for commercial means is strictly prohibited unless explicitly authorized in advance by APEX Testing Technologies, Inc. through a formal written agreement.**
  - Specifically, CUSTOMER and any third party reviewing public or customer documentation shall **not**, without formal written authorization from APEX, develop, market, sell, license, or distribute commercial software products, commercial data converters/parsers, commercial database ingestors, or paid third-party data-translation services that read, write, emulate, or bridge APEX proprietary formats or protocols.

---

## 5. Intellectual Property & Title

- **5.1. No Reverse Engineering**: CUSTOMER shall not reverse assemble, reverse engineer, decompile, disassemble, decrypt, or unlock the Software, SDK libraries, or license mechanisms in whole or in part for any reason (including extracting cryptographic keys or internal application identifiers).
- **5.2. Retention of Source & Title**: APEX retains exclusive right, title, and ownership to all source code, algorithms, user interfaces, APIs, proprietary formats, Modifications, Enhancements, tools, and Licensed Materials. CUSTOMER owns physical removable media (if provided) and retains exclusive title to CUSTOMER's own acquired test data, analytical results, reports, and memoranda generated for CUSTOMER's internal operations.

---

## 6. Software Warranty, Indemnification & Limitation of Liability

- **6.1. Operational & Authority Warranty**: APEX warrants that it owns or holds authority to license the Software and that properly maintained Software operating on compliant hardware within its supported 18-month release window will perform substantially in accordance with APEX's current published specifications.
- **6.2. Disabling Code Warranty**: APEX warrants that it has taken reasonable steps to scan release software against Disabling Code (viruses, worms, unauthorized timers/locks outside standard license enforcement) and to the best of APEX's knowledge Software is free of Disabling Code at release.
- **6.3. Disclaimers**: Unless expressly agreed in writing elsewhere, APEX DOES NOT WARRANT THAT THE SOFTWARE WILL MEET CUSTOMER'S SPECIFIC REQUIREMENTS, OPERATE UNINTERRUPTEDLY OR IN COMBINATION WITH UNSUPPORTED THIRD-PARTY SOFTWARE, OR THAT EVERY DEFECT IS CORRECTABLE. **ALL IMPLIED WARRANTIES — INCLUDING MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE — ARE EXPRESSLY DISCLAIMED TO THE MAXIMUM EXTENT PERMITTED BY LAW.** Third-party software components bundled or referenced (including database engines, GUI toolkits, and hardware vendor SDKs) are provided under their respective third-party warranties/licenses without additional APEX warranty.
- **6.4. U.S. Intellectual Property Indemnification**: APEX will defend and indemnify CUSTOMER against claims that CUSTOMER's authorized use of unmodified APEX Software directly infringes a valid United States patent, copyright, or trade secret, provided CUSTOMER: (i) notifies APEX promptly in writing; (ii) grants APEX sole control and full cooperation in defense/settlement; and (iii) has maintained an uninterrupted Maintenance Agreement (or accepts non-infringing replacement Software provided by APEX). This states APEX's entire liability for IP infringement.
- **6.5. Limitation of Liability**: **NEITHER APEX NOR ITS RESELLERS, SUPPLIERS, OR AGENTS SHALL BE LIABLE FOR LOSS OF PROFIT, LOSS OF DATA, LOSS OF USE, BUSINESS INTERRUPTION, LOSS OF GOODWILL, OR ANY INDIRECT, CONSEQUENTIAL, SPECIAL, INCIDENTAL, OR PUNITIVE DAMAGES ARISING FROM THIS AGREEMENT OR USE OF SOFTWARE, APIS, OR FORMATS.** Except for bodily injury or tangible property damage caused by negligence or willful misconduct, APEX's aggregate cumulative liability shall not exceed the license and service plan fees actually paid by CUSTOMER for the specific Software product giving rise to the claim.

---

## 7. General Legal Provisions

- **7.1. Governing Law**: This Agreement is governed by and construed under the internal substantive laws of the **State of Tennessee, USA**, excluding conflict-of-laws rules.
- **7.2. Export Compliance (EAR & ITAR)**: Both parties agree to comply strictly with U.S. Department of Commerce Export Administration Regulations (**EAR**) and U.S. Department of State International Traffic in Arms Regulations (**ITAR**) and obtain all required governmental authorizations prior to re-exporting U.S.-origin technical data or software.
- **7.3. Assignment**: APEX may assign this Agreement to an affiliate or successor-in-interest at any time upon notice; CUSTOMER may assign only as part of a transfer of substantially all of its relevant business unit assets with written notice and compliance.
- **7.4. Entire Agreement & Written Modifications**: No waiver, exception, or commercial authorization altering any provision of this Agreement — including Section 3 (APIs/SDKs) or Section 4 (Formats/Protocols) — is valid or binding unless executed **in writing and signed by duly authorized representatives of APEX Testing Technologies, Inc. and CUSTOMER**.

---

*For commercial licensing, OEM partnerships, ISV API authorization, or formal format licensing inquiries, contact **APEX Testing Technologies, Inc.** via **[https://apexturbine.com/](https://apexturbine.com/)** or **`+1 (931) 486-0082`**.*
