#!/usr/bin/env python3

from pathlib import Path
from bcc import BPF

bpf_source = Path('ebpf-probe.c').read_text()
bpf = BPF(text=bpf_source).trace_print()
