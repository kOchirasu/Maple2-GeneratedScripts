""" trigger/02000432_bf/summon.xml """
import common


class 룸체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.is_dungeon_room():
            return 소환(self.ctx)


class 소환(common.Trigger):
    def on_enter(self):
        self.set_skip(state=죽음대기)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 죽음대기(self.ctx)


class 죽음대기(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 셀린사망(self.ctx)
        if self.monster_dead(boxIds=[2002]):
            return 피리스사망(self.ctx)


class 셀린사망(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2002, script='$02000432_BF__SUMMON__1$', arg4=4, arg5=0)
        self.add_buff(boxIds=[2002], skillId=40500011, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2002]):
            self.set_achievement(triggerId=199, type='trigger', achieve='SirenDualKill')
            return 종료(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 피리스사망(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.set_achievement(triggerId=199, type='trigger', achieve='BigSisterFirst')
        self.set_conversation(type=1, spawnId=2001, script='$02000432_BF__SUMMON__0$', arg4=4, arg5=0)
        self.add_buff(boxIds=[2001], skillId=40500011, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            self.set_achievement(triggerId=199, type='trigger', achieve='SirenDualKill')
            return 종료(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 룸체크
