__author__ = "Rodolfo Brandão"
__copyright__ = "Copyright 2026, Rodolfo Brandão"
__email__ = "teu_email@uminho.pt"
__license__ = "MIT"

from snakemake.shell import shell
import os

# Argumentos extra (ex: --cpus)
extra = snakemake.params.get("extra", "")

# Extrair prefixo (opcional)
prefix = snakemake.params.get("prefix", "prokka_out")

# O Prokka exige que o diretório de saída não exista previamente, ou falhará.
# No entanto, o Snakemake costuma criar as pastas antes da regra correr.
# Para evitar o erro do Prokka "Output directory already exists", apagamos a pasta se ela estiver vazia,
# ou forçamos o Prokka a sobrescrever (--force). O --force é mais seguro.
force_flag = "--force"

shell(
    "prokka "
    "{extra} "
    "{force_flag} "
    "--outdir {snakemake.output[0]} "
    "--prefix {prefix} "
    "{snakemake.input[0]} "
    ">{snakemake.log} 2>&1"
)