""" trigger/52010008_qd/catchjailbreaker01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901,902,903,904,905,906], arg2=False)
        set_interact_object(triggerIds=[10000851], state=0)
        set_mesh(triggerIds=[6000], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 딜레이01()


class 딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 전투안내01()


class 전투안내01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=100, textId=40010) # 적을 모두 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904,905,906]):
            return 죄수찾기01()


class 죄수찾기01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=100)
        set_interact_object(triggerIds=[10000851], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000851], arg2=0):
            return 죄수등장01()


class 죄수등장01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6000], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='11', seconds=1)
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1010')

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 죄수등장02()


class 죄수등장02(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=2)
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_2010')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 벨마등장01()


class 벨마등장01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=1)
        create_monster(spawnIds=[301], arg2=False)
        select_camera(triggerId=601, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 벨마대화01()


class 벨마대화01(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=3)
        set_conversation(type=2, spawnId=11000521, script='$52010008_QD__CATCHJAILBREAKER01__0$', arg4=3)
        set_skip(state=벨마대화02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 벨마대화02대기()


class 벨마대화02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 벨마대화02()


class 벨마대화02(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=3)
        set_conversation(type=2, spawnId=11000521, script='$52010008_QD__CATCHJAILBREAKER01__1$', arg4=3)
        set_skip(state=벨마대화03대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 벨마대화03대기()


class 벨마대화03대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 벨마대화03()


class 벨마대화03(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=3)
        set_conversation(type=2, spawnId=11000521, script='$52010008_QD__CATCHJAILBREAKER01__2$', arg4=3)
        set_skip(state=벨마연출종료01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 벨마연출종료01()


class 벨마연출종료01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='30', seconds=1)
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=9000, type='trigger', achieve='catchjailbreaker')

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 유저이동준비()


class 유저이동준비(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 유저이동시작()


class 유저이동시작(state.State):
    def on_enter(self):
        move_user(mapId=2010019, portalId=2, boxId=9000)
        destroy_monster(spawnIds=[101,201,301])
        destroy_monster(spawnIds=[901,902,903,904,905,906])


