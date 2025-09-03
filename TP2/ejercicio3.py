#Para realizar este ejercicio, instalamos la librería rdkit en conda y luego creamos un entorno virtual
#Para crear el entorno virtual:

from admet_module import analisis_completo
import pandas as pd
from rdkit import Chem

#SMILES punto 1.a
punto_1_a = {
    "aspirin": "CC(=O)OC1=CC=CC=C1C(=O)O",
    "paracetamol": "CC(=O)NC1=CC=C(C=C1)O",
    "caffeine": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
}

#SMILES punto 1.b (algunos isoméricos, los convertimos)
punto_1_b = {
    "teniposide": "COC1=CC(=CC(=C1O)OC)[C@H]2[C@@H]3[C@H](COC3=O)[C@@H](C4=CC5=C(C=C24)OCO5)O[C@H]6[C@@H]([C@H]([C@H]7[C@H](O6)CO[C@H](O7)C8=CC=CS8)O)O",
    "ecteinascidin": "CC1=CC2=C([C@@H]3[C@@H]4[C@H]5C6=C(C(=C7C(=C6[C@@H](N4[C@H]([C@H](C2)N3C)C#N)COC(=O)[C@@]8(CS5)C9=CC(=C(C=C9CCN8)O)OC)OCO7)C)OC(=O)C)C(=C1OC)O",
    "imatinib": "CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)CN3CCN(CC3)C)NC4=NC=CC(=N4)C5=CN=CC=C5",
    "luteolin-7-O-glucoside": "C1=CC(=C(C=C1C2=CC(=O)C3=C(C=C(C=C3O2)O[C@H]4[C@@H]([C@H]([C@@H]([C@H](O4)CO)O)O)O)O)O)O"
    # Falta (10E)-9-oxo-10-octadecenoic acid
}

def to_canonical(smiles: str) -> str | None:
    if not smiles:
        return None
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return Chem.MolToSmiles(mol, canonical=True, isomericSmiles=False)

def canonicalize_dict(d: dict[str, str]) -> dict[str, str | None]:
    return {name: to_canonical(s) for name, s in d.items()}

#Canonicalizo los SMILES del punto 1.b
punto_1_b = canonicalize_dict(punto_1_b)

# Uno todo
punto_1_a.update(punto_1_b)

#Si hay alguno que falló lo saco...
todas_canonicas = {k: v for k, v in punto_1_a.items() if v}

print("Canonical SMILES generadas:")
for k, v in todas_canonicas.items():
    print(f" - {k}: {v}")

resultados = analisis_completo(punto_1_a)

def resumen_subestructuras(res):
    filas = []
    for nombre, info in res.items():
        subest = info.get("subestructuras") or info.get("alerts") or info.get("pains")
        if isinstance(subest, (list, tuple, set)):
            subest_txt = "; ".join(map(str, subest)) if subest else ""
        else:
            subest_txt = str(subest) if subest is not None else ""
        filas.append({"molecula": nombre, "subestructuras_indeseables": subest_txt})
    return pd.DataFrame(filas)

df_sub = resumen_subestructuras(resultados)
print("\n=== Subestructuras indeseables detectadas ===")
print(df_sub.to_string(index=False))

#Exportar a CSV
df_sub.to_csv("punto3_subestructuras.csv", index=False)
print("\nArchivo generado: punto3_subestructuras.csv")
