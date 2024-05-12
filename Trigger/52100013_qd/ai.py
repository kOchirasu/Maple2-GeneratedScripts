""" trigger/52100013_qd/ai.xml """
import trigger_api


# 플레이어 감지
# 슈팅전 체크 에디셔널 이펙트를 계속 걸어줌
class IsDungeonRoomReady(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return idle(self.ctx)
        if not self.is_dungeon_room():
            return questIdle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[701], skillId=99910120, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Ground', value=1):
            self.remove_buff(boxId=701, skillId=99910120)
            return ready(self.ctx)
        if self.wait_tick(waitTick=500):
            return buff_01(self.ctx)
        if self.user_value(key='Ending', value=1):
            return Ending(self.ctx)


class buff_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[701], skillId=99910120, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Ground', value=1):
            self.remove_buff(boxId=701, skillId=99910120)
            return ready(self.ctx)
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)
        if self.user_value(key='Ending', value=1):
            return Ending(self.ctx)


class questIdle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[701], skillId=99910120, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[2]):
            return QuestEnd_warp(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return Ending(self.ctx)
        if self.user_value(key='Ground', value=1):
            self.remove_buff(boxId=701, skillId=99910120)
            return ready(self.ctx)
        if self.wait_tick(waitTick=500):
            return questIdle_buff_01(self.ctx)
        if self.user_value(key='Ending', value=1):
            return Ending(self.ctx)


class questIdle_buff_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[701], skillId=99910120, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return Ending(self.ctx)
        if self.user_value(key='Ground', value=1):
            self.remove_buff(boxId=701, skillId=99910120)
            return ready(self.ctx)
        if self.wait_tick(waitTick=500):
            return questIdle(self.ctx)
        if self.user_value(key='Ending', value=1):
            return Ending(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=11001, isEnable=False)
        self.enable_spawn_point_pc(spawnId=11002, isEnable=True)
        self.remove_buff(boxId=701, skillId=99910120)
        self.set_mesh(triggerIds=[1001,1002], visible=False)
        self.set_mesh(triggerIds=[1004,1005,1006], visible=False)
        # self.set_local_camera(cameraId=8001, enable=False)
        self.set_local_camera(cameraId=8002, enable=True)
        self.set_conversation(type=1, spawnId=102, script='$52100013_QD__AI__7$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52100013_QD__AI__0$', arg4=2, arg5=0)
        self.destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510]) # 수중 위 몬스터 제거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Ending', value=1):
            return Ending(self.ctx)
        if self.monster_dead(boxIds=[201,210]):
            return Ending(self.ctx)


class Ending(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=701, skillId=99910120)
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[201,210,101,102]) # 메비딕 제거
        self.create_monster(spawnIds=[202,103,104], animationEffect=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Ending_02(self.ctx)


class Ending_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=Ending_04)
        self.destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510]) # 수중 위 몬스터 제거
        self.select_camera_path(pathIds=[8101,8102,8103], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Stun_A', duration=9000000)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2008')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2007')
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100013_QD__AI__1$', align='right', duration=2000)
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100013_QD__AI__2$', align='left', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Ending_03(self.ctx)


class Ending_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=202, script='$52100013_QD__AI__3$', arg4=2, arg5=0)
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100013_QD__AI__4$', align='left', duration=2000)
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100013_QD__AI__5$', align='right', duration=2000)
        self.set_conversation(type=1, spawnId=202, script='$52100013_QD__AI__6$', arg4=2, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return Ending_04(self.ctx)


class Ending_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ending_04_b(self.ctx)


class Ending_04_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Ending_05(self.ctx)


class Ending_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(cameraId=8001, enable=False) # LocalTargetCamera
        self.set_local_camera(cameraId=8002, enable=False) # LocalTargetCamera
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return IsDungeonRoom(self.ctx)


class IsDungeonRoom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return dungeonEnd(self.ctx)
        if not self.is_dungeon_room():
            return questEnd(self.ctx)


class dungeonEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1004,1005,1006], visible=False)
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_mesh(triggerIds=[1001,1002], visible=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_achievement(triggerId=701, type='trigger', achieve='clearalbanos')
        self.set_achievement(triggerId=701, type='trigger', achieve='ClearOceanKing')
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[2]):
            return QuestEnd_warp(self.ctx)


class questEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=701, skillId=99910120)
        self.set_mesh(triggerIds=[1004,1005,1006], visible=False)
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_mesh(triggerIds=[1001,1002], visible=False)
        self.set_achievement(triggerId=701, type='trigger', achieve='clearalbanos')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[2]):
            return QuestEnd_warp(self.ctx)


class QuestEnd_warp(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return QuestEnd_warp_End(self.ctx)

    def on_exit(self) -> None:
        self.move_user(mapId=52010068, portalId=6001)


class QuestEnd_warp_End(trigger_api.Trigger):
    pass


initial_state = IsDungeonRoomReady
