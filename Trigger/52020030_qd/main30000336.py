""" trigger/52020030_qd/main30000336.xml """
from common import *
import state


#  투르카와 전투 
class 체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2003], questIds=[30000336], questStates=[2]):
            return 체크2()


class 체크2(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        set_scene_skip(state=세번째연출대화진행05, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출대화진행_01()


class 세번째연출대화진행_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003756, msg='...계획이 틀어졌군.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출대화진행()


class 세번째연출대화진행(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003753, msg='... 왔나.\n바보같은 행동을 했더군.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출대화진행02()


class 세번째연출대화진행02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4022], returnView=False)
        set_npc_emotion_sequence(spawnId=108, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003756, msg='... 할말 없어.\n그래서, 이제 어쩔 셈이지?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째연출대화진행03()


class 세번째연출대화진행03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='훗. 바보같이.\n이제 흑성회가 움직이긴 어렵겠군.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출대화진행03_01()


class 세번째연출대화진행03_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4040], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='또 다른 계획을 준비해야겠어.', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째연출대화진행04()


class 세번째연출대화진행04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4022], returnView=False)
        set_npc_emotion_sequence(spawnId=108, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003753, msg='그 새로운 계획, 흑성회에도 당연히 전달해 주겠지?\n기대할께.', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째연출대화진행05()


class 세번째연출대화진행05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출대화진행06()


class 세번째연출대화진행06(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        visible_my_pc(isVisible=True)
        move_user(mapId=2020017, portalId=4)


