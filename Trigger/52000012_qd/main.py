""" trigger/52000012_qd/main.xml """
from common import *
import state


class 초기상태(state.State):
    def on_enter(self):
        set_agent(triggerIds=[6000], visible=True)
        set_agent(triggerIds=[6001], visible=True)
        set_agent(triggerIds=[6002], visible=True)
        set_agent(triggerIds=[6003], visible=True)
        set_agent(triggerIds=[6004], visible=True)
        set_agent(triggerIds=[6005], visible=True)
        set_agent(triggerIds=[6006], visible=True)
        set_agent(triggerIds=[6007], visible=True)
        set_agent(triggerIds=[6008], visible=True)
        set_agent(triggerIds=[6009], visible=True)
        set_agent(triggerIds=[6010], visible=True)
        set_agent(triggerIds=[6011], visible=True)
        set_agent(triggerIds=[6012], visible=True)
        set_agent(triggerIds=[6013], visible=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=5001, visible=False, initialSequence='DownIdle_B')
        set_effect(triggerIds=[5002], visible=False)
        set_actor(triggerId=10001, visible=True, initialSequence='Closed')
        set_actor(triggerId=10002, visible=True, initialSequence='Closed')
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[5000], arg2=False)
        set_agent(triggerIds=[7000], visible=True)
        set_agent(triggerIds=[7001], visible=True)
        set_agent(triggerIds=[7002], visible=True)
        set_agent(triggerIds=[7003], visible=True)
        set_agent(triggerIds=[7004], visible=True)
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_mesh(triggerIds=[10011], visible=True)
        set_mesh(triggerIds=[10012], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002610], questStates=[1]):
            return 레논연출1()


class 레논연출1(state.State):
    def on_enter(self):
        set_timer(timerId='9', seconds=2)
        create_monster(spawnIds=[1000], arg2=False)
        set_agent(triggerIds=[7000], visible=False)
        set_agent(triggerIds=[7001], visible=False)
        set_agent(triggerIds=[7002], visible=False)
        set_agent(triggerIds=[7003], visible=False)
        set_agent(triggerIds=[7004], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return 레논연출2()


class 레논연출2(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__0$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 전투1()


class 전투1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            return 벨라연출시작()


class 벨라연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='8', seconds=3)
        select_camera_path(pathIds=[901,902], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='8'):
            return 벨라연출중()


class 벨라연출중(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=7)
        set_conversation(type=2, spawnId=11000844, script='$52000012_QD__MAIN__1$', arg4=2)
        set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__2$', arg4=2)
        set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__3$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 벨라연출종료()


class 벨라연출종료(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=1)
        select_camera_path(pathIds=[906], returnView=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 문열림1()


class 문열림1(state.State):
    def on_enter(self):
        set_timer(timerId='19', seconds=1)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        create_monster(spawnIds=[201], arg2=False)
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[203], arg2=False)
        set_actor(triggerId=10001, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[10011], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='19'):
            return 전투2()


class 전투2(state.State):
    def on_enter(self):
        move_npc(spawnId=1000, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203]):
            return 문열림2()


class 문열림2(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=2)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_actor(triggerId=10002, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[10012], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 악령연출시작()


class 악령연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='13', seconds=6)
        select_camera_path(pathIds=[904,905], returnView=False)
        create_monster(spawnIds=[301], arg2=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 화면끄기()


class 화면끄기(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 영혼연출()


class 영혼연출(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=2)
        destroy_monster(spawnIds=[301])
        destroy_monster(spawnIds=[5000])
        destroy_monster(spawnIds=[301])
        destroy_monster(spawnIds=[5000])
        set_actor(triggerId=5001, visible=True, initialSequence='DownIdle_B')
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 화면켜기()


class 화면켜기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='14', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 영혼연출중()


class 영혼연출중(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=4)
        set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__4$', arg4=3)
        select_camera_path(pathIds=[905,903], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 영혼연출종료()


class 영혼연출종료(state.State):
    def on_enter(self):
        move_npc(spawnId=1000, patrolName='MS2PatrolData_1002')
        select_camera(triggerId=903, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return 전투3()


class 전투3(state.State):
    def on_enter(self):
        set_actor(triggerId=5001, visible=False, initialSequence='DownIdle_B')
        set_effect(triggerIds=[5002], visible=False)
        create_monster(spawnIds=[302], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[302]):
            return 레논교체()


class 레논교체(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1000])
        create_monster(spawnIds=[2000], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[10002611], questStates=[2]):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9001]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1000,2000,101,102,103,201,202,203,301,302])

    def on_tick(self) -> state.State:
        if true():
            return 대기()


