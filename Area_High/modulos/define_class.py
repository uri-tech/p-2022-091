# -*- coding: utf-8 -*-
"""."""
try:
    from enum import Enum, auto
except Exception as ex:
    print("ERROR in the import section")
    raise Exception(f"ERROR\n{ex}")


class Tracks(Enum):
    try:
        ONE: int = 0
        TWO: int = 1
        THREE: int = 2
        Time_Intervel: int = 2_000
        Size_Two: int = 37
        Sleep_Time: int = 1
        INDEX_EQUAL: int = 16  # its not incloding the ''
    except Exception as ex:
        print(f"ERROR:\n{ex}")

    def __repr__(self) -> str:
        """[summary].

        Returns:
            str: [description]

        """
        try:
            return f"{self.__class__.__name__}()"
        except Exception as ex:
            print(f"ERROR:\n{ex}")


class PhoneEnum(Enum):
    try:
        DEFAULT_SIZE: int = 10
        MAX_SIZE: int = 14
        START_INDEX: int = 2
        START: str = '05'
        START2_INDEX: int = 4
        START2: str = '9725'
        START3_INDEX: int = 5
        START3: str = '+9725'
    except Exception as ex:
        print(f"ERROR:\n{ex}")

    def __repr__(self) -> str:
        """[summary].

        Returns:
            str: [description]

        """
        try:
            return f"{self.__class__.__name__}()"
        except Exception as ex:
            print(f"ERROR:\n{ex}")
