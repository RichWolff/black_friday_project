# -*- coding: utf-8 -*-
import os
from os.path import join
ROOT = os.path.dirname(__file__)
DATA = join(ROOT,'data')
DB = join(DATA,'blackFriday.sqlite')
db_engine = 'sqlite:///' + DB