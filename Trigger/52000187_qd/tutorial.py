""" trigger/52000187_qd/tutorial.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=0) # Invisible
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_widget(type='Guide')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90002]):
            return 환영(self.ctx)


class 환영(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_quest_accept(questId=90000008)
        self.side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[11000071], stateValue=0):
            self.side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__1$')
            self.set_quest_complete(questId=90000008)
            return 머쉬킹대화1(self.ctx)


class 머쉬킹대화1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2000], visible=False, arg3=0, delay=0, scale=0) # Invisible
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[1]):
            return 머쉬킹대화2(self.ctx)
        if self.quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[2]):
            return 머쉬킹대화2(self.ctx)
        if self.quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[3]):
            return 머쉬킹대화2(self.ctx)


class 머쉬킹대화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2001], visible=False, arg3=0, delay=0, scale=0) # Invisible

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90003]):
            self.side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__2$')
            self.move_npc(spawnId=103, patrolName='MS2PatrolData_lazy_1')
            return 머쉬킹대화3(self.ctx)


class 머쉬킹대화3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90004]):
            self.side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__3$')
            return 머쉬킹대화4(self.ctx)


class 머쉬킹대화4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90005]):
            return 모쿰소환(self.ctx)


class 모쿰소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 모쿰이동(self.ctx)


class 모쿰이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_mokum_0')
        self.add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__5$')
        self.side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__6$')
        self.add_buff(boxIds=[99999], skillId=71000077, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='Guide', name='IsTriggerEvent', condition='551'):
            # 가이드 To 트리거 -: 몬스터생성신호
            self.create_monster(spawnIds=[101], animationEffect=False)
            return 모쿰대사1(self.ctx)


class 모쿰대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_mokum_1')
        self.add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__7$')
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 해제(self.ctx)
        if self.wait_tick(waitTick=3000):
            return 모쿰대사2(self.ctx)


class 모쿰대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 해제(self.ctx)
        if self.wait_tick(waitTick=3000):
            return 모쿰대사2(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_mokum_2')
        self.guide_event(eventId=560)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[3]):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
