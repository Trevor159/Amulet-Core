from __future__ import annotations

import numpy

from amulet.world_interface.chunk.translators.bedrock import BaseBedrockTranslator
from amulet.api.block import Block

from PyMCTranslate.py3.translation_manager import Version


class BedrockNumericalTranslator(BaseBedrockTranslator):
    @staticmethod
    def is_valid(key):
        if key[0] != "bedrock":
            return False
        if not key[1] < (1, 2, 13):
            return False
        return True

    def _pack_palette(self, version: Version, palette: numpy.ndarray) -> numpy.ndarray:
        """
        Packs a numpy array of Block objects into an object array of containing block ids and block data values.
        :param version:
        :param palette:
        :return:
        """
        palette_ = numpy.empty(len(palette), dtype=object)
        for palette_index, entry in enumerate(palette):
            entry: Block
            block_tuple = version.block_to_ints(entry)
            if block_tuple is None:
                block_tuple = (0, 0)  # TODO: find some way for the user to specify this
            palette_[palette_index] = ((None, block_tuple),)

        return palette_


TRANSLATOR_CLASS = BedrockNumericalTranslator
