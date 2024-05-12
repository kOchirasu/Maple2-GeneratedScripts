""" trigger/52010008_qd/catchjailbreaker01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[901,902,903,904,905,906], animationEffect=False)
        self.set_interact_object(triggerIds=[10000851], state=0)
        self.set_mesh(triggerIds=[6000], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 전투안내01(self.ctx)


class 전투안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=100, textId=40010) # 적을 모두 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906]):
            return 죄수찾기01(self.ctx)


class 죄수찾기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=100)
        self.set_interact_object(triggerIds=[10000851], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000851], stateValue=0):
            return 죄수등장01(self.ctx)


class 죄수등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[6000], visible=False, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='11', seconds=1)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 죄수등장02(self.ctx)


class 죄수등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='12', seconds=2)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 벨마등장01(self.ctx)


class 벨마등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='20', seconds=1)
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.select_camera(triggerId=601, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 벨마대화01(self.ctx)


class 벨마대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='21', seconds=3)
        self.set_conversation(type=2, spawnId=11000521, script='$52010008_QD__CATCHJAILBREAKER01__0$', arg4=3)
        self.set_skip(state=벨마대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return 벨마대화02대기(self.ctx)


class 벨마대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 벨마대화02(self.ctx)


class 벨마대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='22', seconds=3)
        self.set_conversation(type=2, spawnId=11000521, script='$52010008_QD__CATCHJAILBREAKER01__1$', arg4=3)
        self.set_skip(state=벨마대화03대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='22'):
            return 벨마대화03대기(self.ctx)


class 벨마대화03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 벨마대화03(self.ctx)


class 벨마대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='23', seconds=3)
        self.set_conversation(type=2, spawnId=11000521, script='$52010008_QD__CATCHJAILBREAKER01__2$', arg4=3)
        self.set_skip(state=벨마연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='23'):
            return 벨마연출종료01(self.ctx)


class 벨마연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_timer(timerId='30', seconds=1)
        self.select_camera(triggerId=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=9000, type='trigger', achieve='catchjailbreaker')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            return 유저이동준비(self.ctx)


class 유저이동준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='31', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='31'):
            return 유저이동시작(self.ctx)


class 유저이동시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2010019, portalId=2, boxId=9000)
        self.destroy_monster(spawnIds=[101,201,301])
        self.destroy_monster(spawnIds=[901,902,903,904,905,906])


initial_state = 대기
