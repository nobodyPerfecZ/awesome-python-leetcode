from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs
        on the bottom to represent the minutes (0-59). Each LED represents a zero or
        one, with the least significant bit on the right.
        - For example, the below binary watch reads "4:51".

        Given an integer turnedOn which represents the number of LEDs that are currently
        on (ignoring the PM), return all possible times the watch could represent. You
        may return the answer in any order.

        The hour must not contain a leading zero.
        - For example, "01:00" is not valid. It should be "1:00".

        The minute must consist of two digits and may contain a leading zero.
        - For example, "10:2" is not valid. It should be "10:02".
        """
        if 0 < turnedOn >= 9:
            return []

        queue = [(0, 0, 0, {8, 4, 2, 1}, {32, 16, 8, 4, 2, 1})]
        visited = set()
        result = []
        while queue:
            # Get data from queue
            (
                cur_hour,
                cur_minutes,
                cur_turnedOn,
                cur_hour_missing,
                cur_minutes_missing,
            ) = queue.pop()

            # Check if goal state is reached
            if turnedOn == cur_turnedOn:
                result.append((cur_hour, cur_minutes))
                continue

            # Iterate over all valid hour options
            for hour in cur_hour_missing:
                # Next state
                next_hour = cur_hour + hour
                next_minutes = cur_minutes
                next_turnedOn = cur_turnedOn + 1
                next_hour_missing = cur_hour_missing - {hour}
                next_minutes_missing = cur_minutes_missing

                # Check if next time is valid and is not visited before
                if next_hour <= 11 and (next_hour, next_minutes) not in visited:
                    visited.add((next_hour, next_minutes))
                    queue.append(
                        (
                            next_hour,
                            next_minutes,
                            next_turnedOn,
                            next_hour_missing,
                            next_minutes_missing,
                        )
                    )

            # Iterate over all valid minutes options
            for minutes in cur_minutes_missing:
                # Next state
                next_hour = cur_hour
                next_minutes = cur_minutes + minutes
                next_turnedOn = cur_turnedOn + 1
                next_hour_missing = cur_hour_missing
                next_minutes_missing = cur_minutes_missing - {minutes}

                # Check if next time is valid and is not visited before
                if next_minutes <= 59 and (next_hour, next_minutes) not in visited:
                    visited.add((next_hour, next_minutes))
                    queue.append(
                        (
                            next_hour,
                            next_minutes,
                            next_turnedOn,
                            next_hour_missing,
                            next_minutes_missing,
                        )
                    )
        return list(map(lambda item: f"{item[0]}:{item[1]:02d}", result))
