""" trigger/52000002_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
        self.destroy_monster(spawnIds=[2099])
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3007,3008,3009,3010,3011,3012,3013], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000606], state=2)
        self.set_interact_object(triggerIds=[10000607,10000608,10000609,10000610,10000611], state=2)
        self.set_interact_object(triggerIds=[10000612,10000613,10000614,10000615,10000616], state=2)
        self.create_monster(spawnIds=[1099], animationEffect=False)
        self.create_monster(spawnIds=[1101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 던전시작(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 차목표1(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 차목표1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000002_QD__MAIN__0$')
        self.set_timer(timerId='5', seconds=5)
        self.set_skip(state=오브젝트생성)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 오브젝트생성(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 오브젝트생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000607,10000608,10000609,10000610,10000611], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000607,10000608,10000609,10000610,10000611], stateValue=0):
            return 단계준비2(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 단계준비2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3)
        self.show_guide_summary(entityId=25200202, textId=25200202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 레버대기(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 레버대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25200202)
        self.set_interact_object(triggerIds=[10000606], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000606], stateValue=0):
            return 다리생성(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, delay=300, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 단계시작2(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 단계시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000002_QD__MAIN__2$')
        self.set_timer(timerId='5', seconds=5)
        self.set_skip(state=양생성)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 양생성(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 양생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000612,10000613,10000614,10000615,10000616], state=1)
        self.create_monster(spawnIds=[2001,2002,2003,2004,2005], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000612,10000613,10000614,10000615,10000616], stateValue=2):
            return 단계준비3(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 단계준비3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=2)
        self.show_guide_summary(entityId=25200202, textId=25200202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 단계대기3(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 단계대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25200202)
        self.set_mesh(triggerIds=[3007,3008,3009,3010,3011,3012,3013], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[106]):
            return 단계시작3(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 단계시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000002_QD__MAIN__4$')
        self.set_timer(timerId='5', seconds=5)
        self.set_skip(state=늑대생성)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 늑대생성(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 늑대생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2006,2007,2008,2009,2010], animationEffect=False)
        self.create_monster(spawnIds=[2099], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 성공대기(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 성공대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)
        if self.time_expired(timerId='2'):
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.move_npc(spawnId=1102, patrolName='MS2PatrolData_1102')
        self.set_event_ui(type=7, arg2='$52000002_QD__MAIN__5$', arg3='3000', arg4='0')
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 포털생성(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1102, script='$52000002_QD__MAIN__6$', arg4=6)
        self.set_timer(timerId='30', seconds=30)
        self.show_guide_summary(entityId=25200203, textId=25200203)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            self.move_user(mapId=2000002, portalId=30, boxId=101)
            return 종료(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25200203)
        self.hide_guide_summary(entityId=25200202)
        self.destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
        self.destroy_monster(spawnIds=[2099])
        self.destroy_monster(spawnIds=[1099])
        self.destroy_monster(spawnIds=[1101])
        self.destroy_monster(spawnIds=[1102])
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000606], state=2)
        self.set_interact_object(triggerIds=[10000607,10000608,10000609,10000610,10000611], state=2)
        self.set_interact_object(triggerIds=[10000612,10000613,10000614,10000615,10000616], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
