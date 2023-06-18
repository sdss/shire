# encoding: utf-8

import os
import asyncio
from functools import partial

from sdsstools import get_config, get_logger, get_package_version

# pip package name
NAME = 'sdss5-shire'

# Loads config. config name is the package name.
config = get_config('sdss5-shire')

# Inits the logging system as NAME. Only shell logging, and exception and warning catching.
# File logging can be started by calling log.start_file_logger(path).  Filename can be different
# than NAME.
log = get_logger(NAME)


# package name should be pip package name
__version__ = get_package_version(path=__file__, package_name=NAME)


observatory = os.getenv("OBSERVATORY")


async def wrapBlocking(func, *args, **kwargs):
    loop = asyncio.get_event_loop()

    wrapped = partial(func, *args, **kwargs)

    return await loop.run_in_executor(None, wrapped)
