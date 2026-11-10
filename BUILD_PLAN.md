# M.33 CyberDeck: Build Plan

As of 2026-11-09. Prices are approximate and change often. This is the Raspberry Pi plan. A mini PC alternative is in `MINI_PC_PLAN.md`, and both are kept current while the choice is made. A memory (DRAM) shortage raised Pi and mini PC prices through 2026, so older estimates were too low. The case design shared by both builds is in `CASE_SPEC.md`.

## Overview

The M.33 CyberDeck is a portable, battery-powered device for wireless packet capture, testing home and home-lab networks, and coding (including Claude Code). Priority is the lowest cost that still does the job.

- Wireless capture in monitor mode for authorized home-lab testing
- Many ports for serial, USB, and older hardware
- Runs with the lid closed, but not all the time
- Portable enough to strap on or carry in a backpack
- Laptop-style option: also usable as a cheap everyday computer (web, IDE, YouTube, Claude Code) with a screen and keyboard

## Compute board

Decision so far: Raspberry Pi 4 (2 GB or 4 GB) for a headless capture hub, with the Pi 5 as the step-up option. For the laptop-style deck (web, IDE, YouTube), the Pi 5 with 8 GB is the preferred board, and 1 GB and 2 GB models are too small.

| Board | Approx. cost | Notes |
| --- | --- | --- |
| Pi Zero 2 W | $15 to $20 | Cheapest, but only one USB port. Too limited for this build. |
| Pi 4 (2 or 4 GB) | $45 to $65 (earlier estimate, likely higher now) | Chosen for the headless capture hub. Enough USB, Ethernet, and HDMI for capture work. |
| Pi 5 (4 GB) | $60 to $80 (earlier estimate, likely higher now) | Faster, but runs hotter and needs its active cooler for sustained loads. |
| Pi 5 (8 GB) | US price not verified | Preferred for the laptop-style deck. One Japanese listing showed ¥36,300 incl. tax. |

