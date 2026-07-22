from ase.spacegroup import crystal
from ase.io import write

def base(a=6.39):
    u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
                spacegroup=221, cellpar=[a]*3+[90]*3)
    return u.repeat((2,2,2))

def make(tag, swaps):
    at = base()
    for sym_from, sym_to, n in swaps:
        idx = [a.index for a in at if a.symbol == sym_from][:n]
        for i in idx: at[i].symbol = sym_to
    write(f"candfull_{tag}.xyz", at)          # full lattice
    I = [a.index for a in at if a.symbol == 'I']
    vac = at.copy(); hole = vac.positions[I[0]].copy(); del vac[I[0]]
    write(f"cand_{tag}.xyz", vac)             # with vacancy
    print(f"{tag}: {vac.get_chemical_formula()} {len(vac)} atoms")

make("base", [])
make("br",   [('I','Br',6)])
make("rb",   [('Cs','Rb',2)])
make("k",    [('Cs','K',2)])
