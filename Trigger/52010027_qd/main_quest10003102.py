""" trigger/52010027_qd/main_quest10003102.xml """
from common import *
import state


#  바람의 골짜기 : 52010027  
#  중간 보스 사라짐  
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003102], questStates=[1]):
            return Del()


class Del(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010027, portalId=6007)
        create_monster(spawnIds=[803], arg2=True)
        set_npc_emotion_loop(spawnId=803, sequenceName='Stun_A', duration=160000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 엔피씨와말을걸면()


class 엔피씨와말을걸면(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스몬스터는소멸준비()


class 보스몬스터는소멸준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=완료조건, arg2='exit')
        add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__0$', duration=4000)
        add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 보스몬스터는소멸준비01()


class 보스몬스터는소멸준비01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__2$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__3$', duration=3000)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 보스몬스터는소멸준비02()


class 보스몬스터는소멸준비02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__4$', duration=4000)
        add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__5$', duration=3000)
        add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__6$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 보스몬스터는소멸()


class 보스몬스터는소멸(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 보스몬스터는소멸_01()


class 보스몬스터는소멸_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[803])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투종료()


class 전투종료(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__7$', duration=2000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__8$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__9$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 전투종료01()


class 전투종료01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투종료02()


class 전투종료02(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 완료조건()


class 완료조건(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='WindValleyBattle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        move_user(mapId=2000051, portalId=3)