Pi prices rose with the DRAM shortage. One [comparison](https://www.jeffgeerling.com/blog/2026/raspberry-pi-cheaper-than-mini-pc/) found a Pi 5 16 GB kit went from $208 (March 2025) to $246.95 (January 2026), though that article says the Pi is now cheaper than a comparable mini PC again. Confirm the US price of the Pi 5 8 GB before budgeting.

Other boards considered but not chosen: Orange Pi 5 or 5 Plus and Radxa Rock 5B (faster than the Pi 5 but with less polished software, and I haven't verified their prices). Arduino and ESP32 are microcontrollers and can't run a desktop OS. An ESP32 may still be useful as a side tool for passive Wi-Fi sniffing on authorized networks.

Open: RAM size (2 GB vs 4 GB) for Wireshark and Claude Code workloads on the headless hub, and the Pi 5 8 GB price for the laptop-style deck.

## Wireless capture

The Pi's built-in Wi-Fi usually can't do monitor mode well, so an external USB adapter is needed.

| Option | Approx. cost | Notes |
| --- | --- | --- |
| Alfa AWUS036ACH or similar | $65 for the USB-C version ($25 to $50 was an earlier estimate) | Common choice for monitor mode and injection. Listing price from [Rokland](https://reach.dog/shop/rokland/products/alfa-awus036ach-usb-c-802-11ac-ac1200-dual-band-high-power-wifi-usb-adapter). |

Decision needed: confirm the chipset supports monitor mode and packet injection on the chosen OS kernel before buying. Only capture on networks you own or have written permission to test.

## Ports and I/O

The Pi provides USB, HDMI, Ethernet, and GPIO pins. Older hardware needs extra adapters.

- Powered USB hub, about $10 to $15, so capture adapters and serial adapters don't overload the Pi's ports
- USB-to-serial adapters, about $5 to $10 each, for serial and console work
- GPIO pins for custom or legacy connections, if needed

Open: which legacy interfaces (serial, JTAG, other) you actually need first, so you buy only those adapters.

## Display and input (laptop-style deck)

| Part | Approx. cost | Notes |
| --- | --- | --- |
| 10 to 11 inch 1080p HDMI IPS screen (USB-powered) | $60 to $90 (estimate) | The official 7 inch Pi display is 800x480, too small for this. |
| Compact keyboard | $20 to $40 (estimate) | A 60% or 65% mechanical or Bluetooth board fits a deck. |
| Touchpad or trackball | $10 to $25 (estimate) | Keeps you from needing a mouse. |

Open: screen size and whether the keyboard sits inside the case or on top.

## Peripherals

**Pointing device (built-in mouse)**

Decision so far (updated): a small USB trackpad on the right side with two mouse buttons beside it, because the deck only travels through rain closed, and a trackpad on the top plate is sealed in when the case is shut. A cheap USB trackball stays as the fallback. Both connect over USB, so either one swaps into the replaceable top plate without changing the rest of the build.

Layout decision: put the pointing device on the right side of the base with two mouse buttons beside it, mouse-style, instead of in the middle. The right hand stays put, and the middle of the deck stays clear of the wrists. A small trackpad (about 2.5 to 3 in wide, or a round pad around 35 mm) is narrower than a trackball zone, which gives about 0.5 to 1.5 in more width for the keyboard. Open: which pad to buy and where the buttons go.

| Option | Reliability | Notes |
| --- | --- | --- |
| Trackball (optical), fallback | Rugged. Works with gloves or damp hands and holds still on bumpy surfaces. Needs occasional cleaning if grit gets under the ball. | Fallback if the trackpad misbehaves. Works wet, so it suits use with the case open outdoors. Takes a few days to learn. Cover or recess the ball to keep dirt out. |
| Trackpad | No moving parts, so mechanically reliable. Can misbehave with wet or sweaty fingers or gloves, and a loose mount or electrical noise can cause jumpy cursors. | Familiar and supports gestures. Needs a flat, exposed surface in the case. |

Prices not checked yet. The earlier estimate of $10 to $25 still applies.

## Power

The battery is the riskiest part of this build. Options so far:

- **Pi 5 needs 5 V at 5 A** for full USB power. A power bank that can't supply that will limit USB output.
- **Example 74 Wh pack:** Intenso PD20000 (20,000 mAh), about €30.85 at [Galaxus](https://galaxus.be/en/s1/product/intenso-pd20000-20000-mah-74-wh-powerbanks-13023817). The listing doesn't state its USB-C PD output wattage, so confirm it supplies 5 V/5 A before buying.
- **USB-C power bank or battery HAT.** Must supply enough current for the board plus USB devices. Underpowered setups cause random crashes.
- **Built-in BMS and protection.** Use a pack with a battery management system and a fuse or protection circuit.
- **Flight limits.** Airlines usually cap carry-on lithium batteries at 100 Wh, with some allowing up to 160 Wh with approval. Check the watt-hour rating printed on the pack. The deck is planned for car and bike use, not flying, so this cap applies only if that changes. See `CASE_SPEC.md` for the battery size target.

Open: target runtime (hours with the lid closed), which decides the pack's watt-hour size. Battery pack and capacity are not yet chosen.

## Switch cluster (power and pass-through modes)

Idea under consideration: three guarded toggle switches (race-car style, with a flip cover) in a row above the trackpad. Not decided yet.

1. **Pi power:** a toggle in the 5 V feed. A Pi 5 needs 5 V at 5 A, so the switch needs a DC rating above that, with a fuse and short thick wires. A Pi starts when power returns. Cutting power on a running Pi risks corrupting the SD card, so shut down first or use an NVMe drive with a journaling filesystem.
2. **Screen power:** cuts the screen's power line. A 10 in panel draws roughly 3 to 4 W, which is large next to a Pi's 2 to 12 W, so it matters most here. These figures are estimates.
3. **Pass-through mode:** the deck acts as the screen, keyboard and trackpad for another computer (a laptop or a second Pi) while the Pi is off. Easiest build: a screen with a second input (HDMI plus USB-C) that switches automatically, a small USB switch (2 in, 1 out) for the keyboard and trackpad, and an HDMI-in and a USB host port on the case panel. Most USB switches use a momentary button, so a latching toggle needs a small relay or a switch with a hardware selector.

Power wiring: the screen and the USB switch must stay powered with the Pi switch off. Feed them from the main battery before the Pi switch, through an inline fuse and the screen switch. A power bank with two USB-C ports can do this directly. Battery requirement: two outputs usable at once (5 V at 5 A for the Pi, plus an always-on USB-C for the screen), and check that the pack does not split its wattage between ports or turn off a port under a small load.

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

Detailed case design (two compartments, battery bay, vent and fan, mounting, antennas): see [CASE_SPEC.md](CASE_SPEC.md).

## Software

- **OS:** Raspberry Pi OS or Kali Linux.
- **Capture tools:** Wireshark and tcpdump.
- **Development:** Claude Code runs on Linux and ARM. The model runs on Anthropic's servers, so the Pi only needs to run the client.

Open: which OS to install first (Pi OS for a general build, Kali for security tooling).

## Budget

Rough starting total for the headless capture hub is about $120 to $145, with the Pi 4 price unverified. Prices are approximate.

**Headless capture hub (Pi 4)**

| Category | Approx. cost | Status |
| --- | --- | --- |
| Raspberry Pi 4 | $45 to $65 (earlier estimate, likely higher) | Chosen |
| Monitor-mode Wi-Fi adapter | About $65 (USB-C Alfa AWUS036ACH) | Chosen type, model not picked |
| Powered USB hub | $10 to $15 | Planned |
| Battery pack | TBD | Not chosen |
| Enclosure | TBD | Not chosen |
| Printer (optional) | $200 to $300 | Only if self-printing |

**Laptop-style deck (Pi 5 8 GB)**

Everything except the board, capture adapter, and case comes to about $125 to $190. Add the Pi 5 8 GB price once it is confirmed.

| Category | Approx. cost | Status |
| --- | --- | --- |
| Raspberry Pi 5 8 GB | US price not verified (earlier $80 to $100 estimate is likely low) | Preferred board |
| 10 to 11 inch 1080p screen | $60 to $90 (estimate) | Not picked |
| Keyboard and touchpad | $30 to $65 (estimate) | Not picked |
| Power bank, 74 Wh | About €31 (Intenso PD20000) | Option, not picked |
| Capture adapter (optional) | About $65 | Only if capture is needed |
| Case | TBD | Not chosen |

Online print services such as JLCPCB or Craftcloud can print test parts for a few dollars each, so you can check fit before buying a printer.

## Open decisions

- [ ] Monitor-mode adapter: pick a model and confirm its chipset supports monitor mode and injection
- [ ] Pi RAM: 2 GB or 4 GB (headless capture hub)
- [ ] Headless capture hub (Pi 4) or laptop-style deck (Pi 5 8 GB)
- [ ] Confirm the US price of the Pi 5 8 GB
- [ ] Screen, keyboard, and touchpad choice for the laptop-style deck
- [ ] Pointing device: small USB trackpad first, with a trackball as the fallback
- [ ] Which trackpad to buy (small pad or round pad) and where the two buttons go on the right side
- [ ] Battery pack: choose capacity from target runtime and check its watt-hour rating
- [ ] Cooling: fan or passive heatsink, and vent layout
- [ ] Enclosure: choose the shell and confirm it fits the Pi, hub, and battery
- [ ] Cyberdeck design: find a Printables or Thingiverse model and check its largest part against printer bed size
- [ ] Printer: self-print or use an online service for test parts
- [ ] Thermal test with the lid closed
- [ ] Target runtime, which drives battery size
- [ ] Switch cluster: confirm it fits above the trackpad, and pick guarded toggles with a DC rating that covers the board's current
- [ ] Pass-through mode: screen with a second input and auto-switching, plus a USB switch for the keyboard and trackpad
- [ ] Battery with two outputs at once: a high-power one for the board and an always-on USB-C one for the screen and USB switch

## Safety and legal

- **Battery:** lithium cells can swell or enter thermal runaway if punctured, overcharged, or crushed. Don't charge the pack while sealed in the case, and keep it padded and away from the computer.
- **Authorized testing only:** capture and test only networks you own or have explicit written permission to test.
