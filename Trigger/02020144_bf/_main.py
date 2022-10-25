""" trigger/02020144_bf/_main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=1003, skillId=70002151, isPlayer=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1002]):
            return 보스전_시작(self.ctx)


class 보스전_시작(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__0$', duration=5670, voice='ko/Npc/00002206')
        self.create_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5670):
            return 조건추가(self.ctx)


class 조건추가(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 보스전_성공(self.ctx)


class 보스전_성공(common.Trigger):
    def on_enter(self):
        self.set_achievement(type='trigger', achieve='ClearGreenLapenta_Quest')
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__1$', duration=7940, voice='ko/Npc/00002207')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7940):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        # <action name="업적이벤트를발생시킨다" arg2="trigger" arg3="ClearGreenLapenta"/>


initial_state = 대기
