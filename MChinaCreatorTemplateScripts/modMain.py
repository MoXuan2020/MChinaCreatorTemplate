# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

from mod.common.mod import Mod

from .config import modConfig

@Mod.Binding(modConfig.ModName, modConfig.ModVersion)
class MChinaCreatorTemplateMod(object):
    
    @Mod.InitServer()
    def InitMChinaCreatorTemplateServerSystem(self):
        serverApi.RegisterSystem()
    
    @Mod.InitClient()
    def InitMChinaCreatorTemplateClientSystem(self):
        clientApi.RegisterSystem()
