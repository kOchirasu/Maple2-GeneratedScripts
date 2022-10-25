""" trigger/02000252_bf/elite_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8902], visible=False) # 가이드 화살표
        self.set_effect(triggerIds=[605], visible=False) # 벨라 음성
        self.set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=True)
        self.set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=904, boxId=1):
            return 딜레이(self.ctx)


class 대기2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=True)
        self.set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=904, boxId=1):
            return 딜레이2(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라(self.ctx)


class 딜레이2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라2(self.ctx)


class 벨라(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사(self.ctx)


class 벨라2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사2(self.ctx)


class 벨라대사(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_conversation(type=1, spawnId=1003, script='$02000252_BF__ELITE_02__0$', arg4=2)
        self.set_scene_skip(state=이동, action='nextState')
        # action name="스킵을설정한다" arg1="이동" /

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라스킬(self.ctx)


class 벨라대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_conversation(type=1, spawnId=1003, script='$02000252_BF__ELITE_02__1$', arg4=2)
        self.set_scene_skip(state=이동, action='nextState')
        # action name="스킵을설정한다" arg1="이동" /

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라스킬2(self.ctx)


class 벨라스킬(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_4')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 이동(self.ctx)


class 벨라스킬2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_scene_skip()
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_4')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 이동2(self.ctx)


class 이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9998" arg3="904" arg4="1" />
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)
        self.create_monster(spawnIds=[1109], animationEffect=False)
        self.create_monster(spawnIds=[1110], animationEffect=False)
        self.set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라삭제(self.ctx)


class 이동2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9998" arg3="904" arg4="1" />
        self.set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라삭제(self.ctx)


class 벨라삭제(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1003])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[202]):
            return 개봉(self.ctx)


class 개봉(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8902], visible=True) # 가이드 화살표
        self.set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=False)
        self.set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)


initial_state = 대기
