"""Snakemake wrapper for MetaEuk easy-predict."""

__author__ = "Rodolfo Brandão Dias Ferreira"
__copyright__ = "Copyright 2026, Rodolfo"
__license__ = "MIT"

from snakemake.shell import shell
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

out_prefix = snakemake.params.get("out_prefix", "metaeuk_results")
tmp_dir = snakemake.params.get("tmp_dir", "tmp_metaeuk")

os.makedirs(tmp_dir, exist_ok=True)

shell(
    "metaeuk easy-predict "
    "{snakemake.input.contigs:q} "
    "{snakemake.input.db:q} "
    "{out_prefix:q} "
    "{tmp_dir:q} "
    "--threads {snakemake.threads} "
    "{extra} "
    "{log}"
)