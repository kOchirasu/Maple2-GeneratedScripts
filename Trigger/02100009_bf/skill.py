""" trigger/02100009_bf/skill.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=100, key='Fencebreak', value=0)
        self.set_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[1000001], enable=True)
        self.set_skill(triggerIds=[1000002], enable=True)
        self.set_skill(triggerIds=[1000003], enable=True)
        self.set_skill(triggerIds=[1000004], enable=True)
        self.set_skill(triggerIds=[1000005], enable=True)
        self.set_skill(triggerIds=[1000006], enable=True)
        self.set_skill(triggerIds=[1000007], enable=True)
        self.set_skill(triggerIds=[1000008], enable=True)
        self.set_skill(triggerIds=[1000008], enable=True)
        self.set_skill(triggerIds=[1000008], enable=True)
        self.set_skill(triggerIds=[1000008], enable=True)
        self.set_skill(triggerIds=[1000008], enable=True)
        self.set_skill(triggerIds=[1000009], enable=True)
        self.set_skill(triggerIds=[1000010], enable=True)
        self.set_skill(triggerIds=[1000011], enable=True)
        self.set_skill(triggerIds=[1000012], enable=True)
        self.set_skill(triggerIds=[1000013], enable=True)
        self.set_skill(triggerIds=[1000014], enable=True)
        self.set_skill(triggerIds=[1000015], enable=True)
        self.set_skill(triggerIds=[1000016], enable=True)
        self.set_skill(triggerIds=[1000017], enable=True)
        self.set_skill(triggerIds=[1000018], enable=True)
        self.set_skill(triggerIds=[1000019], enable=True)
        self.set_skill(triggerIds=[1000020], enable=True)
        self.set_skill(triggerIds=[1000021], enable=True)
        self.set_skill(triggerIds=[1000022], enable=True)
        self.set_skill(triggerIds=[1000023], enable=True)
        self.set_skill(triggerIds=[1000024], enable=True)
        self.set_skill(triggerIds=[1000025], enable=True)
        self.set_skill(triggerIds=[1000026], enable=True)
        self.set_skill(triggerIds=[1000027], enable=True)
        self.set_skill(triggerIds=[1000028], enable=True)
        self.set_skill(triggerIds=[1000029], enable=True)
        self.set_skill(triggerIds=[1000030], enable=True)
        self.set_skill(triggerIds=[1000031], enable=True)
        self.set_skill(triggerIds=[1000032], enable=True)
        self.set_skill(triggerIds=[1000033], enable=True)
        self.set_skill(triggerIds=[1000034], enable=True)
        self.set_skill(triggerIds=[1000035], enable=True)
        self.set_skill(triggerIds=[1000036], enable=True)
        self.set_skill(triggerIds=[1000037], enable=True)
        self.set_skill(triggerIds=[1000038], enable=True)
        self.set_skill(triggerIds=[1000039], enable=True)
        self.set_skill(triggerIds=[1000040], enable=True)
        self.set_skill(triggerIds=[1000041], enable=True)
        self.set_skill(triggerIds=[1000042], enable=True)
        self.set_skill(triggerIds=[1000043], enable=True)
        self.set_skill(triggerIds=[1000044], enable=True)
        self.set_skill(triggerIds=[1000045], enable=True)
        self.set_skill(triggerIds=[1000046], enable=True)
        self.set_skill(triggerIds=[1000047], enable=True)
        self.set_skill(triggerIds=[1000048], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 스킬사용(self.ctx)


class 스킬사용(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FenceBreak', value=1):
            return 길막삭제(self.ctx)


class 길막삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[1000001], enable=False)
        self.set_skill(triggerIds=[1000002], enable=False)
        self.set_skill(triggerIds=[1000003], enable=False)
        self.set_skill(triggerIds=[1000004], enable=False)
        self.set_skill(triggerIds=[1000005], enable=False)
        self.set_skill(triggerIds=[1000006], enable=False)
        self.set_skill(triggerIds=[1000007], enable=False)
        self.set_skill(triggerIds=[1000008], enable=False)
        self.set_skill(triggerIds=[1000008], enable=False)
        self.set_skill(triggerIds=[1000008], enable=False)
        self.set_skill(triggerIds=[1000008], enable=False)
        self.set_skill(triggerIds=[1000008], enable=False)
        self.set_skill(triggerIds=[1000009], enable=False)
        self.set_skill(triggerIds=[1000010], enable=False)
        self.set_skill(triggerIds=[1000011], enable=False)
        self.set_skill(triggerIds=[1000012], enable=False)
        self.set_skill(triggerIds=[1000013], enable=False)
        self.set_skill(triggerIds=[1000014], enable=False)
        self.set_skill(triggerIds=[1000015], enable=False)
        self.set_skill(triggerIds=[1000016], enable=False)
        self.set_skill(triggerIds=[1000017], enable=False)
        self.set_skill(triggerIds=[1000018], enable=False)
        self.set_skill(triggerIds=[1000019], enable=False)
        self.set_skill(triggerIds=[1000020], enable=False)
        self.set_skill(triggerIds=[1000021], enable=False)
        self.set_skill(triggerIds=[1000022], enable=False)
        self.set_skill(triggerIds=[1000023], enable=False)
        self.set_skill(triggerIds=[1000024], enable=False)
        self.set_skill(triggerIds=[1000025], enable=False)
        self.set_skill(triggerIds=[1000026], enable=False)
        self.set_skill(triggerIds=[1000027], enable=False)
        self.set_skill(triggerIds=[1000028], enable=False)
        self.set_skill(triggerIds=[1000029], enable=False)
        self.set_skill(triggerIds=[1000030], enable=False)
        self.set_skill(triggerIds=[1000031], enable=False)
        self.set_skill(triggerIds=[1000032], enable=False)
        self.set_skill(triggerIds=[1000033], enable=False)
        self.set_skill(triggerIds=[1000034], enable=False)
        self.set_skill(triggerIds=[1000035], enable=False)
        self.set_skill(triggerIds=[1000036], enable=False)
        self.set_skill(triggerIds=[1000037], enable=False)
        self.set_skill(triggerIds=[1000038], enable=False)
        self.set_skill(triggerIds=[1000039], enable=False)
        self.set_skill(triggerIds=[1000040], enable=False)
        self.set_skill(triggerIds=[1000041], enable=False)
        self.set_skill(triggerIds=[1000042], enable=False)
        self.set_skill(triggerIds=[1000043], enable=False)
        self.set_skill(triggerIds=[1000044], enable=False)
        self.set_skill(triggerIds=[1000045], enable=False)
        self.set_skill(triggerIds=[1000046], enable=False)
        self.set_skill(triggerIds=[1000047], enable=False)
        self.set_skill(triggerIds=[1000048], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return None # Missing State: 끝1


initial_state = 대기
