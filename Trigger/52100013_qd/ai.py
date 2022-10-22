""" trigger/52100013_qd/ai.xml """
from common import *
import state


#  플레이어 감지 
#  슈팅전 체크 에디셔널 이펙트를 계속 걸어줌 
class IsDungeonRoomReady(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return idle()
        if not is_dungeon_room():
            return questIdle()


class idle(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910120, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='Ground', value=1):
            remove_buff(boxId=701, skillId=99910120)
            return ready()
        if wait_tick(waitTick=500):
            return buff_01()
        if user_value(key='Ending', value=1):
            return Ending()


class buff_01(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910120, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='Ground', value=1):
            remove_buff(boxId=701, skillId=99910120)
            return ready()
        if wait_tick(waitTick=500):
            return idle()
        if user_value(key='Ending', value=1):
            return Ending()


class questIdle(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910120, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[2]):
            return QuestEnd_warp()
        if quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return Ending()
        if user_value(key='Ground', value=1):
            remove_buff(boxId=701, skillId=99910120)
            return ready()
        if wait_tick(waitTick=500):
            return questIdle_buff_01()
        if user_value(key='Ending', value=1):
            return Ending()


class questIdle_buff_01(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910120, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return Ending()
        if user_value(key='Ground', value=1):
            remove_buff(boxId=701, skillId=99910120)
            return ready()
        if wait_tick(waitTick=500):
            return questIdle()
        if user_value(key='Ending', value=1):
            return Ending()


class ready(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=11001, isEnable=False)
        enable_spawn_point_pc(spawnId=11002, isEnable=True)
        remove_buff(boxId=701, skillId=99910120)
        set_mesh(triggerIds=[1001,1002], visible=False)
        set_mesh(triggerIds=[1004,1005,1006], visible=False)
        # <action name="SetLocalCamera" cameraId="8001" enable="0"/>
        set_local_camera(cameraId=8002, enable=True)
        set_conversation(type=1, spawnId=102, script='$52100013_QD__AI__7$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$52100013_QD__AI__0$', arg4=2, arg5=0)
        destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510]) # 수중 위 몬스터 제거

    def on_tick(self) -> state.State:
        if user_value(key='Ending', value=1):
            return Ending()
        if monster_dead(boxIds=[201,210]):
            return Ending()


class Ending(state.State):
    def on_enter(self):
        remove_buff(boxId=701, skillId=99910120)
        set_effect(triggerIds=[7001], visible=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[201,210,101,102]) # 메비딕 제거
        create_monster(spawnIds=[202,103,104], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ending_02()


class Ending_02(state.State):
    def on_enter(self):
        set_skip(state=Ending_04)
        destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510]) # 수중 위 몬스터 제거
        select_camera_path(pathIds=[8101,8102,8103], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=202, sequenceName='Stun_A', duration=9000000)
        move_npc(spawnId=103, patrolName='MS2PatrolData_2008')
        move_npc(spawnId=104, patrolName='MS2PatrolData_2007')
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100013_QD__AI__1$', align='right', duration=2000)
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100013_QD__AI__2$', align='left', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Ending_03()


class Ending_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$52100013_QD__AI__3$', arg4=2, arg5=0)
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100013_QD__AI__4$', align='left', duration=2000)
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100013_QD__AI__5$', align='right', duration=2000)
        set_conversation(type=1, spawnId=202, script='$52100013_QD__AI__6$', arg4=2, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Ending_04()


class Ending_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ending_04_b()


class Ending_04_b(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ending_05()


class Ending_05(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=False) # LocalTargetCamera
        set_local_camera(cameraId=8002, enable=False) # LocalTargetCamera
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return IsDungeonRoom()


class IsDungeonRoom(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return dungeonEnd()
        if not is_dungeon_room():
            return questEnd()


class dungeonEnd(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1004,1005,1006], visible=False)
        set_effect(triggerIds=[7001], visible=False)
        set_mesh(triggerIds=[1001,1002], visible=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_achievement(triggerId=701, type='trigger', achieve='clearalbanos')
        set_achievement(triggerId=701, type='trigger', achieve='ClearOceanKing')
        dungeon_clear()

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[2]):
            return QuestEnd_warp()


class questEnd(state.State):
    def on_enter(self):
        remove_buff(boxId=701, skillId=99910120)
        set_mesh(triggerIds=[1004,1005,1006], visible=False)
        set_effect(triggerIds=[7001], visible=False)
        set_mesh(triggerIds=[1001,1002], visible=False)
        set_achievement(triggerId=701, type='trigger', achieve='clearalbanos')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[2]):
            return QuestEnd_warp()


class QuestEnd_warp(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestEnd_warp_End()

    def on_exit(self):
        move_user(mapId=52010068, portalId=6001)


class QuestEnd_warp_End(state.State):
    pass


