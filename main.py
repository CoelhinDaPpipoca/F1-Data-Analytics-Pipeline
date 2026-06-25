import subprocess
import time
from datetime import datetime

print("\n==============================")
print("🏎️ F1 DATA ANALYTICS PIPELINE")
print("==============================\n")

inicio = time.time()

etapas = [

"src/ingestion/ingest.py",

"src/transformation/transform.py",

"src/transformation/gold.py"

]

log = "logs/pipeline.log"

with open(
log,
"a",
encoding="utf-8"
) as f:

    f.write("\n")
    f.write("="*40 + "\n")
    f.write(
        f"Execução: {datetime.now()}\n"
    )

for etapa in etapas:

    print(
        f"\nExecutando → {etapa}"
    )

    resultado = subprocess.run(

        ["python", etapa],

        capture_output=True,

        text=True

    )

    print(
        resultado.stdout
    )

    with open(
        log,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"\nETAPA: {etapa}\n"
        )

        f.write(
            resultado.stdout
        )

    if resultado.returncode != 0:

        print(
            "❌ Falha detectada"
        )

        with open(
            log,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                resultado.stderr
            )

        break

tempo = round(
time.time()-inicio,
2
)

with open(
log,
"a",
encoding="utf-8"
) as f:

    f.write(
        f"\nTempo total: {tempo}s\n"
    )

print("\n==============================")
print("✅ PIPELINE FINALIZADO")
print(f"⏱ Tempo: {tempo}s")
print("📄 Logs gerados")
print("==============================")