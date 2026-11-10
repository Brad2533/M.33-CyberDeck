# M.33 CyberDeck: Mini PC Build Plan

As of 2026-11-09. Prices are approximate and change often. This is an alternative to the Raspberry Pi plan in `BUILD_PLAN.md`. Both are being kept current while the choice is made. A memory (DRAM) shortage raised mini PC and Pi prices through 2026, so older estimates in earlier versions of this plan were too low. Figures below were rechecked on 2026-11-09 where a source is noted.

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
| Intel N100 | $120 to $160 (earlier estimate, not rechecked, likely higher) | About 6 to 15 W | Enough for web, IDE, video, and Claude Code. Limited headroom. |
| Intel N150, new, 16 GB / 512 GB | $281 to $550, median $349 | About 6 to 15 W | Slightly faster than N100. Was about $158 in 2025. Barebone (no RAM or SSD) was $235. |
| AMD Ryzen 7 8845HS mini PC | $829 to $939 with 32 GB / 1 TB, $349 to $383 barebone | Higher under load | Much more headroom. Heavier battery needed. |

Source for the N150 and Ryzen figures: [Computing for Geeks](https://computingforgeeks.com/mini-pc-prices/), Amazon US prices pulled 2026-11-01.

Decision needed: N150 for a first build, a used business mini PC (see below), or a Ryzen model if you want headroom for heavier work. Used units now cost less than new N150 boxes.

Specs to check on any model:

- 16 GB RAM (8 GB is the minimum for comfortable browsing with many tabs)
- 256 GB or larger SSD
- Multiple USB-A ports, HDMI, and at least one USB-C
- 2.5 GbE Ethernet if homelab transfers matter
- Fan and cooling that fit inside the case

## Used business mini PC options

Dell OptiPlex 7xxx Micro and Lenovo ThinkCentre Tiny units are strong enough for web, IDE, YouTube, and Claude Code. Prices below are Amazon Renewed listings checked on 2026-10-20 (see [Computing for Geeks](https://computingforgeeks.com/best-used-tiny-pc-homelab/)). eBay and local listings may be cheaper. Prices change often.

| Model | CPU gen | Approx. price | RAM and storage | Notes |
| --- | --- | --- | --- | --- |
| Lenovo M920q | 8th/9th | $210 to $240 | Up to 32 GB RAM, 1 NVMe plus 2.5 in | Guide's main pick. Has a PCIe riser slot for a later NIC. |
| Lenovo M720q (32 GB installed) | 8th/9th | About $363 | Up to 32 GB, 1 NVMe plus 2.5 in | Riser slot, no vPro. |
| Lenovo M90q Gen 1 | 10th | $300 to $350 | Up to 64 GB, 2 NVMe plus 2.5 in | Riser slot uses the 2.5 in bay. |
| Dell OptiPlex 7070 Micro | 9th | $237 to $252 | Up to 32 GB, 1 NVMe plus 2.5 in | No user PCIe slot. |
| Dell OptiPlex 7080 Micro | 10th | About $296 | Up to 64 GB, 2 NVMe plus 2.5 in | Newer, more headroom. |

- Prefer 35 W T-series CPUs (for example i5-8500T or i5-10500T). They are 6-core chips that handle this workload.
- Other OptiPlex 7xxx generations exist (7060, 7010, 7020), but I haven't priced them for this plan.
- Dell Micros have no user PCIe slot, and Micro boards usually have one onboard Ethernet port.

**Adapter and battery warning**

- Dell recommends a [90 W or higher adapter](https://dell.com/support/kbdoc/en-md/000221342/no-power-no-display-or-alert-about-undersized-power-adapter-on-optiplex-micro-form-factor) for OptiPlex Micros. Undersized adapters can cause no power, no display, or an undersized-adapter warning.
- The guide reports a 7070 Micro showing a boot error on a 65 W adapter, and an M920q throttling on one.
- Whatever battery is used must deliver 90 W or more at the model's input voltage. The TalentCell 19.5 V / 3 A pack (about 58 W) is likely too small.
- Confirm the adapter connector and any ID signal the model expects before buying a battery.

Decision needed: pick a model (cheapest of these: Lenovo M920q; more headroom: OptiPlex 7080 Micro).

**Board-only build (decided)**

The mini PC's shell will not be kept. Only its insides are used as parts: the motherboard with its heatsink and fan, plus the RAM and SSD. This is a big part of the fun of the build, and it is why thickness matters so much.

- Keep the original heatsink and fan, since they are designed for the board. Plan an air path from an intake to the fan and out an exhaust vent, because the stock shell used to provide that duct.
- The rear I/O ports (USB, Ethernet, HDMI, power jack) sit on the board edge, so cut openings in the case to reach them, or use short extension cables to a panel.
- Check teardown photos for the chosen model before buying: board size, height with cooler, port positions, and whether the power jack and any adapter ID signal can be reused. I haven't verified these figures.
- Thin, bare boards can sit in a rear strip behind the keyboard, which keeps heat out from under the hands.

## Wireless capture

The built-in Wi-Fi on most mini PCs will not do monitor mode, so an external USB adapter is still needed for capture.

| Option | Approx. cost | Notes |
| --- | --- | --- |
| Alfa AWUS036ACH or similar | $65 for the USB-C version ($25 to $50 was an earlier estimate) | Common choice for monitor mode and injection. Listing price from [Rokland](https://reach.dog/shop/rokland/products/alfa-awus036ach-usb-c-802-11ac-ac1200-dual-band-high-power-wifi-usb-adapter). |

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

Most mini PCs take 12 V or 19 V DC, not USB-C power, so a standard power bank may not work.

- **Battery with 12 V or 19 V output:** Simplest route. Check that the output voltage and current match the mini PC's power brick.
- **Power bank plus DC-DC converter:** Works with a standard power bank, but adds parts and heat.
- **Watt-hour limit:** The deck is for car and bike use, not flying, so the 100 Wh airline cap does not apply. Target about 150 to 200 Wh (see `CASE_SPEC.md`).
- **Output wattage:** At least 90 W for OptiPlex and Lenovo units (see the adapter warning above).

Target runtime: about 3 to 6 hours with the screen on and mixed use. Battery pack not yet chosen.

Open: pack capacity and output voltage, once the mini PC model is picked.

## Switch cluster (power and pass-through modes)

Idea under consideration: three guarded toggle switches (race-car style, with a flip cover) in a row above the trackpad. Not decided yet.

1. **PC power:** a toggle in the DC feed to the board. At 90 W and 19 V that is about 5 A, so the switch needs a DC rating above that. It is a hard cut, not a clean shutdown. Set the BIOS to power on after power loss, so flipping it on boots the board.
2. **Screen power:** cuts the screen's power line. A 10 in panel draws roughly 3 to 4 W, so it saves about 15 to 25% on headless jobs. These figures are estimates.
3. **Pass-through mode:** the deck acts as the screen, keyboard and trackpad for another computer (a Pi or a laptop) while the internal board is off. Easiest build: a screen with a second input (HDMI plus USB-C) that switches automatically, a small USB switch (2 in, 1 out) for the keyboard and trackpad, and an HDMI-in and a USB host port on the case panel. Most USB switches use a momentary button, so a latching toggle needs a small relay or a switch with a hardware selector.

Power wiring: the screen and the USB switch must stay powered with the PC switch off. Feed them from the main battery before the PC switch, through an inline fuse and the screen switch. If the pack has a spare USB-C port, plug them into that. If the pack has only a 19 V DC output, add a small step-down converter to 5 V or a PD trigger module. Battery requirement: two outputs usable at once (high-power for the board, always-on USB-C for the screen). Check that the pack does not split its wattage between ports or turn off a port under a small load.

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

Detailed case design (two compartments, battery bay, vent and fan, mounting, antennas): see [CASE_SPEC.md](CASE_SPEC.md).

## Software

- **OS:** Ubuntu or Kali Linux for security tooling, or Windows if you want to run Windows-only apps.
- **Capture tools:** Wireshark and tcpdump.
- **Development:** Claude Code runs in a terminal. The model runs on Anthropic's servers, so the mini PC only needs to run the client.

Open: which OS to install first.

## Budget

Rough subtotal before battery, case, and capture gear: about $300 to $390 with a used Lenovo M920q, or about $370 to $500 with a new N150 ($281 to $349 median range). Prices are approximate. Screen and keyboard figures are estimates, not priced listings.

| Category | Approx. cost | Status |
| --- | --- | --- |
| Mini PC, new N150 (16 GB, 512 GB) | $281 to $550, median $349 | Options, not picked |
| Mini PC, used Lenovo M920q | $210 to $240 | Option, not picked |
| Mini PC, used OptiPlex 7070 Micro | $237 to $252 | Option, not picked |
| Mini PC, used OptiPlex 7080 Micro | About $296 | Option, not picked |
| Mini PC, used Lenovo M90q Gen 1 | $300 to $350 | Option, not picked |
| Mini PC, used Lenovo M720q (32 GB) | About $363 | Option, not picked |
| Screen | $60 to $90 | Not picked |
| Keyboard and touchpad | $30 to $60 | Not picked |
| Battery with DC output, 150 to 200 Wh, 90 W+ | Not priced. The earlier $50 to $100 estimate is likely too low. | Not picked |
| Capture adapter and hub (optional) | Adapter about $65, plus hub $10 to $15 | Only if capture is needed |
| Case | TBD | Not chosen |

## Open decisions

- [ ] Mini PC class: N150 for a first build, or a Ryzen model for more headroom
- [ ] Used model: Lenovo M920q, Lenovo M90q, OptiPlex 7070, or OptiPlex 7080 Micro
- [ ] Battery that delivers 90 W or more at the model's adapter voltage
- [ ] RAM: 16 GB recommended
- [ ] Screen size and layout
- [ ] Keyboard and touchpad choice
- [ ] Pointing device: small USB trackpad first, with a trackball as the fallback
- [ ] Which trackpad to buy (small pad or round pad) and where the two buttons go on the right side
- [ ] Battery pack: output voltage, capacity, and watt-hour rating
- [ ] Cooling: fan layout and vent positions
- [ ] Case: rugged shell, printed case, or existing cyberdeck design
- [ ] Monitor-mode adapter: pick a model and confirm its chipset supports monitor mode and injection
- [ ] OS: Ubuntu, Kali, or Windows
- [ ] Thermal test with the lid closed
- [ ] Switch cluster: confirm it fits above the trackpad, and pick guarded toggles with a DC rating that covers the board's current
- [ ] Pass-through mode: screen with a second input and auto-switching, plus a USB switch for the keyboard and trackpad
- [ ] Battery with two outputs at once: a high-power one for the board and an always-on USB-C one for the screen and USB switch

## Safety and legal

- **Battery:** lithium cells can swell or enter thermal runaway if punctured, overcharged, or crushed. Don't charge the pack while sealed in the case, and keep it padded and away from the computer.
- **Authorized testing only:** capture and test only networks you own or have explicit written permission to test, including the homelab.
