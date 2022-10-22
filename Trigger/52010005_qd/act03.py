""" trigger/52010005_qd/act03.xml """
from common import *
import state


class 퀘스트조건03(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000872], state=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002822], questStates=[1]):
            return Q3_딜레이01()


class Q3_딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='100', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return Q3_미카등장01()


#   3rd Quest  
class Q3_미카등장01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[601], arg2=False)
        move_npc(spawnId=601, patrolName='MS2PatrolData_6010')
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[501], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return Q3_미카연출01()


class Q3_미카연출01(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=5)
        select_camera_path(pathIds=[2001,2002], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return Q3_미카연출02()


class Q3_미카연출02(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=8003, spawnIds=[601]):
            return Q3_미카연출03()


class Q3_미카연출03(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=4)
        move_npc(spawnId=601, patrolName='MS2PatrolData_6011')
        select_camera_path(pathIds=[2002,2001], returnView=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return Q3_미카연출04()


class Q3_미카연출04(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000872], state=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000872], arg2=0):
            return Q3_영상재생()


class Q3_영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='MemoryofDragon.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return Q3_시네마틱연출01()


class Q3_시네마틱연출01(state.State):
    def on_enter(self):
        set_timer(timerId='25', seconds=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT03__0$', arg4=4)
        set_skip(state=Q3_시네마틱연출02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return Q3_시네마틱연출02대기()


class Q3_시네마틱연출02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return Q3_시네마틱연출02()


class Q3_시네마틱연출02(state.State):
    def on_enter(self):
        select_camera(triggerId=4001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return Q3_시네마틱연출03()


class Q3_시네마틱연출03(state.State):
    def on_enter(self):
        set_timer(timerId='26', seconds=3)
        set_conversation(type=2, spawnId=11001316, script='$52010005_QD__ACT03__1$', arg4=3)
        set_skip(state=Q3_시네마틱연출04)

    def on_tick(self) -> state.State:
        if time_expired(timerId='26'):
            return Q3_시네마틱연출04()


class Q3_시네마틱연출04(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Q3_시네마틱연출05()


class Q3_시네마틱연출05(state.State):
    def on_enter(self):
        set_timer(timerId='27', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='27'):
            return Q3_미카퇴장01()


class Q3_미카퇴장01(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=2)
        move_npc(spawnId=601, patrolName='MS2PatrolData_6013')

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return Q3_미카퇴장02()


class Q3_미카퇴장02(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=3)
        set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT03__2$', arg4=3)
        set_skip(state=Q3_미카퇴장03)

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return Q3_미카퇴장03()

    def on_exit(self):
        remove_cinematic_talk()


class Q3_미카퇴장03(state.State):
    def on_enter(self):
        move_npc(spawnId=601, patrolName='MS2PatrolData_6014')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8010, spawnIds=[601]):
            return Q3_미카퇴장04()


class Q3_미카퇴장04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601])
        set_timer(timerId='40', seconds=1)
        select_camera(triggerId=4001, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='40'):
            return Q3_업적발생()


class Q3_업적발생(state.State):
    def on_enter(self):
        set_achievement(triggerId=9001, type='trigger', achieve='Intothememory')
        destroy_monster(spawnIds=[501])
        create_monster(spawnIds=[502], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002823], questStates=[2]):
            return Q3_유저퇴장01()


class Q3_유저퇴장01(state.State):
    def on_enter(self):
        set_timer(timerId='41', seconds=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='41'):
            return Q3_유저퇴장02()

    def on_exit(self):
        remove_cinematic_talk()


class Q3_유저퇴장02(state.State):
    def on_enter(self):
        set_timer(timerId='42', seconds=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001316, script='$52010005_QD__ACT03__3$', arg4=4)
        set_skip(state=Q3_유저퇴장03)

    def on_tick(self) -> state.State:
        if time_expired(timerId='42'):
            return Q3_유저퇴장03()

    def on_exit(self):
        remove_cinematic_talk()


class Q3_유저퇴장03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2010026, portalId=3, boxId=9000)


