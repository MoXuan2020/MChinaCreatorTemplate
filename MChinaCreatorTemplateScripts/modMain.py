# -*- coding: utf-8 -*-

from mod.common.mod import Mod

from .config import modConfig

@Mod.Binding(modConfig.ModName, modConfig.ModVersion)
class MChinaCreatorTemplateMod(object):
    pass
