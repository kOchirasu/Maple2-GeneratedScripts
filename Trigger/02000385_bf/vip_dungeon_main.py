""" trigger/02000385_bf/vip_dungeon_main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[601,602,603], visible=False)
        self.move_user(mapId=2000385, portalId=1)
        self.set_interact_object(triggerIds=[10001083], state=1)
        self.set_interact_object(triggerIds=[10001084], state=1)
        self.set_interact_object(triggerIds=[10001085], state=1)
        self.select_camera(triggerId=299, enable=True)
        # self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 이벤트시작(self.ctx)


class 이벤트시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.select_camera(triggerId=300, enable=True)
            self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return 캐릭터선택대기(self.ctx)


class 캐릭터선택대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=20003851, textId=20003851)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001083], stateValue=0):
            return 천둥선택(self.ctx)
        if self.object_interacted(interactIds=[10001084], stateValue=0):
            return 알론선택(self.ctx)
        if self.object_interacted(interactIds=[10001085], stateValue=0):
            return 오스칼선택(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20003851)
        self.move_user(mapId=2000385, portalId=2)


class 천둥선택(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.add_buff(boxIds=[199], skillId=99910090, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=311, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 게임준비(self.ctx)


class 알론선택(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[602], visible=True)
        self.add_buff(boxIds=[199], skillId=99910100, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=312, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 게임준비(self.ctx)


class 오스칼선택(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[603], visible=True)
        self.add_buff(boxIds=[199], skillId=99910110, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=313, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 게임준비(self.ctx)


class 게임준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_UI_Start_01')
        self.create_widget(type='ScoreBoard')
        # 스코어 창 열기  arg3는 위치 (1:중앙:다크스트림, 2:우상단:아케이드)
        self.widget_action(type='ScoreBoard', func='OpenBoard', widgetArg='1')
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 게임시작(self.ctx)


class 게임시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='ScoreBoard', func='SetScore', widgetArg='0', desc='점수 강제 설정')
        # self.widget_action(type='ScoreBoard', func='AddScore', widgetArg='10', desc='점수 강제 추가')
        self.show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__0$', stage=1, count=3)
        self.set_event_ui(type=0, arg2='1,5')
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작1(self.ctx)


class 라운드시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9991001, key='round1start', value=1)
        self.set_timer(timerId='30', seconds=30, startDelay=0, interval=1, vOffset=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 라운드종료1(self.ctx)


class 라운드종료1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__1$', stage=2, count=3)
        self.set_event_ui(type=0, arg2='2,5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작2(self.ctx)


class 라운드시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9991001, key='round2start', value=1)
        self.set_timer(timerId='30', seconds=30, startDelay=0, interval=1, vOffset=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 라운드종료2(self.ctx)


class 라운드종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__2$', stage=3, count=3)
        self.set_event_ui(type=0, arg2='3,5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작3(self.ctx)


class 라운드시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9991001, key='round3start', value=1)
        self.set_timer(timerId='30', seconds=30, startDelay=0, interval=1, vOffset=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 라운드종료3(self.ctx)


class 라운드종료3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__3$', stage=4, count=3)
        self.set_event_ui(type=0, arg2='4,5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작4(self.ctx)


class 라운드시작4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9991001, key='round4start', value=1)
        self.set_timer(timerId='30', seconds=30, startDelay=0, interval=1, vOffset=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 라운드종료4(self.ctx)


class 라운드종료4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__4$', stage=5, count=3)
        self.set_event_ui(type=0, arg2='5,5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작5(self.ctx)


class 라운드시작5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9991001, key='round5start', value=1)
        self.set_timer(timerId='30', seconds=30, startDelay=0, interval=1, vOffset=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 게임종료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=301, enable=True)
        self.set_event_ui(type=0, arg2='0,0')
        self.move_user(mapId=2000385, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 정산(self.ctx)


class 정산(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[0])
        self.widget_action(type='ScoreBoard', func='CloseBoard')
        self.remove_buff(boxId=199, skillId=99910090)
        self.remove_buff(boxId=199, skillId=99910100)
        self.remove_buff(boxId=199, skillId=99910110)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='ScoreBoard', name='Compare', condition='>=,1500', desc='비교 연산 (연산자,대상값)'):
            self.debug_string(value='1500점 이상')
            return 보상(self.ctx)
        if self.widget_condition(type='ScoreBoard', name='Compare', condition='>=,1000', desc='비교 연산 (연산자,대상값)'):
            self.debug_string(value='1000점 이상')
            return 보상(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 보상(self.ctx)


class 보상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
