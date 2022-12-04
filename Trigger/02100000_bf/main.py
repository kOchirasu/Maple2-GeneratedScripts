""" trigger/02100000_bf/main.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return CheckUser10_GuildRaid(self.ctx)


class CheckUser10_GuildRaid(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1, interval=0, vOffset=0) # 최대 30초 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.count_users(boxId=101, boxId=10, operator='Less'):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Wait(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timerId='1'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(waitTick=6000):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Start(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=904, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100000_BF__MAIN__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ShowCaption02(self.ctx)


class ShowCaption02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100000_BF__MAIN__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(trigger_api.Trigger):
    def on_enter(self):
        self.close_cinematic()
        self.select_camera(triggerId=904, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000133, level=1, isPlayer=False, isSkillSet=False)
        self.add_buff(boxIds=[101], skillId=70000133, level=1, isPlayer=False, isSkillSet=True)
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_mesh(triggerIds=[80000], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[910001], enable=True)
        self.set_skill(triggerIds=[910002], enable=True)
        self.set_skill(triggerIds=[910003], enable=True)
        self.set_skill(triggerIds=[910004], enable=True)
        self.set_skill(triggerIds=[910005], enable=True)
        self.set_skill(triggerIds=[910006], enable=True)
        self.set_skill(triggerIds=[910007], enable=True)
        self.set_skill(triggerIds=[910008], enable=True)
        self.set_skill(triggerIds=[910009], enable=True)
        self.set_skill(triggerIds=[910010], enable=True)
        self.set_skill(triggerIds=[910011], enable=True)
        self.set_skill(triggerIds=[910012], enable=True)
        self.set_skill(triggerIds=[910013], enable=True)
        self.set_skill(triggerIds=[910014], enable=True)
        self.set_skill(triggerIds=[910015], enable=True)
        self.set_skill(triggerIds=[910016], enable=True)
        self.set_skill(triggerIds=[910017], enable=True)
        self.set_skill(triggerIds=[910018], enable=True)
        self.set_skill(triggerIds=[910019], enable=True)
        self.set_skill(triggerIds=[910020], enable=True)
        self.set_skill(triggerIds=[920001], enable=True)
        self.set_skill(triggerIds=[920002], enable=True)
        self.set_skill(triggerIds=[920003], enable=True)
        self.set_skill(triggerIds=[920004], enable=True)
        self.set_skill(triggerIds=[920005], enable=True)
        self.set_skill(triggerIds=[920006], enable=True)
        self.set_skill(triggerIds=[920007], enable=True)
        self.set_skill(triggerIds=[920008], enable=True)
        self.set_skill(triggerIds=[920009], enable=True)
        self.set_skill(triggerIds=[920010], enable=True)
        self.set_skill(triggerIds=[920011], enable=True)
        self.set_skill(triggerIds=[920012], enable=True)
        self.set_skill(triggerIds=[920013], enable=True)
        self.set_skill(triggerIds=[920014], enable=True)
        self.set_skill(triggerIds=[920015], enable=True)
        self.set_skill(triggerIds=[930001], enable=True)
        self.set_skill(triggerIds=[930002], enable=True)
        self.set_skill(triggerIds=[930003], enable=True)
        self.set_skill(triggerIds=[930004], enable=True)
        self.set_skill(triggerIds=[930005], enable=True)
        self.set_skill(triggerIds=[930006], enable=True)
        self.set_skill(triggerIds=[930007], enable=True)
        self.set_skill(triggerIds=[930008], enable=True)
        self.set_skill(triggerIds=[930009], enable=True)
        self.set_skill(triggerIds=[930010], enable=True)
        self.set_skill(triggerIds=[930011], enable=True)
        self.set_skill(triggerIds=[930012], enable=True)
        self.set_skill(triggerIds=[930013], enable=True)
        self.set_skill(triggerIds=[930014], enable=True)
        self.set_skill(triggerIds=[930015], enable=True)
        self.set_skill(triggerIds=[930016], enable=True)
        self.set_skill(triggerIds=[940001], enable=True)
        self.set_skill(triggerIds=[940002], enable=True)
        self.set_skill(triggerIds=[940003], enable=True)
        self.set_skill(triggerIds=[940004], enable=True)
        self.set_skill(triggerIds=[940005], enable=True)
        self.set_skill(triggerIds=[940006], enable=True)
        self.set_skill(triggerIds=[940007], enable=True)
        self.set_skill(triggerIds=[940008], enable=True)
        self.set_skill(triggerIds=[940009], enable=True)
        self.set_skill(triggerIds=[940010], enable=True)
        self.set_skill(triggerIds=[940011], enable=True)
        self.set_skill(triggerIds=[940012], enable=True)
        self.set_skill(triggerIds=[940013], enable=True)
        self.set_skill(triggerIds=[940014], enable=True)
        self.set_skill(triggerIds=[940015], enable=True)
        self.set_skill(triggerIds=[940016], enable=True)
        self.set_skill(triggerIds=[940017], enable=True)
        self.set_skill(triggerIds=[940018], enable=True)
        self.set_skill(triggerIds=[940019], enable=True)
        self.set_skill(triggerIds=[940020], enable=True)
        self.set_skill(triggerIds=[940021], enable=True)
        self.set_skill(triggerIds=[940022], enable=True)
        self.set_skill(triggerIds=[940023], enable=True)
        self.set_skill(triggerIds=[940024], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프_2(self.ctx)


class 버프_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02100000_BF__MAIN__2$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 바리케이트(self.ctx)


class 바리케이트(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02100000_BF__MAIN__3$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 닫기(self.ctx)


class 닫기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8001], visible=True)
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_effect(triggerIds=[8003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = Wait
