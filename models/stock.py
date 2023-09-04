from dataclasses import dataclass, field
from typing import List


@dataclass
class Stock:
    symbol: str = ""
    fk: float = 0.0
    indfk: float = 0.0
    pddd: float = 0.0
    indpddd: float = 0.0
    ebitda_margin: float = 0.0
    ind_ebitda_margin: float = 0.0
    dates: List[int] = field(default_factory=list)
    current_assets: List[int] = field(default_factory=list)
    fixed_assets: List[int] = field(default_factory=list)
    total_assets: List[int] = field(default_factory=list)
    short_term_debts: List[int] = field(default_factory=list)
    long_term_debts: List[int] = field(default_factory=list)
    total_debts: List[int] = field(default_factory=list)
    total_equities: List[int] = field(default_factory=list)
    total_revenues: List[int] = field(default_factory=list)
    gross_profits: List[int] = field(default_factory=list)
    operating_incomes: List[int] = field(default_factory=list)
    net_profits: List[int] = field(default_factory=list)
