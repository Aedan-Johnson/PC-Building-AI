"""Rule based compatibility checker. Owner: Aedan.

Every AI answer passes through check_build() before the user sees it.
Each rule returns a list of problem strings. Empty list means the rule passed.

A `build` is a dict of part names, e.g.:
    {"cpu": "Ryzen 5 7600", "motherboard": "...", "ram": "...",
     "gpu": "...", "case": "...", "psu": "...", "storage": "..."}
"""

PSU_HEADROOM = 1.3


def check_socket(build, parts) -> list[str]:
    """Rule 1: CPU socket matches the motherboard."""
    raise NotImplementedError


def check_ram_type(build, parts) -> list[str]:
    """Rule 2: RAM type matches the motherboard."""
    raise NotImplementedError


def check_motherboard_fits_case(build, parts) -> list[str]:
    """Rule 3: Motherboard form factor is supported by the case."""
    raise NotImplementedError


def check_gpu_fits_case(build, parts) -> list[str]:
    """Rule 4: GPU length <= case max GPU length."""
    raise NotImplementedError


def check_psu_wattage(build, parts) -> list[str]:
    """Rule 5: PSU watts >= (CPU TDP + GPU TDP) * PSU_HEADROOM."""
    raise NotImplementedError


def check_budget(build, parts, budget: float) -> list[str]:
    """Rule 6: Total price is within budget."""
    raise NotImplementedError


def check_parts_exist(build, parts) -> list[str]:
    """Rule 7: Every part named in the build exists in the spreadsheet."""
    raise NotImplementedError


def check_build(build, parts, budget: float | None = None) -> list[str]:
    """Run every rule. Returns all problems found (empty list = valid build).

    Rule 7 runs first: if a part doesn't exist, the other rules can't look it up.
    """
    problems = check_parts_exist(build, parts)
    if problems:
        return problems
    for rule in (check_socket, check_ram_type, check_motherboard_fits_case,
                 check_gpu_fits_case, check_psu_wattage):
        problems += rule(build, parts)
    if budget is not None:
        problems += check_budget(build, parts, budget)
    return problems
