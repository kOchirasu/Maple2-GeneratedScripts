""" trigger/52010030_qd/main.xml """
from common import *
import state


#  시련의 동굴 : 52010030  
#  에바고르 좌절씬  
class idle(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[101], arg2=True) # 에바고르: 11003391

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에바고르_독백_01()


class 에바고르_독백_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=200000) # 에바고르 좌절모션
        set_cinematic_ui(type=9, script='$52010030_QD__MAIN__0$', arg3=False)
        set_scene_skip(state=종료, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_독백_02()


class 에바고르_독백_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010030_QD__MAIN__1$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_독백_02_01()


class 에바고르_독백_02_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010030_QD__MAIN__2$', arg3=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_독백_03()


class 에바고르_독백_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010030_QD__MAIN__3$', arg3=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_독백_04()


class 에바고르_독백_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010030_QD__MAIN__4$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_좌절_01()


class 에바고르_좌절_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004,4001], returnView=False) # 에바고르 정면
        add_cinematic_talk(npcId=11003391, msg='$52010030_QD__MAIN__5$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_좌절_02()


class 에바고르_좌절_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__6$', duration=2000, align='Left')
        add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__7$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에바고르_좌절_03()


class 에바고르_좌절_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=200000) # 에바고르 좌절모션
        add_cinematic_talk(npcId=11003391, msg='$52010030_QD__MAIN__8$', duration=2000, align='Left')
        select_camera_path(pathIds=[4002], returnView=False) # 에바고르 얼굴 돌림

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 뮤테라피온_등장_01()


class 뮤테라피온_등장_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        # <action name="몬스터를생성한다" arg1="201" arg2="1" />
        add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__9$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 뮤테라피온_등장_02()


class 뮤테라피온_등장_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2002,4003], returnView=False) # 뮤테라 피온 줌인
        add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__10$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 잠시뒤()


class 잠시뒤(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010030_QD__MAIN__11$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 잠시뒤_1()


class 잠시뒤_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        move_user(mapId=2000146, portalId=3)


