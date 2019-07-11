#!/usr/bin/env python3

# a buffer
# --------
# 01234567
# 
# XXXa buffer
# -----------
# 01234567890
#
# aXXX buffer
# -----------
# 01234567890
#

class GapBuffer(object):
    def __init__(self, string, cursor_pos):
        string_len = len(string)
        self.gap_len = 2
        self.cursor_pos = min(cursor_pos, string_len + 1)
        self.list = [None] * (string_len + self.gap_len)
        self.size = len(self.list)
        for i in range(len(self.list)):
            if i < cursor_pos:
                self.list[i] = string[i]
            elif i >= cursor_pos + self.gap_len:
                target = i - self.gap_len
                self.list[i] = string[target]

    
    def move_cursor(self, amount):
        new_pos = self.cursor_pos + amount
        if new_pos + self.gap_len > self.size or new_pos < 0:
            return

        if amount > 0:
            # save the char to be overwritten
            for i in range(self.cursor_pos + self.gap_len + amount - 1, self.cursor_pos, -1):
                print(i)
                # swap chars
                tmp = self.list[i]
                self.list[i] = self.list[i-1]
                self.list[i-1] = tmp
        else:
            for i in range(self.cursor_pos, self.cursor_pos + self.gap_len + amount + 1):
                print(i)
                tmp = self.list[i-1]
                self.list[i-1] = self.list[i]
                self.list[i] = tmp


    def insert(self, string):
        pass

    def remove(self, amount):
        pass

    def print(self):
        print(self.list)


if __name__ == "__main__":
    buf = GapBuffer("a buffer", 0)
    buf.print()
    buf.move_cursor(2)
    buf.print()
