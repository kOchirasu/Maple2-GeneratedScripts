""" trigger/52000012_qd/main.xml """
import trigger_api


class 초기상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[6000], visible=True)
        self.set_agent(triggerIds=[6001], visible=True)
        self.set_agent(triggerIds=[6002], visible=True)
        self.set_agent(triggerIds=[6003], visible=True)
        self.set_agent(triggerIds=[6004], visible=True)
        self.set_agent(triggerIds=[6005], visible=True)
        self.set_agent(triggerIds=[6006], visible=True)
        self.set_agent(triggerIds=[6007], visible=True)
        self.set_agent(triggerIds=[6008], visible=True)
        self.set_agent(triggerIds=[6009], visible=True)
        self.set_agent(triggerIds=[6010], visible=True)
        self.set_agent(triggerIds=[6011], visible=True)
        self.set_agent(triggerIds=[6012], visible=True)
        self.set_agent(triggerIds=[6013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_actor(triggerId=5001, visible=False, initialSequence='DownIdle_B')
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_actor(triggerId=10001, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=10002, visible=True, initialSequence='Closed')
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[5000], animationEffect=False)
        self.set_agent(triggerIds=[7000], visible=True)
        self.set_agent(triggerIds=[7001], visible=True)
        self.set_agent(triggerIds=[7002], visible=True)
        self.set_agent(triggerIds=[7003], visible=True)
        self.set_agent(triggerIds=[7004], visible=True)
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_mesh(triggerIds=[10011], visible=True)
        self.set_mesh(triggerIds=[10012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002610], questStates=[1]):
            return 레논연출1(self.ctx)


class 레논연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='9', seconds=2)
        self.create_monster(spawnIds=[1000], animationEffect=False)
        self.set_agent(triggerIds=[7000], visible=False)
        self.set_agent(triggerIds=[7001], visible=False)
        self.set_agent(triggerIds=[7002], visible=False)
        self.set_agent(triggerIds=[7003], visible=False)
        self.set_agent(triggerIds=[7004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return 레논연출2(self.ctx)


class 레논연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 전투1(self.ctx)


class 전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            return 벨라연출시작(self.ctx)


class 벨라연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='8', seconds=3)
        self.select_camera_path(pathIds=[901,902], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='8'):
            return 벨라연출중(self.ctx)


class 벨라연출중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='11', seconds=7)
        self.set_conversation(type=2, spawnId=11000844, script='$52000012_QD__MAIN__1$', arg4=2)
        self.set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__2$', arg4=2)
        self.set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__3$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 벨라연출종료(self.ctx)


class 벨라연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='14', seconds=1)
        self.select_camera_path(pathIds=[906], returnView=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 문열림1(self.ctx)


class 문열림1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='19', seconds=1)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.set_actor(triggerId=10001, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[10011], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='19'):
            return 전투2(self.ctx)


class 전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1000, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203]):
            return 문열림2(self.ctx)


class 문열림2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='12', seconds=2)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_actor(triggerId=10002, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[10012], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 악령연출시작(self.ctx)


class 악령연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='13', seconds=6)
        self.select_camera_path(pathIds=[904,905], returnView=False)
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='13'):
            return 화면끄기(self.ctx)


class 화면끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='22', seconds=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='22'):
            return 영혼연출(self.ctx)


class 영혼연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='23', seconds=2)
        self.destroy_monster(spawnIds=[301])
        self.destroy_monster(spawnIds=[5000])
        self.destroy_monster(spawnIds=[301])
        self.destroy_monster(spawnIds=[5000])
        self.set_actor(triggerId=5001, visible=True, initialSequence='DownIdle_B')
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='23'):
            return 화면켜기(self.ctx)


class 화면켜기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='14', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 영혼연출중(self.ctx)


class 영혼연출중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='15', seconds=4)
        self.set_conversation(type=2, spawnId=11000064, script='$52000012_QD__MAIN__4$', arg4=3)
        self.select_camera_path(pathIds=[905,903], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 영혼연출종료(self.ctx)


class 영혼연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1000, patrolName='MS2PatrolData_1002')
        self.select_camera(triggerId=903, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 전투3(self.ctx)


class 전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=5001, visible=False, initialSequence='DownIdle_B')
        self.set_effect(triggerIds=[5002], visible=False)
        self.create_monster(spawnIds=[302], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[302]):
            return 레논교체(self.ctx)


class 레논교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1000])
        self.create_monster(spawnIds=[2000], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[10002611], questStates=[2]):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9001]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1000,2000,101,102,103,201,202,203,301,302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 초기상태
