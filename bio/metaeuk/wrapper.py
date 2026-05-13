"""Snakemake wrapper for MetaEuk."""

__author__ = "Rodolfo Brandão Dias Ferreira"
__copyright__ = "Copyright 2026, Rodolfo Brandão"
__email__ = "rodolfobrandao88@gmail.com"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

first_output = Path(snakemake.output[0])
outdir = first_output.parent
prefix = first_output.stem

out_prefix = outdir / prefix
tmp_dir = outdir / "tmp"

shell(
    "metaeuk easy-predict "
    "--threads {snakemake.threads} "
    "{extra} "
    "{snakemake.input.fasta} "
    "{snakemake.input.db} "
    "{out_prefix} "
    "{tmp_dir} "
    "{log}"
)