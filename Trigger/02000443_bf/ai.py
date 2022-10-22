""" trigger/02000443_bf/ai.xml """
from common import *
import state


#  플레이어 감지 
#  슈팅전 체크 에디셔널 이펙트를 계속 걸어줌 
class IsDungeonRoomReady(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return idle()


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Ending', value=1):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[210]) # 메비딕 제거
        destroy_monster(spawnIds=[101,102]) # 초반 등장 npc 제거

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ending()


class Ending(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=49200003, level=1, arg4=False, arg5=False)
        remove_buff(boxId=701, skillId=99910120)
        set_effect(triggerIds=[7001], visible=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[202,103,104], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ending_02()


class Ending_02(state.State):
    def on_enter(self):
        set_skip(state=Ending_04)
        select_camera_path(pathIds=[8101,8102,8103], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=202, sequenceName='Stun_A', duration=9000000)
        move_npc(spawnId=103, patrolName='MS2PatrolData_2008')
        move_npc(spawnId=104, patrolName='MS2PatrolData_2007')
        set_conversation(type=1, spawnId=103, script='$02000443_BF__AI__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=104, script='$02000443_BF__AI__1$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Ending_03()


class Ending_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$02000443_BF__AI__2$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=104, script='$02000443_BF__AI__3$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=103, script='$02000443_BF__AI__4$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=202, script='$02000443_BF__AI__5$', arg4=2, arg5=6)

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


class dungeonEnd(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        set_mesh(triggerIds=[1001,1002], visible=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_achievement(triggerId=701, type='trigger', achieve='clearalbanos')
        set_achievement(triggerId=701, type='trigger', achieve='ClearOceanKing')
        dungeon_clear()

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50001518], questStates=[1]):
            return None # Missing State: QuestEnd_warp


