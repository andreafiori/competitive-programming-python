"""
Problem 79: Passcode Derivation | https://projecteuler.net/problem-79

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.
"""

import itertools

from pathlib import Path

class PasscodeDerivation:

    def find_secret_passcode(self, logins: list[str]) -> int:
        """
        Returns the shortest possible secret passcode of unknown length.

        >>> PasscodeDerivation().find_secret_passcode(["135", "259", "235", "189", "690", "168", "120",
        ...     "136", "289", "589", "160", "165", "580", "369", "250", "280"])
        12365890

        >>> PasscodeDerivation().find_secret_passcode(["426", "281", "061", "819", "268", "406", "420",
        ...     "428", "209", "689", "019", "421", "469", "261", "681", "201"])
        4206819
        """

        # Split each login by character e.g. '319' -> ('3', '1', '9')
        split_logins = [tuple(login) for login in logins]

        unique_chars = {char for login in split_logins for char in login}

        for permutation in itertools.permutations(unique_chars):
            satisfied = True
            for login in logins:
                if not (
                    permutation.index(login[0])
                    < permutation.index(login[1])
                    < permutation.index(login[2])
                ):
                    satisfied = False
                    break

            if satisfied:
                return int("".join(permutation))

        raise Exception("Unable to find the secret passcode")


    def solution(self, input_file: str = "keylog.txt") -> int:
        """
        Returns the shortest possible secret passcode of unknown length
        for successful login attempts given by `input_file` text file.

        >>> PasscodeDerivation().solution("keylog_test.txt")
        6312980
        """
        logins = Path(__file__).parent.joinpath(input_file).read_text().splitlines()

        return self.find_secret_passcode(logins)
