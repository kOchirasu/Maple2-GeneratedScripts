""" trigger/02020028_bf/main.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201])


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=24120001, illustId='Neirin_normal', msg='$02020028_BF__main__0$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=24120001, illustId='Neirin_normal', msg='$02020028_BF__main__1$', duration=5000, align='left')


initial_state = 전투시작
