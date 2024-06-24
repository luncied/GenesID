import polars as pl
import pandas as pd

# q1 = pl.scan_csv("./src/data/Systematic Review - Copia de UNIQUE.csv")
# out = q1.select(pl.col("*").exclude("Position", "DOI"))

df = pd.read_csv("./src/data/Systematic Review - Copia de UNIQUE.csv")
out = df[["TARGETS", "Specie"]]
