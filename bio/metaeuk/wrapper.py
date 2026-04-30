"""Snakemake wrapper for MetaEuk easy-predict."""

__author__ = "Rodolfo Brandão Dias Ferreira"
__copyright__ = "Copyright 2026, Rodolfo Brandão"
__email__ = "rodolfobrandão88@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

first_output = snakemake.output[0]
outdir = os.path.dirname(first_output)
prefix = os.path.splitext(os.path.basename(first_output))[0]

out_prefix = os.path.join(outdir, prefix)

tmp_dir = os.path.join(outdir, "tmp")

shell(
    "metaeuk easy-predict "
    "{extra} "
    "{snakemake.input.fasta} "
    "{snakemake.input.db} "
    "{out_prefix} "
    "{tmp_dir} "
    "{log}"
)