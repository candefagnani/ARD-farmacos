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

# === Llamo al análisis ===
resultados = analisis_completo(punto_1_a)

# === FUNCIÓN FINAL ===
def resumen_subestructuras(res):
    sub_map = {}

    # Extraer PAINS
    if "pains" in res and isinstance(res["pains"], pd.DataFrame):
        pains_df = res["pains"]
        for _, row in pains_df.iterrows():
            nombre = row["Name"]
            alerts = row.get("PAINS_Alerts", 0)
            details = row.get("PAINS_Details", [])
            if alerts and alerts > 0:
                if isinstance(details, list):
                    details_txt = "; ".join(details)
                else:
                    details_txt = str(details)
                sub_map.setdefault(nombre, []).append(details_txt)

    # Extraer Toxicidad
    if "toxicidad" in res and isinstance(res["toxicidad"], pd.DataFrame):
        tox_df = res["toxicidad"]
        for _, row in tox_df.iterrows():
            nombre = row["Name"]
            alerts = row.get("Toxicity_Alerts", 0)
            if alerts and alerts > 0:
                sub_map.setdefault(nombre, []).append(f"{alerts} toxicidad")

    # Construyo filas finales
    filas = []
    for nombre in res["propiedades"]["Name"]:  # asegurar mismo orden que entrada
        detalles = "; ".join(sub_map.get(nombre, []))
        filas.append({
            "molecula": nombre,
            "subestructuras_indeseables": detalles
        })

    return pd.DataFrame(filas)


# === Genero el DataFrame ===
df_sub = resumen_subestructuras(resultados)
print("\n=== Subestructuras indeseables detectadas ===")
print(df_sub.to_string(index=False))

#Exportar a CSV
df_sub.to_csv("punto3_subestructuras.csv", index=False)
print("\nArchivo generado: punto3_subestructuras.csv")
