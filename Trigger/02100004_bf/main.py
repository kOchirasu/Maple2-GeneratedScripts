""" trigger/02100004_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return CheckUser10_GuildRaid(self.ctx)


class CheckUser10_GuildRaid(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=30, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=199, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.count_users(boxId=199, boxId=10, operator='Less'):
            return MaxCount10_Wait(self.ctx)
        if not self.is_dungeon_room():
            return MaxCount10_Start(self.ctx)


class MaxCount10_Wait(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=199, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timerId='99'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(waitTick=6000):
            return MaxCount10_Wait(self.ctx)
        if not self.is_dungeon_room():
            return MaxCount10_Start(self.ctx)


class MaxCount10_Start(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='99')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return DungeonStart(self.ctx)


# 설명문 출력
class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100004_BF__MAIN__0$')
        self.set_skip(state=Caption01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return Caption01Skip(self.ctx)


class Caption01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0)
        self.close_cinematic()
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[601], visible=True)
        self.show_guide_summary(entityId=20002411, textId=20002411)
        self.set_user_value(triggerId=999993, key='BattleStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 라운드시작1(self.ctx)


class 라운드시작1(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002411)
        self.show_count_ui(text='$02100004_BF__MAIN__1$', stage=0, count=3)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드1(self.ctx)


class 라운드1(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='1,10')
        self.set_timer(timerId='1', seconds=20, startDelay=1, interval=1)

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작2(self.ctx)
        if self.time_expired(timerId='1'):
            return 라운드시작2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 라운드시작2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__2$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드2(self.ctx)


class 라운드2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='2', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='2,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작3(self.ctx)
        if self.time_expired(timerId='2'):
            return 라운드시작3(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='2')


class 라운드시작3(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__3$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드3(self.ctx)


class 라운드3(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='3', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='3,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작4(self.ctx)
        if self.time_expired(timerId='3'):
            return 라운드시작4(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='3')


class 라운드시작4(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__4$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드4(self.ctx)


class 라운드4(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='4', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='4,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작5(self.ctx)
        if self.time_expired(timerId='4'):
            return 라운드시작5(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='4')


class 라운드시작5(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__5$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드5(self.ctx)


class 라운드5(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='5', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='5,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작6(self.ctx)
        if self.time_expired(timerId='5'):
            return 라운드시작6(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='5')


class 라운드시작6(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__6$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드6(self.ctx)


class 라운드6(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='6', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='6,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작7(self.ctx)
        if self.time_expired(timerId='6'):
            return 라운드시작7(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='6')


class 라운드시작7(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__7$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드7(self.ctx)


class 라운드7(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='7', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='7,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작8(self.ctx)
        if self.time_expired(timerId='7'):
            return 라운드시작8(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='7')


class 라운드시작8(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__8$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드8(self.ctx)


class 라운드8(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='8', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='8,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작9(self.ctx)
        if self.time_expired(timerId='8'):
            return 라운드시작9(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='8')


class 라운드시작9(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_user_value(triggerId=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__9$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드9(self.ctx)


class 라운드9(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='9', seconds=20, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='9,10')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작10(self.ctx)
        if self.time_expired(timerId='9'):
            return 라운드시작10(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='9')


class 라운드시작10(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.create_monster(spawnIds=[2000], animationEffect=True)
        self.show_count_ui(text='$02100004_BF__MAIN__10$', stage=0, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드10(self.ctx)


class 라운드10(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_timer(timerId='10', seconds=150, startDelay=1, interval=1)
        self.move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        self.set_event_ui(type=0, arg2='10,10')
        self.set_user_value(triggerId=999995, key='LastRoundStart', value=1) # 트로피 전용

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000]):
            self.reset_timer(timerId='10')
            return 성공(self.ctx)
        if self.time_expired(timerId='10'):
            return 실패(self.ctx)

    def on_exit(self):
        self.set_event_ui(type=0, arg2='0,0')
        self.set_user_value(triggerId=999995, key='LastRoundEnd', value=1) # 트로피 전용


class 성공(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999993, key='BattleEnd', value=1)
        self.destroy_monster(spawnIds=[-1])
        self.set_achievement(triggerId=9900, type='trigger', achieve='Find02100004')
        self.set_event_ui(type=7, arg2='$02000251_BF__TRIGGER_01_01__0$', arg3='2000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 실패(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=5, arg2='$02100004_BF__MAIN__11$', arg3='2000', arg4='0')
        self.set_user_value(triggerId=999993, key='BattleEnd', value=1)
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
