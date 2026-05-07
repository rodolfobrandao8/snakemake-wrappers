"""Snakemake wrapper for Prokka."""

__author__ = "Rodolfo Brandão" 
__copyright__ = "Copyright 2026, Rodolfo"
__email__ = "rodolfobrandao88@gmail.com"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

first_output = Path(snakemake.output[0])
outdir = first_output.parent
prefix = first_output.stem

proteins = snakemake.input.get("proteins", "")
proteins_cmd = f"--proteins {proteins}" if proteins else ""

shell(
    "prokka "
    "{extra} "
    "--outdir {outdir} "
    "--prefix {prefix} "
    "--force "
    "{proteins_cmd} "
    "{snakemake.input.fasta} "
    "{log}"
)