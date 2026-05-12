"""Snakemake wrapper for Prokka."""

__author__ = "Rodolfo Brandão Dias Ferreira"
__copyright__ = "Copyright 2026, Rodolfo Brandão"
__email__ = "rodolfobrandao88@gmail.com" 
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


proteins = snakemake.input.get("proteins", "")
proteins_cmd = f"--proteins {proteins}" if proteins else ""

kingdom = snakemake.params.get("kingdom", "")
kingdom_cmd = f"--kingdom {kingdom}" if kingdom else ""

genus = snakemake.params.get("genus", "")
genus_cmd = f"--genus {genus}" if genus else ""

species = snakemake.params.get("species", "")
species_cmd = f"--species {species}" if species else ""

first_output = Path(snakemake.output[0])
outdir = first_output.parent
prefix = first_output.stem

shell(
    "prokka "
    "--outdir {outdir} "
    "--prefix {prefix} "
    "--force "
    "{proteins_cmd} "
    "{kingdom_cmd} "
    "{genus_cmd} "
    "{species_cmd} "
    "{extra} "
    "{snakemake.input.fasta} "
    "{log}"
)