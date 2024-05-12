""" trigger/52010056_qd/eventsection_b.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2004]):
            return 연출준비_A(self.ctx)


class 연출준비_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.add_buff(boxIds=[2001], skillId=70000085, level=1, isPlayer=False, isSkillSet=True) # 연출용 무적 버프
        self.add_buff(boxIds=[2001], skillId=70000085, level=1, isPlayer=False, isSkillSet=False) # 연출용 무적 버프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출준비_B(self.ctx)


class 연출준비_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[999], animationEffect=False) # 크림슨 스피어: 29000386
        self.select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 경비병_스폰(self.ctx)


class 경비병_스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=121, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003816, msg='$52010056_QD__EventSection_B__0$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 경비병_이동시작(self.ctx)


class 경비병_이동시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=999, patrolName='MS2PatrolData_3008')
        self.select_camera_path(pathIds=[4005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조작_시작(self.ctx)


class 조작_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.remove_buff(boxId=2001, skillId=70000107)
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection_B__1$', arg3='3000', arg4='0')

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_sound(triggerId=7001, enable=False)


initial_state = Idle
