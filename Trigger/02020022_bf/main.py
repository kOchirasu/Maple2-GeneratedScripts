""" trigger/02020022_bf/main.xml """
import common


class 전투시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201])


class 시작(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=23200086, illustId='Neirin_normal', msg='$02020022_BF__main__0$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=23200086, illustId='Neirin_normal', msg='$02020022_BF__main__1$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=23200086, illustId='Neirin_normal', msg='$02020022_BF__main__2$', duration=5000, align='left')


class 종료(common.Trigger):
    pass


initial_state = 전투시작
