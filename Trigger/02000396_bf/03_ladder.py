""" trigger/02000396_bf/03_ladder.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[501], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[502], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[503], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[504], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[505], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_interact_object(triggerIds=[10001128], state=0, arg4=False) # LeverForLadder
        set_user_value(key='EnableLadder', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='EnableLadder', value=1):
            return LeverOn()


class LeverOn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001128], state=1) # LeverForLadder

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001128], arg2=0):
            return LadderOn()


class LadderOn(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[501], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[502], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[503], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[504], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[505], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut


class CameraWalk01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[601,600], returnView=True)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FirstBattle()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_ladder(triggerIds=[510], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[511], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[512], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[513], visible=True, animationEffect=True) # LadderEnterance
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_Barrier


class FirstBattle(state.State):
    def on_enter(self):
        set_user_value(triggerId=3, key='CameraWalkEnd', value=1)
        create_monster(spawnIds=[901,902,903], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001043], arg2=0):
            return FirstBridgeOn()


class FirstBridgeOn(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        destroy_monster(spawnIds=[901,902,903])
        set_mesh(triggerIds=[3110], visible=False, arg3=0, arg4=0, arg5=0) # 1stBridgeBarrier
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=True, arg3=0, arg4=100, arg5=10) # 1stBridge
        set_user_value(triggerId=101, key='BridgeOpen', value=1)
        set_user_value(triggerId=102, key='BridgeOpen', value=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[504]):
            return SecondBattle()


class SecondBattle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[904,905,906], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001044], arg2=0):
            return SecondBridgeOn()


class SecondBridgeOn(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        destroy_monster(spawnIds=[904,905,906])
        set_mesh(triggerIds=[3210], visible=False, arg3=0, arg4=0, arg5=0) # 2ndBridgeBarrier
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=True, arg3=0, arg4=100, arg5=10) # 2ndBridge
        set_user_value(triggerId=101, key='BridgeOpen', value=2)
        set_user_value(triggerId=102, key='BridgeOpen', value=2)
        set_user_value(triggerId=103, key='BridgeOpen', value=2)
        set_user_value(triggerId=104, key='BridgeOpen', value=2)
        set_user_value(triggerId=105, key='BridgeOpen', value=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[507]):
            return ThirdBattle()


class ThirdBattle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[907,908,909], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001035], arg2=0):
            return ThirdBridgeOn()


class ThirdBridgeOn(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        destroy_monster(spawnIds=[907,908,909])
        set_mesh(triggerIds=[3310], visible=False, arg3=0, arg4=0, arg5=0) # 3rdBridgeBarrier
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309], visible=True, arg3=0, arg4=100, arg5=10) # 3rdBridge
        set_user_value(triggerId=101, key='BridgeOpen', value=3)
        set_user_value(triggerId=102, key='BridgeOpen', value=3)
        set_user_value(triggerId=103, key='BridgeOpen', value=3)
        set_user_value(triggerId=104, key='BridgeOpen', value=3)
        set_user_value(triggerId=105, key='BridgeOpen', value=3)
        set_user_value(triggerId=106, key='BridgeOpen', value=3)
        set_user_value(triggerId=107, key='BridgeOpen', value=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            return BossBattle01()


class BossBattle01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return Success()

    def on_exit(self):
        destroy_monster(spawnIds=[99])


class Success(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


