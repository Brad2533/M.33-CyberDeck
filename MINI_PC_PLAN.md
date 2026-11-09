# M.33 CyberDeck: Mini PC Build Plan

As of 2026-11-09. Prices are approximate and change often. This is an alternative to the Raspberry Pi plan in `BUILD_PLAN.md`. Both are being kept current while the choice is made.

## Overview

A portable, cyberdeck-style computer built around a mini PC. It runs a full desktop for web, IDE, video, and Claude Code, and it can be used for wireless capture and homelab work when needed. The build itself is part of the goal, so the case and layout matter as much as the specs.

- Full desktop for web, IDE, YouTube, and Claude Code
- Wireless capture in monitor mode for authorized homelab testing, through a USB adapter
- Portable, with a screen, keyboard, and battery in one case
- Looks like a cyberdeck, and is built by hand

## Compute: mini PC

Options so far:

| Class | Approx. cost | Power draw | Notes |
| --- | --- | --- | --- |
| Intel N100 | $120 to $160 | About 6 to 15 W | Enough for web, IDE, video, and Claude Code. Limited headroom. |
| Intel N150 | $150 to $220 | About 6 to 15 W | Slightly faster than N100. Recommended starting point. |
| AMD Ryzen 7 mini PC | $300 to $400 | Higher under load | Much more headroom. Heavier battery needed. |

Decision needed: N150 for a first build, or a Ryzen model if you want headroom for heavier work.

Specs to check on any model:

- 16 GB RAM (8 GB is the minimum for comfortable browsing with many tabs)
- 256 GB or larger SSD
- Multiple USB-A ports, HDMI, and at least one USB-C
- 2.5 GbE Ethernet if homelab transfers matter
- Fan and cooling that fit inside the case

## Wireless capture

The built-in Wi-Fi on most mini PCs will not do monitor mode, so an external USB adapter is still needed for capture.

| Option | Approx. cost | Notes |
| --- | --- | --- |
| Alfa AWUS036ACH or similar | $25 to $50 | Common choice for monitor mode and injection. |

Decision needed: confirm the chipset supports monitor mode and packet injection on the chosen OS before buying. Only capture on networks you own or have written permission to test.

## Ports and I/O

Mini PCs usually cover most ports directly, so a hub may not be needed.

- Check the number of USB-A ports before buying a hub.
- USB-to-serial adapters, about $5 to $10 each, for serial and console work.
- Confirm the model has the video output you need for the screen.

Open: which legacy interfaces (serial, JTAG, other) you actually need first.

## Display and input

| Part | Approx. cost | Notes |
| --- | --- | --- |
| 10 to 11 inch 1080p HDMI IPS screen (USB-powered) | $60 to $90 | Sized for a deck-style layout. |
| Compact keyboard | $20 to $40 | A 60% or 65% mechanical or Bluetooth board fits a deck. |
| Touchpad or trackball | $10 to $25 | Keeps you from needing a mouse. |

Open: screen size and whether the keyboard sits inside the case or on top.

## Power

Most mini PCs take 12 V or 19 V DC, not USB-C power, so a standard power bank may not work.

- **Battery with 12 V or 19 V output:** Simplest route. Check that the output voltage and current match the mini PC's power brick.
- **Power bank plus DC-DC converter:** Works with a standard power bank, but adds parts and heat.
- **Watt-hour limit:** Keep the pack under 100 Wh for carry-on flights.

Target runtime: about 3 to 6 hours with the screen on and mixed use. Battery pack not yet chosen.

Open: pack capacity and output voltage, once the mini PC model is picked.

## Cooling

- A mini PC's fan needs clear airflow. Plan vents on both intake and exhaust sides.
- Keep the battery and DC converter away from the warmest part of the mini PC.
- Test under real load with the lid closed for an hour before trusting the case.

Open: fan layout and vent positions, once the case is chosen.

## Case and enclosure

Options so far:

| Option | Approx. cost | Notes |
| --- | --- | --- |
| Rugged hard case (Pelican Micro, Nanuk, SKB, Gator) with printed inserts | Varies | Protective, easy to seal and vent. |
| Fully 3D-printed case | Printer cost plus filament | Most custom look. Harder to make rigid and vented. |
| Cyberdeck design from Printables or Thingiverse | Free to download | Start from an existing design and adjust for your mini PC. |

Open: pick the case after the mini PC and screen sizes are fixed. Check the largest part against printer bed size if printing.

## Software

- **OS:** Ubuntu or Kali Linux for security tooling, or Windows if you want to run Windows-only apps.
- **Capture tools:** Wireshark and tcpdump.
- **Development:** Claude Code runs in a terminal. The model runs on Anthropic's servers, so the mini PC only needs to run the client.

Open: which OS to install first.

## Budget

Rough total: about $325 to $500, depending on the mini PC and battery. Prices are approximate.

| Category | Approx. cost | Status |
| --- | --- | --- |
| Mini PC (N150, 16 GB, 256 GB+) | $150 to $220 | Recommended, not picked |
| Screen | $60 to $90 | Not picked |
| Keyboard and touchpad | $30 to $60 | Not picked |
| Battery with DC output | $50 to $100 | Not picked |
| Capture adapter and hub (optional) | $35 to $65 | Only if capture is needed |
| Case | TBD | Not chosen |

## Open decisions

- [ ] Mini PC class: N150 for a first build, or a Ryzen model for more headroom
- [ ] RAM: 16 GB recommended
- [ ] Screen size and layout
- [ ] Keyboard and touchpad choice
- [ ] Battery pack: output voltage, capacity, and watt-hour rating
- [ ] Cooling: fan layout and vent positions
- [ ] Case: rugged shell, printed case, or existing cyberdeck design
- [ ] Monitor-mode adapter: pick a model and confirm its chipset supports monitor mode and injection
- [ ] OS: Ubuntu, Kali, or Windows
- [ ] Thermal test with the lid closed

## Safety and legal

- **Battery:** lithium cells can swell or enter thermal runaway if punctured, overcharged, or crushed. Don't charge the pack while sealed in the case, and keep it padded and away from the computer.
- **Authorized testing only:** capture and test only networks you own or have explicit written permission to test, including the homelab.
