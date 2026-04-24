"""Snakemake wrapper for Prokka."""

__author__ = "Rodolfo Brandão" 
__copyright__ = "Copyright 2026, Rodolfo"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

prefix = snakemake.params.get("prefix", "prokka_results")

shell(
    "prokka "
    " --cpus {snakemake.threads} "
    " --outdir {snakemake.output.outdir:q} "
    " --prefix {prefix:q} "
    " {extra} "
    " {snakemake.input.fasta:q} "
    " {log}"
)