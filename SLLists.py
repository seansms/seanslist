import logging

from SLFiler import SLFiler
from SLFrameOver import SLFrameOver


class SLLists:

    def __init__(self):
        self.frame = None

    def get_combos_from_lists(self, my_lists):
        c = []
        for list1 in my_lists:
            c.append(list1[1])
        return c

    def engage(self):
        # import lists
        filer = SLFiler()
        filer.main_dict = filer.get_main_dict()

        k = filer.main_dict["all_list_names"]
        my_combos = [k, k, k, k]
        my_displayed_list_names = filer.main_dict["My Lists"]

        # my_combos = filer.get_my_lists(SLControl.my_combos_filename, SLControl.my_combos_version)

        if __debug__:
            logging.info(filer.main_dict)

        self.frame = SLFrameOver(None)
        self.frame.filer = filer
        self.frame.hydrate_lists(filer.main_dict, my_displayed_list_names)
        self.frame.hydrate_combos(my_combos)
        self.frame.hydrate_statics(my_displayed_list_names)

        self.frame.Show(True)

