""" trigger/02020311_bf/sidetalk.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Sidetalk', value=1):
            self.side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$02020311_BF__SIDETALK__0$', duration=3000)
            return 세번째(self.ctx)


class 세번째(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Sidetalk', value=2):
            self.side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$02020311_BF__SIDETALK__1$', duration=3000)
            return 네번째(self.ctx)


class 네번째(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Sidetalk', value=3):
            self.side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$02020311_BF__SIDETALK__2$', duration=3000)
            return 대사대기(self.ctx)


class 대사대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 계속(self.ctx)


class 계속(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[101]):
            self.side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$02020311_BF__SIDETALK__3$', duration=3000)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
