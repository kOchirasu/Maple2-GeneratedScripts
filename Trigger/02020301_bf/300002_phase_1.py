""" trigger/02020301_bf/300002_phase_1.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='AI_Phase', value=1):
            return 텍스트_대기(self.ctx)


class 텍스트_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 패이즈_1_시작(self.ctx)


class 패이즈_1_시작(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='AI_Phase', value=0)
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300002_PHASE_1__0$', duration=4176)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 대기
