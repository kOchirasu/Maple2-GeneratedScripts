""" trigger/02010049_bf/main01.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # Voice 60000509
        set_mesh(triggerIds=[10000], visible=True, arg3=0, arg4=0, arg5=0) # battle02
        set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True, arg3=0, arg4=0, arg5=0) # battle02 flag
        set_mesh(triggerIds=[20000], visible=True, arg3=0, arg4=0, arg5=0) # battle03
        set_mesh(triggerIds=[30000], visible=True, arg3=0, arg4=0, arg5=0) # battle04
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=True, arg3=0, arg4=0, arg5=0) # battle03 flag
        set_mesh(triggerIds=[9990,9991,9992,9993], visible=True, arg3=0, arg4=0, arg5=0) # startzone
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017], visible=True, arg3=0, arg4=0, arg5=0) # startzone flag
        set_mesh(triggerIds=[7000,7001,7002,7003], visible=False, arg3=0, arg4=0, arg5=0) # bridge

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        create_monster(spawnIds=[102,103,104,105,107,108], arg2=False)
        create_monster(spawnIds=[201,202,203,204,205,206], arg2=False)
        show_guide_summary(entityId=20104901, textId=20104901, duration=3000) # 벌레떼가 모여들고 있습니다.
        play_system_sound_in_box(sound='System_Space_PopUp_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraWalk01()

state.DungeonStart = DungeonStart


class CameraWalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_skip(state=CameraWalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CameraWalk02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class CameraWalk02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GateOpen01()


class GateOpen01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9990,9991,9992,9993], visible=False, arg3=0, arg4=0, arg5=0) # startzone
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017], visible=False, arg3=0, arg4=0, arg5=10) # startzone flag

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 전투지역01시작()


class 전투지역01시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104902, textId=20104902, duration=5000) # 달려드는 벌레들을 모두 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,103,104,105,107,108]):
            return 전투지역02대기()


class 전투지역02대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=False, arg3=0, arg4=0, arg5=0) # battle02
        set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=False, arg3=0, arg4=0, arg5=10) # battle02 flag
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104903, textId=20104903, duration=5000) # 안 쪽에 벌레들이 더 있습니다.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 전투지역02시작()


class 전투지역02시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104902, textId=20104902, duration=5000) # 달려드는 벌레들을 모두 처치하세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투지역02추가()


class 전투지역02추가(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104904, textId=20104904, duration=5000) # 화장실 악취에는 벌레도 기절합니다.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206]):
            return 전투지역03대기()


class 전투지역03대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20000], visible=False, arg3=0, arg4=0, arg5=0) # battle03
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=False, arg3=0, arg4=0, arg5=10) # battle03 flag
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104903, textId=20104903, duration=5000) # 안 쪽에 벌레들이 더 있습니다.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return 전투지역03시작()


class 전투지역03시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[399], arg2=False) # boss
        create_monster(spawnIds=[302,303,304,305,306,307], arg2=False)
        create_monster(spawnIds=[309], arg2=False) # elite
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104902, textId=20104902, duration=5000) # 달려드는 벌레들을 모두 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[302,303,304,305,306,307]):
            return 전투지역04시작()


class 전투지역04시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=20104904, textId=20104904, duration=5000) # 화장실 악취에는 벌레도 기절합니다.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[309]):
            return 퇴장연출01()


class 퇴장연출01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[399])
        create_monster(spawnIds=[400], arg2=False)
        move_npc(spawnId=400, patrolName='MS2PatrolData_399')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 퇴장연출02()


class 퇴장연출02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # Voice 60000509

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퇴장연출03()


class 퇴장연출03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8000, spawnIds=[400]):
            return 다리생성01()


class 다리생성01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[400])
        set_mesh(triggerIds=[30000], visible=False, arg3=0, arg4=0, arg5=0) # battle04
        set_random_mesh(triggerIds=[7000,7001,7002,7003], visible=True, meshCount=4, arg4=100, delay=100) # bridge
        show_guide_summary(entityId=20104905, textId=20104905, duration=6000) # 포탈을 타세요
        play_system_sound_in_box(sound='System_Space_PopUp_01')

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9010]):
            return 종료()


class 종료(state.State):
    pass


