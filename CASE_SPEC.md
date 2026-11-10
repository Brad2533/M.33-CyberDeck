# M.33 CyberDeck: Case Spec

As of 2026-11-09. Shared by both builds (`BUILD_PLAN.md` for the Pi, `MINI_PC_PLAN.md` for the mini PC). This is a design spec, not a tested build. Verify every part and connection before relying on it.

## Use case

- Mostly car, sometimes bike or backpack, rarely anything else.
- Not for flying, so the 100 Wh airline carry-on cap does not apply. Check airline rules first if that changes.
- Use the deck while stopped, not while riding.

## Layout

- One large plastic case with two compartments separated by a wall: a battery bay and an electronics bay.
- All power stays inside the case, so the deck comes off the bag as one unit. No battery or power part lives in the bag.
- Keep the electronics' exhaust path away from the battery bay.
- Mini PC build uses the bare board: the mini PC shell is removed and only the board, heatsink, fan, RAM and SSD are used. Mount the board on standoffs in a rear strip behind the keyboard, with the exhaust at the back.
- Heat: spread it out. Keep the main heat behind the keys, add an air gap and heat shield under the keyboard, and keep the converter and USB hub away from the board.
- Strip the case's foam. Use rigid mounts only, and no foam near heat or the battery.
- Orientation on the bag: the lid's outside faces out and the right side (trackpad side) faces up, so the back vents point out to the wearer's left. The two lid antennas on the right edge then point at the sky.
- Pointing device: small trackpad on the right side of the base with two mouse buttons beside it, clear of the keys. A trackball is the fallback. Keyboard and trackpad sit in a replaceable top plate, with the keyboard opening cut slightly oversize and a bezel so same-size 60% boards swap over USB.

## Board and cabling layout

Shown in `images/02-inside-base.png`. Hinge edge is the back.

- Rear strip, left: the bare board on standoffs, its heatsink and fan, the capture adapter and hub, and power in. Exhaust out the back. The board's I/O edge faces the left end.
- Rear strip, right: the battery bay, behind a wall, with its own membrane vent on the back edge, next to the fan exhaust.
- Front row: the keyboard zone (60 to 65% board, about 11 in wide) and the trackpad with two buttons on the right.
- Port extenders: only for what is plugged in from outside (power in, one or two USB-A, Ethernet if wanted). They exit the left end. The keyboard, trackpad and capture adapter connect inside, so they need no case holes.
- Antennas: two short ones on the lid's right edge, not on the body.
- Across the hinge: one USB-C or HDMI-plus-USB cable to the screen (video, power and touch), plus two thin coax pigtails from the capture adapter to SMA connectors on the lid's right edge. The adapter itself stays in the base.
- If the keyboard and pointing device can share one USB controller, that saves a port and a cable.

## Case candidates

Interior sizes from listings. The sizes below are not yet checked against a real board. Prices change, and the Apache 3800 prices are from expired deal listings.

| Case | Interior (L x W) | Lid + base depth | Notes |
| --- | --- | --- | --- |
| Apache 3800 (Harbor Freight) | 14 7/8 x 10 5/8 in | 6 1/8 in total | Cheapest ($20 to $40 in listings). Deep and heavier. A Pi 4 cyberdeck has been built in one. Plastic is probably polypropylene, which glues poorly, so use screws and backing plates. |
| Pelican 1470 | about 15.7 x 10.7 in | about 1.47 + 2.4 = 3.87 in | The size wanted. About 4.47 in thick outside and 4.28 lb. Expensive ($185 new), so look used. |
| Nanuk 910 | 13.2 x 9.2 in | 1.3 + 2.8 = 4.1 in | $75.95. Tight for a 60% keyboard plus the trackpad. |
| SKB iSeries 1510-4 | 15 x 10.5 in | 1.25 + 3.25 = 4.5 in | IP67, discontinued listing, premium price. |
| Apache 2800, Seahorse 520, Monoprice 13 x 14 x 7 | Too narrow or too deep | | Not suitable. |

Plan: buy an Apache 3800 as a practice case for test cuts, then move to a used Pelican 1470 once the design is settled. Strip the foam from whichever case is used.

## Weight and carry

Estimated 9 to 13 lb for a mini PC build in a large case, 6 to 8 lb for a Pi 5 with a smaller battery. These are estimates, not measurements.

