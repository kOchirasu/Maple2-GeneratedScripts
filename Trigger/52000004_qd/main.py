""" trigger/52000004_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.destroy_monster(spawnIds=[2001])
        self.destroy_monster(spawnIds=[2099])
        self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 던전시작(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 차목표1(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 차목표1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_timer(timerId='2', seconds=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000004_QD__MAIN__0$')
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.select_camera_path(pathIds=[301], returnView=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 피자들기(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 피자들기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.show_guide_summary(entityId=25200401, textId=25200401)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 엘리트스폰대기(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25200401)


class 엘리트스폰대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016], animationEffect=False)
        self.set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 엘리트스폰(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 엘리트스폰(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25200402, textId=25200402)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=True, arg3=0, delay=0, scale=2)
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.set_conversation(type=1, spawnId=2001, script='$52000004_QD__MAIN__3$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 벽해제(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25200402)


class 벽해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return NPC등장(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class NPC등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.create_monster(spawnIds=[2099], animationEffect=False)
        self.set_conversation(type=1, spawnId=2099, script='$52000004_QD__MAIN__4$', arg4=3)
        self.move_npc(spawnId=2099, patrolName='MS2PatrolData_2099')
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)
        if self.time_expired(timerId='5'):
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[10001852], questStates=[2]):
            self.set_event_ui(type=7, arg2='$52000004_QD__MAIN__5$', arg3='3000', arg4='0')
            return 포털생성(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[10001851], questStates=[2]):
            self.set_event_ui(type=7, arg2='$52000004_QD__MAIN__6$', arg3='3000', arg4='0')
            return 포털생성(self.ctx)
        if self.time_expired(timerId='3'):
            return 포털생성(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.show_guide_summary(entityId=25200403, textId=25200403)
            return 종료대기(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 종료대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            self.move_user(mapId=2000166, portalId=30, boxId=199)
            return 종료(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25200403)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2001])
        self.destroy_monster(spawnIds=[2099])
        self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
