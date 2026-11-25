# PTP Configuration FAQ for MeCalc Devices

## Issue

Users attempting to configure MeCalc devices with PTP (Precision Time Protocol) have experienced poor synchronization accuracy. In some cases, the DS system cannot begin monitoring when PTP is enabled. Documentation for this setup is limited or unavailable.

## Recommended Configuration

1. Switch Configuration
  - **PTP Mode**: Configure the PTP switch to operate in **Peer-to-Peer (P2P) Transparent Clock mode**. This mode is essential for accurate timestamping and delay compensation across the network.
  - **Model Notes**: For example, the **CTC ICS-G24044X** switch behaves similarly to Cisco switches. If CTC-specific documentation is unavailable, Cisco switch configuration references may be useful.
2. Master Clock Setup
  - Use a dedicated **grandmaster clock** (e.g., Meinberg) that synchronizes to GPS.
  - The clock should distribute time via **PTP, IRIG, and/or NTP**.
  - Ensure the **PTP domain number** is unique if there are other PTP clocks or services running on the same network. This prevents interference or master contention.
3. Network Topology
  - If you are experiencing accuracy issues, consider **connecting the MeCalc PTP switch directly to the master clock**.
  - Avoid intermediate switches unless they are properly configured for PTP.
  - Avoid mixed configurations, such as passing through unmanaged or non-transparent switches.
4. MeCalc Device Settings
  - **Sync Interval**: Increase the sync interval (default is 30 ms). Less frequent syncs reduce CPU load and network traffic.
  - **Timeout**: Decrease the default timeout (300 seconds) to help release the sync lock if there are issues.
  - **Sync Offset**: Increase the allowed sync offset to tolerate greater time deviation before rejecting the sync.
  - **Note**: MeCalc cannot sync while streaming data, and cannot stream data while syncing. Plan acquisition accordingly.
5. Troubleshooting Tips
  - Replace the Ethernet cable between the switch and master.
  - Try a different switch port or isolate the MeCalc on a separate PTP domain.
  - Confirm that only one active PTP master exists per domain.
  - Check switch firmware and settings to ensure PTP support and correct behavior.

## Summary

A reliable MeCalc PTP setup requires:

- A properly configured **Transparent Clock (P2P) switch**
- A **dedicated grandmaster clock** with GPS synchronization
- Careful **MeCalc settings and network isolation**

As of now, MeCalc has not provided official documentation on PTP configuration. The above recommendations are based on field experience and troubleshooting shared by users.
