import sys


def input_validate(args: list[str]) -> tuple[str, int, int]:
    if (
        len(args) == 4
        and args[1] in ("auto-pagination", "no-auto-pagination")
        and args[2].isnumeric()
        and args[3].isnumeric()
    ):
        return args[1] == "auto-pagination", int(args[2]), int(args[3])
    sys.exit(
        "Se requiere pasar como argumentos la <auto-pagination|no-auto-pagination>, <querys: int> y <MaxWorkers: int>, en ese mismo orden."
    )
