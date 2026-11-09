# M.33 CyberDeck: Build Plan

As of 2026-11-09. Prices are approximate and change often.

## Overview

The M.33 CyberDeck is a portable, battery-powered device for wireless packet capture, testing home and home-lab networks, and coding (including Claude Code). Priority is the lowest cost that still does the job.

- Wireless capture in monitor mode for authorized home-lab testing
- Many ports for serial, USB, and older hardware
- Runs with the lid closed, but not all the time
- Portable enough to strap on or carry in a backpack

## Compute board

Decision so far: Raspberry Pi 4 (2 GB or 4 GB), with the Pi 5 as the step-up option.

| Board | Approx. cost | Notes |
| --- | --- | --- |
| Pi Zero 2 W | $15 to $20 | Cheapest, but only one USB port. Too limited for this build. |
| Pi 4 (2 or 4 GB) | $45 to $65 | Chosen. Enough USB, Ethernet, and HDMI for capture work. |
| Pi 5 | $60 to $80 | Faster, but runs hotter and needs its active cooler for sustained loads. |

Open: RAM size (2 GB vs 4 GB) for Wireshark and Claude Code workloads.

## Wireless capture

The Pi's built-in Wi-Fi usually can't do monitor mode well, so an external USB adapter is needed.

| Option | Approx. cost | Notes |
| --- | --- | --- |
| Alfa AWUS036ACH or similar | $25 to $50 | Common choice for monitor mode and injection. |

Decision needed: confirm the chipset supports monitor mode and packet injection on the chosen OS kernel before buying. Only capture on networks you own or have written permission to test.

## Ports and I/O

The Pi provides USB, HDMI, Ethernet, and GPIO pins. Older hardware needs extra adapters.

- Powered USB hub, about $10 to $15, so capture adapters and serial adapters don't overload the Pi's ports
- USB-to-serial adapters, about $5 to $10 each, for serial and console work
- GPIO pins for custom or legacy connections, if needed

Open: which legacy interfaces (serial, JTAG, other) you actually need first, so you buy only those adapters.

## Power

The battery is the riskiest part of this build. Options so far:

- **USB-C power bank or battery HAT.** Must supply enough current for the board plus USB devices. Underpowered setups cause random crashes.
- **Built-in BMS and protection.** Use a pack with a battery management system and a fuse or protection circuit.
- **Flight limits.** Airlines usually cap carry-on lithium batteries at 100 Wh, with some allowing up to 160 Wh with approval. Check the watt-hour rating printed on the pack.

Open: target runtime (hours with the lid closed), which decides the pack's watt-hour size. Battery pack and capacity are not yet chosen.

## Cooling

A sealed case traps heat from the board and the battery. Venting only the battery is not enough.

- **Rough load figures:** idle or light browsing draws about 2 to 4 W, sustained load about 6 to 12 W.
- **Throttle risk:** in a sealed plastic box the chip can hit its throttle point (around 80 C) within tens of minutes to a couple of hours under load.
- **Vent the computer side too.** A vent over the board or a small fan helps more than battery mesh.
- **Heatsink** on the processor, or a case lid that conducts heat away.
- **Keep PLA away from heat.** PLA softens around 55 to 60 C, so keep printed mounts clear of the warmest parts.
- **Lower the load** by capping the clock speed or limiting background tasks.

Measurement plan: temperature sensors on the chip and battery, one hour of real workload with the lid closed, then check `vcgencmd get_throttled` on a Pi.

Open: fan or passive heatsink, and which vent layout to use.

## Case and enclosure

Two routes are on the table. The hard shell is the easier starting point.

| Option | Approx. cost | Notes |
| --- | --- | --- |
| Pelican Micro series | Not priced yet | Slim and rugged. Less watertight than the standard Pelican line. |
| Nanuk or SKB slim case | Not priced yet | Impact-resistant, padded dividers. |
| Gator or similar hard tool case | Lower | Good impact protection, basic seals. |
| Fully 3D-printed case | Printer cost plus filament | Most flexible, but harder to make watertight and vent safely. |

- **Hard shell with printed inserts** (chosen direction): a separate, vented battery pocket, sealed from the electronics. Look for a pressure valve or splash-resistant vent.
- **Cyberdeck design:** start from existing Printables or Thingiverse designs, then adjust in Tinkercad if needed.

Open: pick the shell model after the board and battery sizes are fixed.

## Software

- **OS:** Raspberry Pi OS or Kali Linux.
- **Capture tools:** Wireshark and tcpdump.
- **Development:** Claude Code runs on Linux and ARM. The model runs on Anthropic's servers, so the Pi only needs to run the client.

Open: which OS to install first (Pi OS for a general build, Kali for security tooling).

## Budget

Rough starting total is about $90 to $130. Prices are approximate.

| Category | Approx. cost | Status |
| --- | --- | --- |
| Raspberry Pi 4 | $45 to $65 | Chosen |
| Monitor-mode Wi-Fi adapter | $25 to $50 | Chosen type, model not picked |
| Powered USB hub | $10 to $15 | Planned |
| Battery pack | TBD | Not chosen |
| Enclosure | TBD | Not chosen |
| Printer (optional) | $200 to $300 | Only if self-printing |

Online print services such as JLCPCB or Craftcloud can print test parts for a few dollars each, so you can check fit before buying a printer.

## Open decisions

- [ ] Monitor-mode adapter: pick a model and confirm its chipset supports monitor mode and injection
- [ ] Pi RAM: 2 GB or 4 GB
- [ ] Battery pack: choose capacity from target runtime and check its watt-hour rating
- [ ] Cooling: fan or passive heatsink, and vent layout
- [ ] Enclosure: choose the shell and confirm it fits the Pi, hub, and battery
- [ ] Cyberdeck design: find a Printables or Thingiverse model and check its largest part against printer bed size
- [ ] Printer: self-print or use an online service for test parts
- [ ] Thermal test with the lid closed
- [ ] Target runtime, which drives battery size

## Safety and legal

- **Battery:** lithium cells can swell or enter thermal runaway if punctured, overcharged, or crushed. Don't charge the pack while sealed in the case, and keep it padded and away from the computer.
- **Authorized testing only:** capture and test only networks you own or have explicit written permission to test.
