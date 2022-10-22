""" trigger/52000070_qd/trap01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False) # SlidingBoard
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # SlidingBoard
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0) # WallforMinimap
        set_mesh(triggerIds=[4100], visible=False, arg3=0, arg4=0, arg5=0) # BoardOpened
        set_mesh(triggerIds=[4200], visible=True, arg3=0, arg4=0, arg5=0) # BoardClosed
        set_actor(triggerId=3000, visible=True, initialSequence='Closed') # Door
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[6000], visible=False) # LargeGear_SlidingBoard
        set_effect(triggerIds=[6100], visible=False) # DoorOpen

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[1]):
            return LoadingDelay01()


class LoadingDelay01(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCEnter01()


class PCEnter01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCEnter02()


class PCEnter02(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        set_mesh(triggerIds=[4200], visible=False, arg3=100, arg4=0, arg5=3) # BoardClosed
        set_breakable(triggerIds=[4000], enabled=True) # SlidingBoard
        set_visible_breakable_object(triggerIds=[4000], arg2=True) # SlidingBoard
        set_effect(triggerIds=[6000], visible=True) # LargeGear_SlidingBoard

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BoardSlide01()


class BoardSlide01(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=True, initialSequence='Opened') # Door
        set_effect(triggerIds=[6100], visible=True) # DoorOpen

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BoardSlide02()


class BoardSlide02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4100], visible=True, arg3=800, arg4=0, arg5=3) # BoardOpened

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyNpcWalkIn01()


class EnemyNpcWalkIn01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False) # LargeGear_SlidingBoard
        set_breakable(triggerIds=[4000], enabled=False) # SlidingBoard
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # SlidingBoard
        move_user_path(patrolName='MS2PatrolData_1000')
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyNpcWalkIn02()


class EnemyNpcWalkIn02(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=True)
        create_monster(spawnIds=[102], arg2=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyNpcWalkIn03()


class EnemyNpcWalkIn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyNpcWalkIn04()


class EnemyNpcWalkIn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=False)
        move_npc(spawnId=104, patrolName='MS2PatrolData_104')
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyNpcTalk01()


class EnemyNpcTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001963, script='$52000070_QD__TRAP01__0$', arg4=5) # 카트반의 첩자
        set_skip(state=EnemyNpcTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EnemyNpcTalk01Skip()


class EnemyNpcTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return EnemyNpcTalk02()


class EnemyNpcTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001963, script='$52000070_QD__TRAP01__1$', arg4=5) # 카트반의 첩자
        set_skip(state=EnemyNpcTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EnemyNpcTalk02Skip()


class EnemyNpcTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EnemyMobChange01()


class EnemyMobChange01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        destroy_monster(spawnIds=[101,102,103,104])
        create_monster(spawnIds=[901,902,903,904], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904]):
            return BattleEnd01()


class BattleEnd01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCPositionFix01()


class PCPositionFix01(state.State):
    def on_enter(self):
        select_camera(triggerId=604, enable=True)
        move_user(mapId=52000070, portalId=10, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCPositionFix02()


class PCPositionFix02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FriendNpcWalkIn01()


class FriendNpcWalkIn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,202,203,204], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FriendNpcWalkIn02()


class FriendNpcWalkIn02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        select_camera(triggerId=605, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FriendNpcTalk01()


class FriendNpcTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001964, script='$52000070_QD__TRAP01__2$', arg4=4) # 험플스 대원
        set_skip(state=FriendNpcTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FriendNpcTalk01Skip()


class FriendNpcTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FriendNpcTalk02()


class FriendNpcTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001964, script='$52000070_QD__TRAP01__3$', arg4=4) # 험플스 대원
        set_skip(state=FriendNpcTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FriendNpcTalk02Skip()


class FriendNpcTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WayOpen01()


class WayOpen01(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_211')
        move_npc(spawnId=202, patrolName='MS2PatrolData_212')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WayOpen02()


class WayOpen02(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_213')
        move_npc(spawnId=204, patrolName='MS2PatrolData_214')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WayOpen03()


class WayOpen03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000070_QD__TRAP01__4$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestCom()


class QuestCom(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='remnantssweeping')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[2]):
            return MoveToComplete()


class MoveToComplete(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        move_user(mapId=2000208, portalId=1)


