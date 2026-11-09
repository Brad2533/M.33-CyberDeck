# M.33 CyberDeck

A portable, battery-powered cyberdeck for wireless capture, network security testing of home-lab gear, and coding (including Claude Code).

## Goals

- Wireless packet capture (monitor mode) for testing home and home-lab networks
- Many ports to reach serial, USB, and other legacy or modern I/O
- Runs when closed, portable, and as cheap as possible
- Fully authorized testing only: capture and test only networks I own or have written permission to test

## Concept images

Early concept drawings of the deck. They are close to the intended design, but the board, battery pack, and exact layout are not final.

- `images/01-open.png`: the open deck (screen, keyboard, trackpad on the right with two buttons, antennas, corner clips, end vent)
- `images/02-inside-base.png`: top-down plan of the base (bare board in a rear strip with back exhaust, wall, battery bay, keyboard zone, trackpad)
- `images/03-on-bag.png`: closed case clipped to a backpack with a backup strap

The editable design canvas is "M.33 CyberDeck Concept" in Claude. The PNGs are renders of it and use a fallback font.

## Status and decisions

Two builds are being developed in parallel while the choice is open. Options stay in the docs unless a decision is made to drop them.

- `BUILD_PLAN.md`: Raspberry Pi plan (headless capture hub with a Pi 4, or a laptop-style deck with a Pi 5 8 GB)
- `MINI_PC_PLAN.md`: mini PC plan (new N150, or used OptiPlex 7xxx Micro and Lenovo ThinkCentre Tiny units)
- `CASE_SPEC.md`: shared case design for car, bike, and backpack use

Decisions so far:

- Surface Pro: not used for the deck. Tearing it down is risky (glued screen and battery), so it is planned as a server instead.
- Arduino and ESP32: ruled out as the main board because they can't run a desktop OS. An ESP32 may be a side tool.
- Use case: car, bike, and backpack, not flying, so the 100 Wh airline battery cap does not apply. Battery target is about 150 to 200 Wh.
- OptiPlex and Lenovo mini PCs need a battery that delivers 90 W or more.
- Mini PC build: the shell is removed and only the board, heatsink, fan, RAM and SSD are used. Case thinness matters, and the case needs to be easy to cut.
- Pointing device: a small USB trackpad on the right side with two mouse buttons beside it, with a cheap USB trackball as the fallback. The deck only travels through rain closed, so the trackpad is sealed in. The keyboard is a wired USB 60% board in a replaceable top plate.
- Prices rose through 2026 because of the DRAM shortage. Older estimates in earlier versions were too low.

## Hardware plan (draft)

This is the original draft. See the plan docs above for current options and prices.


| Part | Choice | Est. cost |
|---|---|---|
| Compute | Raspberry Pi 4 (2 GB or 4 GB). Pi 5 is the step-up option, but it runs hotter and needs its active cooler. | $45 to $65 |
| Wireless capture | USB adapter with a monitor-mode and packet-injection chipset (e.g. Alfa AWUS036ACH or similar). Verify chipset before buying. | $25 to $50 |
| Ports | Powered USB hub, plus USB-to-serial adapters as needed | $10 to $25 |
| Power | USB-C power bank or battery HAT that supplies enough current for board plus USB devices | TBD |
| Enclosure | Rugged slim case (Pelican Micro, Nanuk, SKB, or Gator) with 3D-printed inserts, or a fully printed case | TBD |

Rough starting total: about $90 to $130 (Pi 4, monitor-mode adapter, hub).

## Software plan

- Raspberry Pi OS or Kali Linux
- Wireshark and tcpdump for captures
- Claude Code for development

## Build notes

### Thermal
- Sealed cases trap heat. Vent the computer side as well as the battery side.
- Heatsink on the processor, or a small fan.
- Keep PLA parts away from the warmest components (PLA softens around 55 to 60 C).
- Measure before trusting it: temperature sensors on the chip and battery, one-hour test under real load with the lid closed. Check `vcgencmd get_throttled` on a Pi.

### Battery safety
- Use a pack with a built-in BMS and a fuse or protection circuit.
- Do not charge the pack while sealed inside the case.
- Give the battery its own compartment, padded, not crushable, with vent holes and mesh or foam filter.
- Keep the power switch reachable for quick shutdown.
- Check watt-hour rating before flying (commonly 100 Wh carry-on limit, some airlines allow up to 160 Wh with approval).

### Enclosure
- Sealed cable glands or gaskets for ports if water resistance is wanted.
- Water resistance is optional; ruggedness and venting are the priority.

## Open questions

- [ ] Confirm the chosen Wi-Fi adapter's chipset supports monitor mode and injection on the Pi OS kernel
- [ ] Choose the battery pack and measure its runtime under load
- [ ] Choose the enclosure and confirm it fits the Pi, hub, and battery
- [ ] Find or design the cyberdeck case (Printables / Thingiverse), and check the largest part against printer bed size
- [ ] Pick a printer if self-printing (budget options around $200 to $300)
- [ ] Thermal test with the lid closed

## Ethics and legal

Only capture or test traffic on networks I own or have explicit written permission to test.
