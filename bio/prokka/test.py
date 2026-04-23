import subprocess
import os
from pathlib import Path

def test_prokka_wrapper():
    
    test_path = Path(__file__).parent / "test"

    command = [
        "snakemake",
        "--snakefile", str(test_path / "Snakefile"),
        "--directory", str(test_path),
        "--use-conda",
        "--cores", "1",
        "output"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Teste concluído com sucesso!")
        
        output_file = test_path / "output" / "resultado_final.gff"
        if output_file.exists():
            print(f"Verificação de ficheiro: {output_file} encontrado.")
        else:
            print("Erro: Ficheiro de output não encontrado.")
            
    except subprocess.CalledProcessError as e:
        print(f"O teste falhou com o erro:\n{e.stderr}")
        raise e

if __name__ == "__main__":
    test_prokka_wrapper()