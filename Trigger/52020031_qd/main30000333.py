""" trigger/52020031_qd/main30000333.xml """
from common import *
import state


#  제단 입장 
# 
# 예상치 못한 인물 하렌(11003747) - spawnpoint : 1 
# 한순간의 방심 하렌(11003749) - spawnpoint : 2
# 연출용 하렌(11003756) - spawnpoint : 101 
# 
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000333], questStates=[1]):
            return 두번째연출준비()


class 두번째연출준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 두번째연출준비_01()


class 두번째연출준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[102]) # 퀘스트용 하렌
        create_monster(spawnIds=[101], arg2=False)
        select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 두번째연출준비_02()


class 두번째연출준비_02(state.State):
    def on_enter(self):
        move_user(mapId=52020031, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 두번째연출()


class 두번째연출(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='천공의 심장을 돌려줘.', duration=3000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 두번째연출_01()


class 두번째연출_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 두번째연출_02()


class 두번째연출_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003756, msg='곱게 가져갈 수 있을 거라고 생각해?', duration=3000)
        add_cinematic_talk(npcId=11003756, msg='꿈도 야무지다니까... 호호호', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 두번째연출_03()


class 두번째연출_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 두번째연출전투준비_01()


class 두번째연출전투준비_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 두번째연출전투준비()


class 두번째연출전투준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=2) # UI 숨기기 초기화
        set_cinematic_ui(type=0) # 유저 이동 가능하게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 두번째연출전투준비1()


class 두번째연출전투준비1(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[601], arg2=False) # 몬스터 하렌
        set_event_ui(type=1, arg2='하렌을 처치하세요!', arg3='2000', arg4='0')
        add_balloon_talk(spawnId=601, msg='숨통을 끊어주마.', duration=3000, delayTick=3000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601]):
            return 두번째연출전투종료1()


class 두번째연출전투종료1(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0.5)
        move_user(mapId=52020031, portalId=6001)
        destroy_monster(spawnIds=[601])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 두번째연출전투종료2()


class 두번째연출전투종료2(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


