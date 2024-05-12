""" trigger/02020019_bf/02020019_5phase.xml """
import trigger_api


# <5페이즈 크림슨 발록의 AI 너프버전으로 시작>
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='5Phase', value=1):
            return 크림슨발록스폰체크(self.ctx)


class 크림슨발록스폰체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[241], skillId=49218001, level=1, isPlayer=True)
        # <한국용 공격력 1.2배 강화 버프>
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[242], skillId=49218001, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[243], skillId=49218001, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[244], skillId=49218001, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[245], skillId=49218001, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[246], skillId=49218001, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_01', boxIds=[247], skillId=49218001, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[241], skillId=49218002, level=1, isPlayer=True)
        # <중국용 공격력 2배 강화 버프>
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[242], skillId=49218002, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[243], skillId=49218002, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[244], skillId=49218002, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[245], skillId=49218002, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[246], skillId=49218002, level=1, isPlayer=True)
        self.add_buff(feature='FameChallengeBuff_02', boxIds=[247], skillId=49218002, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[242]):
            return 크림슨스피어죽음(self.ctx)


class 크림슨스피어죽음(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[241]):
            return 발록에게신호쏴주기(self.ctx)


class 발록에게신호쏴주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='SpearDead', value=1)


initial_state = 대기
