from GetAPIResults import EnsemblAPI
from GetTableGenes import out, df

if __name__ == "__main__":
    api = EnsemblAPI()
    ensembleIDs: list = []
    out = out.head(10)
    for target, specie in zip(out["TARGETS"], out["Specie"]):
        # print(target, specie)
        ensembleIDs.append(api.getEnsembleId(specie, target))
    df["EnsembleID"] = ensembleIDs

    print(df)
