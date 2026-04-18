from __future__ import annotations

import argparse
import ast
import contextlib
from collections.abc import Generator
from collections.abc import Sequence
from typing import Any

AST: tuple[type[Any], ...] = (ast.AST,)
expr_context: tuple[type[Any], ...] = (ast.expr_context,)


def _is_sub_node(node: object) -> bool:
    pass


def _is_leaf(node: ast.AST) -> bool:
    pass


def _fields(n: ast.AST, show_offsets: bool = True) -> tuple[str, ...]:
    pass


def _leaf(node: ast.AST, show_offsets: bool = True) -> str:
    pass


def pformat(
        node: ast.AST | None | str,
        indent: str | int = '    ',
        show_offsets: bool = True,
        _indent: int = 0,
) -> str:
    pass


def pprint(*args: Any, **kwargs: Any) -> None:
    pass


def main(argv: Sequence[str] | None = None) -> int:
    pass


if __name__ == '__main__':
    raise SystemExit(main())
