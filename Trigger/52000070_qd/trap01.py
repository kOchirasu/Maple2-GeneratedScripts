""" trigger/52000070_qd/trap01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=False) # SlidingBoard
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # SlidingBoard
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=0) # WallforMinimap
        self.set_mesh(triggerIds=[4100], visible=False, arg3=0, delay=0, scale=0) # BoardOpened
        self.set_mesh(triggerIds=[4200], visible=True, arg3=0, delay=0, scale=0) # BoardClosed
        self.set_actor(triggerId=3000, visible=True, initialSequence='Closed') # Door
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[6000], visible=False) # LargeGear_SlidingBoard
        self.set_effect(triggerIds=[6100], visible=False) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[1]):
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCEnter01(self.ctx)


class PCEnter01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCEnter02(self.ctx)


class PCEnter02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)
        self.set_mesh(triggerIds=[4200], visible=False, arg3=100, delay=0, scale=3) # BoardClosed
        self.set_breakable(triggerIds=[4000], enable=True) # SlidingBoard
        self.set_visible_breakable_object(triggerIds=[4000], visible=True) # SlidingBoard
        self.set_effect(triggerIds=[6000], visible=True) # LargeGear_SlidingBoard

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BoardSlide01(self.ctx)


class BoardSlide01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=True, initialSequence='Opened') # Door
        self.set_effect(triggerIds=[6100], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BoardSlide02(self.ctx)


class BoardSlide02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4100], visible=True, arg3=800, delay=0, scale=3) # BoardOpened

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyNpcWalkIn01(self.ctx)


class EnemyNpcWalkIn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=False) # LargeGear_SlidingBoard
        self.set_breakable(triggerIds=[4000], enable=False) # SlidingBoard
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # SlidingBoard
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyNpcWalkIn02(self.ctx)


class EnemyNpcWalkIn02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=602, enable=True)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyNpcWalkIn03(self.ctx)


class EnemyNpcWalkIn03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyNpcWalkIn04(self.ctx)


class EnemyNpcWalkIn04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104')
        self.select_camera(triggerId=603, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyNpcTalk01(self.ctx)


class EnemyNpcTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001963, script='$52000070_QD__TRAP01__0$', arg4=5) # 카트반의 첩자
        self.set_skip(state=EnemyNpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return EnemyNpcTalk01Skip(self.ctx)


class EnemyNpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return EnemyNpcTalk02(self.ctx)


class EnemyNpcTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001963, script='$52000070_QD__TRAP01__1$', arg4=5) # 카트반의 첩자
        self.set_skip(state=EnemyNpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return EnemyNpcTalk02Skip(self.ctx)


class EnemyNpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return EnemyMobChange01(self.ctx)


class EnemyMobChange01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.destroy_monster(spawnIds=[101,102,103,104])
        self.create_monster(spawnIds=[901,902,903,904], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904]):
            return BattleEnd01(self.ctx)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCPositionFix01(self.ctx)


class PCPositionFix01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=604, enable=True)
        self.move_user(mapId=52000070, portalId=10, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCPositionFix02(self.ctx)


class PCPositionFix02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FriendNpcWalkIn01(self.ctx)


class FriendNpcWalkIn01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FriendNpcWalkIn02(self.ctx)


class FriendNpcWalkIn02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.select_camera(triggerId=605, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FriendNpcTalk01(self.ctx)


class FriendNpcTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001964, script='$52000070_QD__TRAP01__2$', arg4=4) # 험플스 대원
        self.set_skip(state=FriendNpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FriendNpcTalk01Skip(self.ctx)


class FriendNpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return FriendNpcTalk02(self.ctx)


class FriendNpcTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001964, script='$52000070_QD__TRAP01__3$', arg4=4) # 험플스 대원
        self.set_skip(state=FriendNpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FriendNpcTalk02Skip(self.ctx)


class FriendNpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WayOpen01(self.ctx)


class WayOpen01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_211')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_212')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WayOpen02(self.ctx)


class WayOpen02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_213')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_214')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WayOpen03(self.ctx)


class WayOpen03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=201, script='$52000070_QD__TRAP01__4$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return QuestCom(self.ctx)


class QuestCom(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='remnantssweeping')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[2]):
            return MoveToComplete(self.ctx)


class MoveToComplete(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.move_user(mapId=2000208, portalId=1)


initial_state = Wait
