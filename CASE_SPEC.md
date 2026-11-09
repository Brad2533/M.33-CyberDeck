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
- Pointing device: trackball on the right side of the base with two mouse buttons beside it, clear of the keys. Thumb or finger placement is not decided.

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
