""" trigger/02000488_bf/01_mobspawn.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,111,112,113,114,115,116,121,122,123,124,125,126,201,202,203,204,205,206,207,211,212,213,214,215,216,221,222,223,224,225,226,301,302,303,304,305,306,307,311,312,313,314,315,316,321,322,323,324,325,326,401,402,403,404,405,406,407,408,411,412,413,414,415,416,421,422,423,424,425,426,501,502,503,504,505,506,507,508,509,511,512,513,514,515,516,521,522,523,524,525,526])
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012], visible=True, arg3=0, delay=0, scale=0) # DoorSide_AlwaysOn
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # IronDoor_StageEnter
        self.set_actor(triggerId=4001, visible=True, initialSequence='Closed') # IronDoor_Stage01
        self.set_actor(triggerId=4002, visible=True, initialSequence='Closed') # IronDoor_Stage02
        self.set_actor(triggerId=4003, visible=True, initialSequence='Closed') # IronDoor_Stage03
        self.set_actor(triggerId=4004, visible=True, initialSequence='Closed') # IronDoor_Stage04
        self.set_actor(triggerId=4005, visible=True, initialSequence='Closed') # IronDoor_Stage05
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # DoorBarrier_StageEnter
        # DoorBarrier_StairsBarrier_Stage01
        self.set_mesh(triggerIds=[3101,3110,3111], visible=True, arg3=0, delay=0, scale=0)
        # DoorBarrier_StairsBarrier_Stage02
        self.set_mesh(triggerIds=[3102,3120,3121], visible=True, arg3=0, delay=0, scale=0)
        # DoorBarrier_StairsBarrier_Stage03
        self.set_mesh(triggerIds=[3103,3130,3131], visible=True, arg3=0, delay=0, scale=0)
        # DoorBarrier_StairsBarrier_Stage04
        self.set_mesh(triggerIds=[3104,3140,3141], visible=True, arg3=0, delay=0, scale=0)
        # DoorBarrier_StairsBarrier_Stage05
        self.set_mesh(triggerIds=[3105,3150,3151], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5110,5111,5112,5113], visible=True, arg3=0, delay=0, scale=0) # BlueLight_Stage01
        self.set_mesh(triggerIds=[5210,5211,5212,5213], visible=True, arg3=0, delay=0, scale=0) # BlueLight_Stage02
        self.set_mesh(triggerIds=[5310,5311,5312,5313], visible=True, arg3=0, delay=0, scale=0) # BlueLight_Stage03
        self.set_mesh(triggerIds=[5410,5411,5412,5413], visible=True, arg3=0, delay=0, scale=0) # BlueLight_Stage04
        self.set_mesh(triggerIds=[5510,5511,5512,5513,5514,5515], visible=True, arg3=0, delay=0, scale=0) # BlueLight_Stage05
        self.set_mesh_animation(triggerIds=[5110,5111,5112,5113], visible=True, arg3=0, arg4=0) # BlueLight_Stage01
        self.set_mesh_animation(triggerIds=[5210,5211,5212,5213], visible=True, arg3=0, arg4=0) # BlueLight_Stage02
        self.set_mesh_animation(triggerIds=[5310,5311,5312,5313], visible=True, arg3=0, arg4=0) # BlueLight_Stage03
        self.set_mesh_animation(triggerIds=[5410,5411,5412,5413], visible=True, arg3=0, arg4=0) # BlueLight_Stage04
        self.set_mesh_animation(triggerIds=[5510,5511,5512,5513,5514,5515], visible=True, arg3=0, arg4=0) # BlueLight_Stage05
        self.set_agent(triggerIds=[8100,8101,8102,8103,8104,8105,8106,8107,8108], visible=True) # StageEnter
        self.set_agent(triggerIds=[8200,8201,8202,8203,8204,8205,8206,8207,8208,8209,8210,8211,8212], visible=True) # Stage01
        self.set_agent(triggerIds=[8300,8301,8302,8303,8304,8305,8306,8307,8308,8309,8310,8311,8312], visible=True) # Stage02
        self.set_agent(triggerIds=[8400,8401,8402,8403,8404,8405,8406,8407,8408,8409,8410,8411,8412], visible=True) # Stage03
        self.set_agent(triggerIds=[8500,8501,8502,8503,8504,8505,8506,8507,8508,8509,8510,8511,8512], visible=True) # Stage04
        self.set_agent(triggerIds=[8600,8601,8602,8603,8604,8605,8606,8607,8608,8609,8610,8611,8612], visible=True) # Stage05
        # Sound_IronDoorOpen_StageEnter
        self.set_effect(triggerIds=[5001], visible=False)
        # Sound_IronDoorOpen_IceMelt_Stage01
        self.set_effect(triggerIds=[5002,5100,5101], visible=False)
        # Sound_IronDoorOpen_IceMelt_Stage02
        self.set_effect(triggerIds=[5003,5200,5201], visible=False)
        # Sound_IronDoorOpen_IceMelt_Stage03
        self.set_effect(triggerIds=[5004,5300,5301], visible=False)
        # Sound_IronDoorOpen_IceMelt_Stage04
        self.set_effect(triggerIds=[5005,5400,5401], visible=False)
        # Sound_IronDoorOpen_IceMelt_Stage05
        self.set_effect(triggerIds=[5006,5500,5501], visible=False)
        self.set_effect(triggerIds=[5007,5008,5009], visible=False) # Sound_PortalOn

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return StageEnter(self.ctx)


class StageEnter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=True, initialSequence='Opened') # IronDoor_StageEnter
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=0) # DoorBarrier_StageEnter
        # Sound_IronDoorOpen_StageEnter
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Stage01MobSpawn(self.ctx)


class Stage01MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103,104,105,106,111,112,113,114,115,116,121,122,123,124,125,126], animationEffect=False)
        self.set_agent(triggerIds=[8100,8101,8102,8103,8104,8105,8106,8107,8108], visible=False) # Stage01

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106,111,112,113,114,115,116,121,122,123,124,125,126]):
            return Stage01DoorOpen(self.ctx)


class Stage01DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4001, visible=True, initialSequence='Opened') # IronDoor_Stage01
        # DoorBarrier_StairsBarrier_Stage01
        self.set_mesh(triggerIds=[3101,3110,3111], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5110,5111,5112,5113], visible=False, arg3=500, delay=0, scale=5) # BlueLight_Stage01
        self.set_mesh_animation(triggerIds=[5110,5111,5112,5113], visible=False, arg3=0, arg4=0) # BlueLight_Stage01
        # Sound_IronDoorOpen_IceMelt_Stage01
        self.set_effect(triggerIds=[5002,5100,5101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Stage02MobSpawn(self.ctx)


class Stage02MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201,202,203,204,205,206,207,211,212,213,214,215,216,221,222,223,224,225,226], animationEffect=False)
        self.set_agent(triggerIds=[8200,8201,8202,8203,8204,8205,8206,8207,8208,8209,8210,8211,8212], visible=False) # Stage02

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206,207,211,212,213,214,215,216,221,222,223,224,225,226]):
            return Stage02DoorOpen(self.ctx)


class Stage02DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened') # IronDoor_Stage02
        # DoorBarrier_StairsBarrier_Stage02
        self.set_mesh(triggerIds=[3102,3120,3121], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5210,5211,5212,5213], visible=False, arg3=500, delay=0, scale=5) # BlueLight_Stage02
        self.set_mesh_animation(triggerIds=[5210,5211,5212,5213], visible=False, arg3=0, arg4=0) # BlueLight_Stage02
        # Sound_IronDoorOpen_IceMelt_Stage02
        self.set_effect(triggerIds=[5003,5200,5201], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Stage03MobSpawn(self.ctx)


class Stage03MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[301,302,303,304,305,306,307,311,312,313,314,315,316,321,322,323,324,325,326], animationEffect=False)
        self.set_agent(triggerIds=[8300,8301,8302,8303,8304,8305,8306,8307,8308,8309,8310,8311,8312], visible=False) # Stage03

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[301,302,303,304,305,306,307,311,312,313,314,315,316,321,322,323,324,325,326]):
            return Stage03DoorOpen(self.ctx)


class Stage03DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4003, visible=True, initialSequence='Opened') # IronDoor_Stage03
        # DoorBarrier_StairsBarrier_Stage03
        self.set_mesh(triggerIds=[3103,3130,3131], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5310,5311,5312,5313], visible=False, arg3=500, delay=0, scale=5) # BlueLight_Stage03
        self.set_mesh_animation(triggerIds=[5310,5311,5312,5313], visible=False, arg3=0, arg4=0) # BlueLight_Stage03
        # Sound_IronDoorOpen_IceMelt_Stage03
        self.set_effect(triggerIds=[5004,5300,5301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Stage04MobSpawn(self.ctx)


class Stage04MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[401,402,403,404,405,406,407,408,411,412,413,414,415,416,421,422,423,424,425,426], animationEffect=False)
        self.set_agent(triggerIds=[8400,8401,8402,8403,8404,8405,8406,8407,8408,8409,8410,8411,8412], visible=False) # Stage04

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[401,402,403,404,405,406,407,408,411,412,413,414,415,416,421,422,423,424,425,426]):
            return Stage04DoorOpen(self.ctx)


class Stage04DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4004, visible=True, initialSequence='Opened') # IronDoor_Stage04
        # DoorBarrier_StairsBarrier_Stage04
        self.set_mesh(triggerIds=[3104,3140,3141], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5410,5411,5412,5413], visible=False, arg3=500, delay=0, scale=5) # BlueLight_Stage04
        self.set_mesh_animation(triggerIds=[5410,5411,5412,5413], visible=False, arg3=0, arg4=0) # BlueLight_Stage04
        # Sound_IronDoorOpen_IceMelt_Stage04
        self.set_effect(triggerIds=[5005,5400,5401], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Stage05MobSpawn(self.ctx)


class Stage05MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[501,502,503,504,505,506,507,508,509,511,512,513,514,515,516,521,522,523,524,525,526], animationEffect=False)
        self.set_agent(triggerIds=[8500,8501,8502,8503,8504,8505,8506,8507,8508,8509,8510,8511,8512], visible=False) # Stage05

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501,502,503,504,505,506,507,508,509,511,512,513,514,515,516,521,522,523,524,525,526]):
            return Stage05DoorOpen(self.ctx)


class Stage05DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4005, visible=True, initialSequence='Opened') # IronDoor_Stage05
        # DoorBarrier_StairsBarrier_Stage05
        self.set_mesh(triggerIds=[3105,3150,3151], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5510,5511,5512,5513,5514,5515], visible=False, arg3=500, delay=0, scale=5) # BlueLight_Stage05
        self.set_mesh_animation(triggerIds=[5510,5511,5512,5513,5514,5515], visible=False, arg3=0, arg4=0) # BlueLight_Stage05
        # Sound_IronDoorOpen_IceMelt_Stage05
        self.set_effect(triggerIds=[5006,5500,5501], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BossStagePortalOpen(self.ctx)


class BossStagePortalOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8600,8601,8602,8603,8604,8605,8606,8607,8608,8609,8610,8611,8612], visible=False) # Stage06
        self.set_effect(triggerIds=[5007,5008,5009], visible=True) # Sound_PortalOn
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=False)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=False)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=False)


initial_state = Setting
