""" trigger/52010032_qd/main_quest10003078.xml """
from common import *
import state


#  무르파고스 신전에 나메드를 만나러 들어오는 퀘스트 
class 무르파고스에들어오면(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=False) # 퀘스트 나메드: 11000039

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003078], questStates=[2]):
            set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[301], arg2=True) # 시끄러운 주먹
        create_monster(spawnIds=[302], arg2=True) # 에바고르
        move_user(mapId=52010032, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 무르파고스이동()


class 무르파고스이동(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 무르파고스이동01()


class 무르파고스이동01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user_path(patrolName='MS2PatrolData_3005')
        move_npc(spawnId=301, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=302, patrolName='MS2PatrolData_3004')
        show_caption(type='VerticalCaption', title='$52010032_QD__MAIN_QUEST10003078__0$', desc='$52010032_QD__MAIN_QUEST10003078__1$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_balloon_talk(spawnId=301, msg='$52010032_QD__MAIN_QUEST10003078__2$', duration=2000, delayTick=1000)
        add_balloon_talk(spawnId=302, msg='$52010032_QD__MAIN_QUEST10003078__3$', duration=2000, delayTick=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 나메드에게퀘스트받기()


class 나메드에게퀘스트받기(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return None # Missing State: 


