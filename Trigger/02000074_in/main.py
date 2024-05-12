""" trigger/02000074_in/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4000], visible=False)
        self.destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001592], questStates=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001592], questStates=[2]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001592], questStates=[1]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001591], questStates=[3]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001591], questStates=[2]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001589], questStates=[2]):
            return 케이틀린스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001589], questStates=[1]):
            return 케이틀린스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001588], questStates=[3]):
            return 케이틀린스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001588], questStates=[2]): # 
            return 케이틀린스폰(self.ctx)


class 케이틀린스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False) # 연출용 어둠의 세력 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return start(self.ctx)


class 쪽지스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_mesh(triggerIds=[4000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return start(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
