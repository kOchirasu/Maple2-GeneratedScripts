""" trigger/02000396_bf/03_ladder.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[501], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[502], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[503], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[504], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[505], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_interact_object(triggerIds=[10001128], state=0, arg4=False) # LeverForLadder
        self.set_user_value(key='EnableLadder', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EnableLadder', value=1):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001128], state=1) # LeverForLadder

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001128], stateValue=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[501], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[502], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[503], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[504], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[505], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[601,600], returnView=True)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return FirstBattle(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_ladder(triggerIds=[510], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True) # LadderEnterance
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0) # Invisible_Barrier


class FirstBattle(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=3, key='CameraWalkEnd', value=1)
        self.create_monster(spawnIds=[901,902,903], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001043], stateValue=0):
            return FirstBridgeOn(self.ctx)


class FirstBridgeOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.destroy_monster(spawnIds=[901,902,903])
        self.set_mesh(triggerIds=[3110], visible=False, arg3=0, delay=0, scale=0) # 1stBridgeBarrier
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=True, arg3=0, delay=100, scale=10) # 1stBridge
        self.set_user_value(triggerId=101, key='BridgeOpen', value=1)
        self.set_user_value(triggerId=102, key='BridgeOpen', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[504]):
            return SecondBattle(self.ctx)


class SecondBattle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[904,905,906], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001044], stateValue=0):
            return SecondBridgeOn(self.ctx)


class SecondBridgeOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.destroy_monster(spawnIds=[904,905,906])
        self.set_mesh(triggerIds=[3210], visible=False, arg3=0, delay=0, scale=0) # 2ndBridgeBarrier
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=True, arg3=0, delay=100, scale=10) # 2ndBridge
        self.set_user_value(triggerId=101, key='BridgeOpen', value=2)
        self.set_user_value(triggerId=102, key='BridgeOpen', value=2)
        self.set_user_value(triggerId=103, key='BridgeOpen', value=2)
        self.set_user_value(triggerId=104, key='BridgeOpen', value=2)
        self.set_user_value(triggerId=105, key='BridgeOpen', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[507]):
            return ThirdBattle(self.ctx)


class ThirdBattle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[907,908,909], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001035], stateValue=0):
            return ThirdBridgeOn(self.ctx)


class ThirdBridgeOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.destroy_monster(spawnIds=[907,908,909])
        self.set_mesh(triggerIds=[3310], visible=False, arg3=0, delay=0, scale=0) # 3rdBridgeBarrier
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309], visible=True, arg3=0, delay=100, scale=10) # 3rdBridge
        self.set_user_value(triggerId=101, key='BridgeOpen', value=3)
        self.set_user_value(triggerId=102, key='BridgeOpen', value=3)
        self.set_user_value(triggerId=103, key='BridgeOpen', value=3)
        self.set_user_value(triggerId=104, key='BridgeOpen', value=3)
        self.set_user_value(triggerId=105, key='BridgeOpen', value=3)
        self.set_user_value(triggerId=106, key='BridgeOpen', value=3)
        self.set_user_value(triggerId=107, key='BridgeOpen', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[402]):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return Success(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[99])


class Success(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = Setting
