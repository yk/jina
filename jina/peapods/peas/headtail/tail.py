__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import argparse

from .. import BasePea
from ....logging import JinaLogger


class TailPea(BasePea):

    def __init__(self,
                 args: 'ArgNamespace',
                 **kwargs):
        super().__init__(args, **kwargs)
        self.name = self.__class__.__name__
        if self.args.name:
            self.name = self.args.name
            self.name = f'{self.name}-tail'
        self.logger = JinaLogger(self.name, **self.args.to_dict())

    def __str__(self):
        return self.name
