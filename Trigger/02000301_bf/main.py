""" trigger/02000301_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000585], state=0)
        self.set_interact_object(triggerIds=[11000004], state=2)
        self.set_interact_object(triggerIds=[13000006], state=2)
        self.set_effect(triggerIds=[604], visible=False)
        self.create_monster(spawnIds=[1007,1008], animationEffect=False)
        self.create_monster(spawnIds=[2099], animationEffect=False)
        self.set_mesh(triggerIds=[4998,4999], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 트리스탄01(self.ctx)


class 트리스탄01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=2, spawnId=11000252, script='$02000301_BF__MAIN__0$', arg4=4)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 몬스터전투(self.ctx)


class 몬스터전투(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[1007,1008]):
            return 골두스이동(self.ctx)


class 골두스이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2099, patrolName='MS2PatrolData_2098')
        self.set_conversation(type=1, spawnId=2099, script='$02000301_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1007,1008]):
            return 또다른연출시작(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[4998,4999], visible=False, arg3=0, delay=0, scale=0)


class 또다른연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=1)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 골두스마무리(self.ctx)


class 골두스마무리(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=2, spawnId=11000252, script='$02000301_BF__MAIN__2$', arg4=4)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 또다른연출종료(self.ctx)


class 또다른연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000585], state=1)
        self.show_guide_summary(entityId=20002999, textId=20002999)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.move_npc(spawnId=2099, patrolName='MS2PatrolData_2099')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000585], stateValue=0):
            self.hide_guide_summary(entityId=20002999)
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_timer(timerId='4', seconds=4)
        self.show_count_ui(text='$02000301_BF__MAIN__4$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            self.move_user(mapId=2000299, portalId=2, boxId=199)
            return 이동대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
