""" trigger/52100002_qd/summon.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SummonSister', value=1):
            return 룸체크(self.ctx)


class 룸체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.is_dungeon_room():
            return 소환(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트소환(self.ctx)


class 소환(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=300, enable=True)
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.set_effect(triggerIds=[602], visible=True)
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__SUMMON__0$', align='left', duration=2000)
        self.set_skip(state=죽음대기)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.reset_camera(interpolationTime=1)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 죽음대기(self.ctx)


class 퀘스트소환(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=300, enable=True)
        self.create_monster(spawnIds=[2102], animationEffect=False)
        self.set_effect(triggerIds=[602], visible=True)
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__SUMMON__0$', align='left', duration=2000)
        self.set_skip(state=퀘스트죽음대기)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.reset_camera(interpolationTime=1)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 퀘스트죽음대기(self.ctx)


class 퀘스트죽음대기(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2101]):
            return 퀘스트셀린사망(self.ctx)
        if self.monster_dead(boxIds=[2102]):
            return 퀘스트피리스사망(self.ctx)


class 퀘스트셀린사망(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2102, script='$02000392_BF__SUMMON__1$', arg4=4, arg5=0)
        self.add_buff(boxIds=[2102], skillId=40442003, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 퀘스트피리스사망(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.set_conversation(type=1, spawnId=2101, script='$02000392_BF__SUMMON__2$', arg4=4, arg5=0)
        self.add_buff(boxIds=[2101], skillId=40442003, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 죽음대기(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 셀린사망(self.ctx)
        if self.monster_dead(boxIds=[2002]):
            return 피리스사망(self.ctx)


class 셀린사망(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2002, script='$02000392_BF__SUMMON__1$', arg4=4, arg5=0)
        self.add_buff(boxIds=[2002], skillId=40442003, level=1, isPlayer=True, isSkillSet=False)

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
        self.set_conversation(type=1, spawnId=2001, script='$02000392_BF__SUMMON__2$', arg4=4, arg5=0)
        self.add_buff(boxIds=[2001], skillId=40442003, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            self.set_achievement(triggerId=199, type='trigger', achieve='SirenDualKill')
            return 종료(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
