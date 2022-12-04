""" trigger/02020024_bf/main.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101])


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=23200084, illustId='Neirin_normal', msg='$02020024_BF__main__0$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=23200084, illustId='Neirin_normal', msg='$02020024_BF__main__1$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=23200084, illustId='Neirin_normal', msg='$02020024_BF__main__2$', duration=5000, align='left')


class 종료(trigger_api.Trigger):
    pass


initial_state = 전투시작
