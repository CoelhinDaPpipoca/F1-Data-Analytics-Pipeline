import subprocess
import time

print("\n===================")
print("PIPELINE F1")
print("===================\n")

etapas = [

"src/ingestion/ingest.py",

"src/transformation/transform.py",

"src/transformation/gold.py"

]

for etapa in etapas:

    print(
        f"\nExecutando {etapa}"
    )

    resultado = subprocess.run(

        ["python", etapa],

        capture_output=True,

        text=True

    )

    print(
        resultado.stdout
    )

    if resultado.returncode != 0:

        print(
            resultado.stderr
        )

        break

    time.sleep(1)

print(
"\nPIPELINE FINALIZADO"
)