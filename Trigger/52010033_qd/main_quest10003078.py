""" trigger/52010033_qd/main_quest10003078.xml """
from common import *
import state


#  페리온 병원 : 52010033  
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003078], questStates=[2]):
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        visible_my_pc(isVisible=False)
        move_user(mapId=52010033, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 티나감사()


class 티나감사(state.State):
    def on_enter(self):
        set_scene_skip(state=나메드들어옴02, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4002], returnView=False)
        add_cinematic_talk(npcId=11003420, msg='$52010033_QD__MAIN_QUEST10003078__0$', duration=4000)
        add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__1$', duration=3000)
        add_cinematic_talk(npcId=11003420, msg='$52010033_QD__MAIN_QUEST10003078__2$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 나메드들어옴()


class 나메드들어옴(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[201], arg2=True) # 나메드:
        select_camera_path(pathIds=[4002,4001], returnView=False)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        show_caption(type='VerticalCaption', title='$52010033_QD__MAIN_QUEST10003078__3$', desc='$52010033_QD__MAIN_QUEST10003078__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2)
        add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__5$', duration=5000)
        add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__6$', duration=4500)
        add_cinematic_talk(npcId=11003420, msg='$52010033_QD__MAIN_QUEST10003078__7$', duration=2000)
        add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__8$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010033_QD__MAIN_QUEST10003078__9$', duration=2000)
        add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__10$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=22000):
            return 나메드들어옴_1()


class 나메드들어옴_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 나메드들어옴02()


class 나메드들어옴02(state.State):
    def on_enter(self):
        move_user(mapId=52010032, portalId=1)


