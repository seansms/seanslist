#    Sean's SuperList - A to-do and general list manager.
#    Copyright (C) 2020  Sean Shannon
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import logging

from SLFiler import SLFiler
from SLFrameOver import SLFrameOver
from SLControl import SLControl


class SLLists:

    def __init__(self):
        self.frame = None
        self.wizard = None

    def get_combos_from_lists(self, my_lists):
        c = []
        for list1 in my_lists:
            c.append(list1[1])
        return c

    def engage(self):
        # import lists
        filer = SLFiler()

        filer.main_dict = filer.get_main_dict(SLControl.my_lists_filename, SLControl.my_lists_version, SLControl.AllList)

        k = filer.main_dict[SLControl.AllList]
        my_combos = [k, k, k, k]
        my_displayed_list_names = filer.main_dict["My Lists"]

        # my_combos = filer.get_my_lists(SLControl.my_combos_filename, SLControl.my_combos_version)

        self.frame = SLFrameOver(None)
        self.frame.filer = filer
        self.frame.hydrate_lists(filer.main_dict, my_displayed_list_names)
        self.frame.hydrate_combos(my_combos, my_displayed_list_names)
        self.frame.hydrate_statics(my_displayed_list_names)

        self.frame.Show(True)

