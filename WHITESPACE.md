# White-space map — CsPbI3 / halide perovskite stabilization
## Landscape density (Google Patents, exact-phrase queries, Jul 14)
- "perovskite" AND "iodide migration": 11
- "cesium lead iodide" AND "stabilization": 43
- "CsPbI3" AND "black phase": 53
- "CsPbI3" AND "additive": 118
- (fuzzy queries returned 4,900-15,000 = noise; exact phrases are the instrument)
- HEADLINE: the specific-mechanism landscape is SMALL. Nobody has fenced this field.

## CROWDED: interface / barrier layers ("build a wall") - 6 of 11
PbS buffer layer | quaternary-ammonium passivation | ALD resistive-oxide buffer (Dhakal)
| metal-salt diffusion layer (Lunt) | SiOx core-shell (Sum) | Li-quinolinolate layer
Common logic: block the iodide from LEAVING. External to the crystal.

## THINNER: additives / composition - 3 of 11
non-stoichiometric FA/Cs ink (Huang) | imidazole additive (Hou) | Eu-doped Sn (Zhou)

## OPEN / THIN ICE (day-1 read)
- Almost nobody targets the INTRINSIC migration barrier inside the lattice.
  The field builds walls; our instrument measures hills (NEB, Phase 3).
- Junk rate on the 11: ~18% (2 stray matches).

## Contradictions found
- [TO FILL: which two patents disagree, and on what]

## Notes
- These are granted/published patents ($15-30k+ each, corporate/university legal depts).
  Our $5k = provisional only: 12-month cheap date-stake, then the expensive convert-or-abandon decision.

## The 53 ("CsPbI3" AND "black phase") - page 1, Jul 15
Benji's blind prediction: ~20% overlap with wall-builders. HIT (2 of 10).
CROWD MOVED: this sample is dominated by SYNTHESIS/PROCESSING, not barriers -
carbohydrazide precursor additive | electrochemical growth route | QD hot-injection |
heat-treatment phase control | MOF-glass composite | mixed-cation (Saliba/Oxford) |
single-crystal growth (Bakr/KAUST) | transition-metal-doped QDs (150x damp-heat stability)
Walls (2): ferrocene protective layer | MAI grain-boundary passivation
Mentor prediction (crowded=composition, thin=process/interface): MISS in BOTH samples,
opposite directions. Interface crowded in the 11; process crowded in the 53.
PERSISTENT HOLE (21 patents, 2 samples): nobody targets the INTRINSIC lattice migration barrier.
The field: build walls, tune recipes. Us: measure and raise the hill.

## MECHANISM-MENU ENTRY (best find so far)
Strain-release layer patent (oxysilane at CsPbI3/TiO2 interface): the ONLY patent naming a full
mechanism chain - thermal-expansion mismatch -> interfacial lattice distortion -> defect formation
-> accelerated polymorphic transformation (black->yellow). Numbers: 20.1% PCE, T90=1800 h encapsulated, MPP, continuous illumination.
WHY IT MATTERS: strain is COMPUTABLE. Strained cell in GPAW -> effect on migration barrier.
This is a testable hypothesis with a published number to check against. Flag for Phase 3.

## The 43 ("cesium lead iodide" AND "stabilization") - page 1, Jul 15
Benji's blind prediction: <=10% overlap with the 53. HIT (~0-1 shared patents). 2 blind predictions, 2 hits.
SATURATION: NO at the patent level (little repeat), YES at the LEVER level. Contents:
bilateral amines (Huang) | mixed-solvent inks (Huang) | doped halide perovskites (Sargent/Saidaminov)
| cubic-phase nanowire synthesis | 2D perovskite templates (Mohite) | restricted annealing |
luminescent crystals | optical processing of phase behaviour (Hofkens/Steele) | ammonium-cation additives
| lead-chelating HTL (Huang)
= the SAME 3 levers (additive / process / interface) in 43 costumes. Heavyweights all present:
Huang (x3-4), Saliba, Bakr, Mohite, Sargent.

## THE HOLE AT 31 PATENTS (3 samples): still nobody touches the intrinsic lattice barrier.
KEY OBSERVATION (why the hole exists): every patent here is something you can DO TO A FILM IN A LAB -
add a molecule, change a solvent, tune an anneal, deposit a layer. The intrinsic barrier is not an ACTION,
it's a PROPERTY. The field patents what it can demonstrate, and demonstrates what its hands can do.
=> supports candidate reason (b) "unmeasurable/undemonstrable" over (a) "too hard".
This is either our opening or the field's wisdom. The PAPER half decides.

## The 118 ("CsPbI3" AND "additive") - page 1 sample, Jul 15
Mentor blind prediction (saturated at lever level, hole still open): HIT, 4 of 4.
Repeats from the 43: mixed-solvent inks (Huang), bilateral amines (Huang), Bakr single crystals. Snaith x2, Saliba x2.
Contents: gamma-CsPbI3 nanomaterials | QD compositions (Samsung) | encapsulated nanoparticles |
mixed-cation Cs/FA/Br-I (Saliba/Snaith/Oxford) | porous dielectric scaffold (Snaith) | composite emitters
= same 3 levers, 4th costume change.

## PATENT HALF: CLOSED (Jul 15, 3 days, 41 patents across 4 queries)
VERDICT: the field's entire IP landscape rests on 3 levers - additives, processing recipes, interface layers.
All three are ACTIONS PERFORMED ON A FILM. Nobody claims the intrinsic lattice migration barrier,
because a barrier is a PROPERTY, not an action - you cannot demonstrate it with hands, so you cannot patent it.
Best mechanism find: strain-release layer (thermal mismatch -> distortion -> defects -> black->yellow; T90=1800h, 20.1%).
NEXT: paper half. Target question - is the hole an OPENING (nobody could compute barriers pre-MLIP)
or the FIELD'S WISDOM (barrier can't be moved without breaking the absorber)?
