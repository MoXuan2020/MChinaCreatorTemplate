# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

from mod.common.mod import Mod

from .config import modConfig

@Mod.Binding(modConfig.ModName, modConfig.ModVersion)
class MChinaCreatorTemplateMod(object):
    """
    组件启动主类
    """
    
    @Mod.InitServer()
    def InitMChinaCreatorTemplateServerSystem(self):
        # 注册服务端
        serverApi.RegisterSystem()
    
    @Mod.InitClient()
    def InitMChinaCreatorTemplateClientSystem(self):
        # 注册客户端
        clientApi.RegisterSystem()