## Switch cluster

Idea under consideration, not decided. Three guarded toggles (flip-cover, race-car style) in a row above the trackpad: board power, screen power, and a pass-through mode where the deck is the screen and keyboard for another computer. Details are in `BUILD_PLAN.md` and `MINI_PC_PLAN.md`.

- Space: a row of three is about 2.5 to 3 in wide and about 1.2 in deep. The right-hand zone is about 3.5 in wide, and the front row is about 4 in deep, so it is tight with a small trackpad on the Pelican 1470. If it does not fit, put it beside the buttons or at the left end by the ports.
- Shutdown button: a separate momentary button (hidden, or a big red arcade style) inside the case, for a clean shutdown. Being inside, a bag cannot press it.
- Case panel: pass-through mode needs an HDMI-in port and a USB host port, with locking connectors like the others.
- Battery: needs two outputs usable at once, one high-power for the board and one always-on for the screen and USB switch.

## Battery bay

- **Capacity:** target about 150 to 200 Wh. That is roughly 6 to 9 hours at a 20 W average and about 1.2 to 2 kg. Larger packs add weight and stored energy without much benefit.
- **Chemistry:** consider LiFePO4. It is heavier but tolerates heat, vibration, and abuse better than standard lithium-ion.
- **Pack:** prefer one finished pack with a built-in battery management system. If using several packs, each needs its own protection and fuse, and mismatched packs must not be wired in parallel.
- **Holding:** padded bay with structure that holds the pack or packs apart and fixed in place.
- **Vent:** passive, water-resistant membrane vent, aimed away from the rider's back and the bag. The vent must work without the fan, because the fan won't help with gas.
- **Fan:** heat-triggered fan for the bay, with a vent path that is not blocked if the fan fails.
- **Safety cutoff:** temperature sensor that cuts power if the pack gets too hot, an inline fuse near the battery, and an external power switch.
- **Charging:** external, covered charge port. Do not charge the pack while it is sealed in the case.
- **Strap protection:** a rigid plate or frame between the straps and the battery bay so strap pressure never reaches the cells.

## Wall between the bays

- Not PLA. It softens around 55 to 60 C.
- Use PETG, ABS, or ASA at minimum. Consider a metal or fire-resistant barrier on the battery side.

## Mounting

- Helmet-style plastic prong (side-release) clips screwed into the corners, strapped to the bag.
- Reinforce each mounting point with a backing plate or washers on the inside, since screws through thin plastic can tear out.
- Seal each screw hole with gasket or sealant if water resistance matters.
- Add a second strap as a backup so the case cannot fall off if a clip fails.
- Test the mounts loaded with the full weight over bumps before real use.

## Antennas

- Some antennas external, mainly the capture adapter's, partly for looks.
- Use gasketed bulkhead SMA connectors with short cables.
- Use caps or short antennas on a bike, since long ones can snag on branches.

## Cables and connectors

- Strain-relieve every cable and use locking or screw-down connectors so vibration doesn't work them loose.
- Seal or grommet any cable passing through a wall.

## Power requirements by build

- **Mini PC (OptiPlex or Lenovo):** the battery bay must deliver 90 W or more, matching the model's adapter. See `MINI_PC_PLAN.md`.
- **Pi 5:** 5 V at 5 A, so the pack needs a USB-C PD output that supplies that.

## Soldering

Prefer screw-terminal, spade or push-on parts so little or no soldering is needed. See the plan docs for the list.

## Weather and heat

- Resistant, not waterproof, is the goal. Vents use membranes or hooded openings.
- Keep the case out of direct sun when parked. A dark case heats the battery.

## Open decisions

- [ ] Case: pick the large plastic case and check internal dimensions against the board, screen, and battery
- [ ] Battery: single finished pack or power-station style, and capacity within 150 to 200 Wh
- [ ] Wall material: PETG, ABS, ASA, or metal
- [ ] Fan: model, trigger temperature, and where the temperature sensor sits
- [ ] Vent: membrane vent model and location
- [ ] Mounts: clip model and reinforcement plan
- [ ] Antenna layout: which are external and where the connectors sit
- [ ] Switch cluster: does it fit above the trackpad, and do the switches carry the board's DC current
- [ ] Shutdown button: style (hidden or big red) and where it sits
