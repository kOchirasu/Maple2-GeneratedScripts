""" trigger/02000253_bf/start.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=True)
        self.set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=False)
        self.set_effect(triggerIds=[8013], visible=False)
        self.set_effect(triggerIds=[8014], visible=False)
        self.set_effect(triggerIds=[8015], visible=False)
        self.set_effect(triggerIds=[8016], visible=False)
        self.set_effect(triggerIds=[8017], visible=False)
        self.set_effect(triggerIds=[8018], visible=False)
        self.set_effect(triggerIds=[8019], visible=False)
        self.set_effect(triggerIds=[8020], visible=False)
        self.set_effect(triggerIds=[8021], visible=False)
        self.set_effect(triggerIds=[8022], visible=False)
        self.set_effect(triggerIds=[8023], visible=False)
        self.set_effect(triggerIds=[8024], visible=False)
        self.set_effect(triggerIds=[8025], visible=False)
        self.set_effect(triggerIds=[8026], visible=False)
        self.set_effect(triggerIds=[8027], visible=False)
        self.set_effect(triggerIds=[8028], visible=False)
        self.set_effect(triggerIds=[8029], visible=False)
        self.set_effect(triggerIds=[8030], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=905, minUsers='1'):
            return 예고이펙트(self.ctx)


"""
class 벨라소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=2)
        self.create_monster(spawnIds=[1004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return None # Missing State: 벨라대사

"""


"""
class 벨라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.move_npc(spawnId=1004, patrolName='MS2PatrolData_5')
            return None # Missing State: 벨라스킬딜레이

"""


"""
class 벨라스킬딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 예고이펙트(self.ctx)

"""


class 예고이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_effect(triggerIds=[8013], visible=True)
        # self.set_effect(triggerIds=[8014], visible=True)
        # self.set_effect(triggerIds=[8015], visible=True)
        # self.set_effect(triggerIds=[8016], visible=True)
        # self.set_effect(triggerIds=[8017], visible=True)
        # self.set_effect(triggerIds=[8018], visible=True)
        # self.set_effect(triggerIds=[8019], visible=True)
        # self.set_effect(triggerIds=[8020], visible=True)
        # self.set_effect(triggerIds=[8021], visible=True)
        # self.set_effect(triggerIds=[8022], visible=True)
        # self.set_effect(triggerIds=[8023], visible=True)
        # self.set_effect(triggerIds=[8024], visible=True)
        # self.set_effect(triggerIds=[8025], visible=True)
        # self.set_effect(triggerIds=[8026], visible=True)
        # self.set_effect(triggerIds=[8027], visible=True)
        # self.set_effect(triggerIds=[8028], visible=True)
        # self.set_effect(triggerIds=[8029], visible=True)
        # self.set_effect(triggerIds=[8030], visible=True)
        self.create_monster(spawnIds=[4021], animationEffect=True)
        self.create_monster(spawnIds=[4022], animationEffect=True)
        self.create_monster(spawnIds=[4023], animationEffect=True)
        self.create_monster(spawnIds=[4024], animationEffect=True)
        self.create_monster(spawnIds=[4025], animationEffect=True)
        self.create_monster(spawnIds=[4026], animationEffect=True)
        self.create_monster(spawnIds=[4027], animationEffect=True)
        self.create_monster(spawnIds=[4028], animationEffect=True)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='5'):
            return 스킬시작대기(self.ctx)


class 스킬시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            # self.show_guide_summary(entityId=20002522, textId=20002522)
            self.set_effect(triggerIds=[8013], visible=False)
            self.set_effect(triggerIds=[8014], visible=False)
            self.set_effect(triggerIds=[8015], visible=False)
            self.set_effect(triggerIds=[8016], visible=False)
            self.set_effect(triggerIds=[8017], visible=False)
            self.set_effect(triggerIds=[8018], visible=False)
            self.set_effect(triggerIds=[8019], visible=False)
            self.set_effect(triggerIds=[8020], visible=False)
            self.set_effect(triggerIds=[8021], visible=False)
            self.set_effect(triggerIds=[8022], visible=False)
            self.set_effect(triggerIds=[8023], visible=False)
            self.set_effect(triggerIds=[8024], visible=False)
            self.set_effect(triggerIds=[8025], visible=False)
            self.set_effect(triggerIds=[8026], visible=False)
            self.set_effect(triggerIds=[8027], visible=False)
            self.set_effect(triggerIds=[8028], visible=False)
            self.set_effect(triggerIds=[8029], visible=False)
            self.set_effect(triggerIds=[8030], visible=False)
            return 스킬01(self.ctx)


class 스킬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=False)
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2301], enable=True)
        self.set_skill(triggerIds=[2302], enable=True)
        self.set_skill(triggerIds=[2303], enable=True)
        self.set_skill(triggerIds=[2304], enable=True)
        self.set_skill(triggerIds=[2305], enable=True)
        self.set_skill(triggerIds=[2306], enable=True)
        self.set_skill(triggerIds=[2307], enable=True)
        self.set_skill(triggerIds=[2308], enable=True)
        self.set_skill(triggerIds=[2309], enable=True)
        self.set_skill(triggerIds=[2310], enable=True)
        self.set_skill(triggerIds=[2311], enable=True)
        self.set_skill(triggerIds=[2312], enable=True)
        self.set_skill(triggerIds=[2313], enable=True)
        self.set_skill(triggerIds=[2314], enable=True)
        self.set_skill(triggerIds=[2315], enable=True)
        self.set_skill(triggerIds=[2316], enable=True)
        self.set_skill(triggerIds=[2317], enable=True)
        self.set_skill(triggerIds=[2318], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬02대기(self.ctx)


class 스킬02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1004])
        self.set_skill(triggerIds=[2301], enable=False)
        self.set_skill(triggerIds=[2302], enable=False)
        self.set_skill(triggerIds=[2303], enable=False)
        self.set_skill(triggerIds=[2304], enable=False)
        self.set_skill(triggerIds=[2305], enable=False)
        self.set_skill(triggerIds=[2306], enable=False)
        self.set_skill(triggerIds=[2307], enable=False)
        self.set_skill(triggerIds=[2308], enable=False)
        self.set_skill(triggerIds=[2309], enable=False)
        self.set_skill(triggerIds=[2310], enable=False)
        self.set_skill(triggerIds=[2311], enable=False)
        self.set_skill(triggerIds=[2312], enable=False)
        self.set_skill(triggerIds=[2313], enable=False)
        self.set_skill(triggerIds=[2314], enable=False)
        self.set_skill(triggerIds=[2315], enable=False)
        self.set_skill(triggerIds=[2316], enable=False)
        self.set_skill(triggerIds=[2317], enable=False)
        self.set_skill(triggerIds=[2318], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬02(self.ctx)


class 스킬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2307], enable=True)
        self.set_skill(triggerIds=[2308], enable=True)
        self.set_skill(triggerIds=[2309], enable=True)
        self.set_skill(triggerIds=[2310], enable=True)
        self.set_skill(triggerIds=[2311], enable=True)
        self.set_skill(triggerIds=[2312], enable=True)
        self.set_skill(triggerIds=[2313], enable=True)
        self.set_skill(triggerIds=[2314], enable=True)
        self.set_skill(triggerIds=[2315], enable=True)
        self.set_skill(triggerIds=[2316], enable=True)
        self.set_skill(triggerIds=[2317], enable=True)
        self.set_skill(triggerIds=[2318], enable=True)
        self.set_skill(triggerIds=[2319], enable=True)
        self.set_skill(triggerIds=[2320], enable=True)
        self.set_skill(triggerIds=[2321], enable=True)
        self.set_skill(triggerIds=[2322], enable=True)
        self.set_skill(triggerIds=[2323], enable=True)
        self.set_skill(triggerIds=[2324], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬03대기(self.ctx)


class 스킬03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2307], enable=False)
        self.set_skill(triggerIds=[2308], enable=False)
        self.set_skill(triggerIds=[2309], enable=False)
        self.set_skill(triggerIds=[2310], enable=False)
        self.set_skill(triggerIds=[2311], enable=False)
        self.set_skill(triggerIds=[2312], enable=False)
        self.set_skill(triggerIds=[2313], enable=False)
        self.set_skill(triggerIds=[2314], enable=False)
        self.set_skill(triggerIds=[2315], enable=False)
        self.set_skill(triggerIds=[2316], enable=False)
        self.set_skill(triggerIds=[2317], enable=False)
        self.set_skill(triggerIds=[2318], enable=False)
        self.set_skill(triggerIds=[2319], enable=False)
        self.set_skill(triggerIds=[2320], enable=False)
        self.set_skill(triggerIds=[2321], enable=False)
        self.set_skill(triggerIds=[2322], enable=False)
        self.set_skill(triggerIds=[2323], enable=False)
        self.set_skill(triggerIds=[2324], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬03(self.ctx)


class 스킬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2313], enable=True)
        self.set_skill(triggerIds=[2314], enable=True)
        self.set_skill(triggerIds=[2315], enable=True)
        self.set_skill(triggerIds=[2316], enable=True)
        self.set_skill(triggerIds=[2317], enable=True)
        self.set_skill(triggerIds=[2318], enable=True)
        self.set_skill(triggerIds=[2319], enable=True)
        self.set_skill(triggerIds=[2320], enable=True)
        self.set_skill(triggerIds=[2321], enable=True)
        self.set_skill(triggerIds=[2322], enable=True)
        self.set_skill(triggerIds=[2323], enable=True)
        self.set_skill(triggerIds=[2324], enable=True)
        self.set_skill(triggerIds=[2325], enable=True)
        self.set_skill(triggerIds=[2326], enable=True)
        self.set_skill(triggerIds=[2327], enable=True)
        self.set_skill(triggerIds=[2328], enable=True)
        self.set_skill(triggerIds=[2329], enable=True)
        self.set_skill(triggerIds=[2330], enable=True)
        self.set_skill(triggerIds=[2331], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬04대기(self.ctx)


class 스킬04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2313], enable=False)
        self.set_skill(triggerIds=[2314], enable=False)
        self.set_skill(triggerIds=[2315], enable=False)
        self.set_skill(triggerIds=[2316], enable=False)
        self.set_skill(triggerIds=[2317], enable=False)
        self.set_skill(triggerIds=[2318], enable=False)
        self.set_skill(triggerIds=[2319], enable=False)
        self.set_skill(triggerIds=[2320], enable=False)
        self.set_skill(triggerIds=[2321], enable=False)
        self.set_skill(triggerIds=[2322], enable=False)
        self.set_skill(triggerIds=[2323], enable=False)
        self.set_skill(triggerIds=[2324], enable=False)
        self.set_skill(triggerIds=[2325], enable=False)
        self.set_skill(triggerIds=[2326], enable=False)
        self.set_skill(triggerIds=[2327], enable=False)
        self.set_skill(triggerIds=[2328], enable=False)
        self.set_skill(triggerIds=[2329], enable=False)
        self.set_skill(triggerIds=[2330], enable=False)
        self.set_skill(triggerIds=[2331], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬05(self.ctx)


class 스킬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2319], enable=True)
        self.set_skill(triggerIds=[2320], enable=True)
        self.set_skill(triggerIds=[2321], enable=True)
        self.set_skill(triggerIds=[2322], enable=True)
        self.set_skill(triggerIds=[2323], enable=True)
        self.set_skill(triggerIds=[2324], enable=True)
        self.set_skill(triggerIds=[2325], enable=True)
        self.set_skill(triggerIds=[2326], enable=True)
        self.set_skill(triggerIds=[2327], enable=True)
        self.set_skill(triggerIds=[2328], enable=True)
        self.set_skill(triggerIds=[2329], enable=True)
        self.set_skill(triggerIds=[2330], enable=True)
        self.set_skill(triggerIds=[2331], enable=True)
        self.set_skill(triggerIds=[2332], enable=True)
        self.set_skill(triggerIds=[2333], enable=True)
        self.set_skill(triggerIds=[2334], enable=True)
        self.set_skill(triggerIds=[2335], enable=True)
        self.set_skill(triggerIds=[2336], enable=True)
        self.set_skill(triggerIds=[2337], enable=True)
        self.set_skill(triggerIds=[2338], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬06대기(self.ctx)


class 스킬06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002522)
        self.set_skill(triggerIds=[2319], enable=False)
        self.set_skill(triggerIds=[2320], enable=False)
        self.set_skill(triggerIds=[2321], enable=False)
        self.set_skill(triggerIds=[2322], enable=False)
        self.set_skill(triggerIds=[2323], enable=False)
        self.set_skill(triggerIds=[2324], enable=False)
        self.set_skill(triggerIds=[2325], enable=False)
        self.set_skill(triggerIds=[2326], enable=False)
        self.set_skill(triggerIds=[2327], enable=False)
        self.set_skill(triggerIds=[2328], enable=False)
        self.set_skill(triggerIds=[2329], enable=False)
        self.set_skill(triggerIds=[2330], enable=False)
        self.set_skill(triggerIds=[2331], enable=False)
        self.set_skill(triggerIds=[2332], enable=False)
        self.set_skill(triggerIds=[2333], enable=False)
        self.set_skill(triggerIds=[2334], enable=False)
        self.set_skill(triggerIds=[2335], enable=False)
        self.set_skill(triggerIds=[2336], enable=False)
        self.set_skill(triggerIds=[2337], enable=False)
        self.set_skill(triggerIds=[2338], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬07(self.ctx)


class 스킬07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2325], enable=True)
        self.set_skill(triggerIds=[2326], enable=True)
        self.set_skill(triggerIds=[2327], enable=True)
        self.set_skill(triggerIds=[2328], enable=True)
        self.set_skill(triggerIds=[2329], enable=True)
        self.set_skill(triggerIds=[2330], enable=True)
        self.set_skill(triggerIds=[2331], enable=True)
        self.set_skill(triggerIds=[2332], enable=True)
        self.set_skill(triggerIds=[2333], enable=True)
        self.set_skill(triggerIds=[2334], enable=True)
        self.set_skill(triggerIds=[2335], enable=True)
        self.set_skill(triggerIds=[2336], enable=True)
        self.set_skill(triggerIds=[2337], enable=True)
        self.set_skill(triggerIds=[2338], enable=True)
        self.set_skill(triggerIds=[2339], enable=True)
        self.set_skill(triggerIds=[2340], enable=True)
        self.set_skill(triggerIds=[2341], enable=True)
        self.set_skill(triggerIds=[2342], enable=True)
        self.set_skill(triggerIds=[2343], enable=True)
        self.set_skill(triggerIds=[2344], enable=True)
        self.set_skill(triggerIds=[2345], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬08대기(self.ctx)


class 스킬08대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2325], enable=False)
        self.set_skill(triggerIds=[2326], enable=False)
        self.set_skill(triggerIds=[2327], enable=False)
        self.set_skill(triggerIds=[2328], enable=False)
        self.set_skill(triggerIds=[2329], enable=False)
        self.set_skill(triggerIds=[2330], enable=False)
        self.set_skill(triggerIds=[2331], enable=False)
        self.set_skill(triggerIds=[2332], enable=False)
        self.set_skill(triggerIds=[2333], enable=False)
        self.set_skill(triggerIds=[2334], enable=False)
        self.set_skill(triggerIds=[2335], enable=False)
        self.set_skill(triggerIds=[2336], enable=False)
        self.set_skill(triggerIds=[2337], enable=False)
        self.set_skill(triggerIds=[2338], enable=False)
        self.set_skill(triggerIds=[2339], enable=False)
        self.set_skill(triggerIds=[2340], enable=False)
        self.set_skill(triggerIds=[2341], enable=False)
        self.set_skill(triggerIds=[2342], enable=False)
        self.set_skill(triggerIds=[2343], enable=False)
        self.set_skill(triggerIds=[2344], enable=False)
        self.set_skill(triggerIds=[2345], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬08(self.ctx)


class 스킬08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2332], enable=True)
        self.set_skill(triggerIds=[2333], enable=True)
        self.set_skill(triggerIds=[2334], enable=True)
        self.set_skill(triggerIds=[2335], enable=True)
        self.set_skill(triggerIds=[2336], enable=True)
        self.set_skill(triggerIds=[2337], enable=True)
        self.set_skill(triggerIds=[2338], enable=True)
        self.set_skill(triggerIds=[2339], enable=True)
        self.set_skill(triggerIds=[2340], enable=True)
        self.set_skill(triggerIds=[2341], enable=True)
        self.set_skill(triggerIds=[2342], enable=True)
        self.set_skill(triggerIds=[2343], enable=True)
        self.set_skill(triggerIds=[2344], enable=True)
        self.set_skill(triggerIds=[2345], enable=True)
        self.set_skill(triggerIds=[2346], enable=True)
        self.set_skill(triggerIds=[2347], enable=True)
        self.set_skill(triggerIds=[2348], enable=True)
        self.set_skill(triggerIds=[2349], enable=True)
        self.set_skill(triggerIds=[2350], enable=True)
        self.set_skill(triggerIds=[2351], enable=True)
        self.set_skill(triggerIds=[2352], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬09대기(self.ctx)


class 스킬09대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2332], enable=False)
        self.set_skill(triggerIds=[2333], enable=False)
        self.set_skill(triggerIds=[2334], enable=False)
        self.set_skill(triggerIds=[2335], enable=False)
        self.set_skill(triggerIds=[2336], enable=False)
        self.set_skill(triggerIds=[2337], enable=False)
        self.set_skill(triggerIds=[2338], enable=False)
        self.set_skill(triggerIds=[2339], enable=False)
        self.set_skill(triggerIds=[2340], enable=False)
        self.set_skill(triggerIds=[2341], enable=False)
        self.set_skill(triggerIds=[2342], enable=False)
        self.set_skill(triggerIds=[2343], enable=False)
        self.set_skill(triggerIds=[2344], enable=False)
        self.set_skill(triggerIds=[2345], enable=False)
        self.set_skill(triggerIds=[2346], enable=False)
        self.set_skill(triggerIds=[2347], enable=False)
        self.set_skill(triggerIds=[2348], enable=False)
        self.set_skill(triggerIds=[2349], enable=False)
        self.set_skill(triggerIds=[2350], enable=False)
        self.set_skill(triggerIds=[2351], enable=False)
        self.set_skill(triggerIds=[2352], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬09(self.ctx)


class 스킬09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2339], enable=True)
        self.set_skill(triggerIds=[2340], enable=True)
        self.set_skill(triggerIds=[2341], enable=True)
        self.set_skill(triggerIds=[2342], enable=True)
        self.set_skill(triggerIds=[2343], enable=True)
        self.set_skill(triggerIds=[2344], enable=True)
        self.set_skill(triggerIds=[2345], enable=True)
        self.set_skill(triggerIds=[2346], enable=True)
        self.set_skill(triggerIds=[2347], enable=True)
        self.set_skill(triggerIds=[2348], enable=True)
        self.set_skill(triggerIds=[2349], enable=True)
        self.set_skill(triggerIds=[2350], enable=True)
        self.set_skill(triggerIds=[2351], enable=True)
        self.set_skill(triggerIds=[2352], enable=True)
        self.set_skill(triggerIds=[2353], enable=True)
        self.set_skill(triggerIds=[2354], enable=True)
        self.set_skill(triggerIds=[2355], enable=True)
        self.set_skill(triggerIds=[2356], enable=True)
        self.set_skill(triggerIds=[2357], enable=True)
        self.set_skill(triggerIds=[2358], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬10대기(self.ctx)


class 스킬10대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2339], enable=False)
        self.set_skill(triggerIds=[2340], enable=False)
        self.set_skill(triggerIds=[2341], enable=False)
        self.set_skill(triggerIds=[2342], enable=False)
        self.set_skill(triggerIds=[2343], enable=False)
        self.set_skill(triggerIds=[2344], enable=False)
        self.set_skill(triggerIds=[2345], enable=False)
        self.set_skill(triggerIds=[2346], enable=False)
        self.set_skill(triggerIds=[2347], enable=False)
        self.set_skill(triggerIds=[2348], enable=False)
        self.set_skill(triggerIds=[2349], enable=False)
        self.set_skill(triggerIds=[2350], enable=False)
        self.set_skill(triggerIds=[2351], enable=False)
        self.set_skill(triggerIds=[2352], enable=False)
        self.set_skill(triggerIds=[2353], enable=False)
        self.set_skill(triggerIds=[2354], enable=False)
        self.set_skill(triggerIds=[2355], enable=False)
        self.set_skill(triggerIds=[2356], enable=False)
        self.set_skill(triggerIds=[2357], enable=False)
        self.set_skill(triggerIds=[2358], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬10(self.ctx)


class 스킬10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2346], enable=True)
        self.set_skill(triggerIds=[2347], enable=True)
        self.set_skill(triggerIds=[2348], enable=True)
        self.set_skill(triggerIds=[2349], enable=True)
        self.set_skill(triggerIds=[2350], enable=True)
        self.set_skill(triggerIds=[2351], enable=True)
        self.set_skill(triggerIds=[2352], enable=True)
        self.set_skill(triggerIds=[2353], enable=True)
        self.set_skill(triggerIds=[2354], enable=True)
        self.set_skill(triggerIds=[2355], enable=True)
        self.set_skill(triggerIds=[2356], enable=True)
        self.set_skill(triggerIds=[2357], enable=True)
        self.set_skill(triggerIds=[2358], enable=True)
        self.set_skill(triggerIds=[2359], enable=True)
        self.set_skill(triggerIds=[2360], enable=True)
        self.set_skill(triggerIds=[2361], enable=True)
        self.set_skill(triggerIds=[2362], enable=True)
        self.set_skill(triggerIds=[2363], enable=True)
        self.set_skill(triggerIds=[2364], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬11대기(self.ctx)


class 스킬11대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2346], enable=False)
        self.set_skill(triggerIds=[2347], enable=False)
        self.set_skill(triggerIds=[2348], enable=False)
        self.set_skill(triggerIds=[2349], enable=False)
        self.set_skill(triggerIds=[2350], enable=False)
        self.set_skill(triggerIds=[2351], enable=False)
        self.set_skill(triggerIds=[2352], enable=False)
        self.set_skill(triggerIds=[2353], enable=False)
        self.set_skill(triggerIds=[2354], enable=False)
        self.set_skill(triggerIds=[2355], enable=False)
        self.set_skill(triggerIds=[2356], enable=False)
        self.set_skill(triggerIds=[2357], enable=False)
        self.set_skill(triggerIds=[2358], enable=False)
        self.set_skill(triggerIds=[2359], enable=False)
        self.set_skill(triggerIds=[2360], enable=False)
        self.set_skill(triggerIds=[2361], enable=False)
        self.set_skill(triggerIds=[2362], enable=False)
        self.set_skill(triggerIds=[2363], enable=False)
        self.set_skill(triggerIds=[2364], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬11(self.ctx)


class 스킬11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2353], enable=True)
        self.set_skill(triggerIds=[2354], enable=True)
        self.set_skill(triggerIds=[2355], enable=True)
        self.set_skill(triggerIds=[2356], enable=True)
        self.set_skill(triggerIds=[2357], enable=True)
        self.set_skill(triggerIds=[2358], enable=True)
        self.set_skill(triggerIds=[2359], enable=True)
        self.set_skill(triggerIds=[2360], enable=True)
        self.set_skill(triggerIds=[2361], enable=True)
        self.set_skill(triggerIds=[2362], enable=True)
        self.set_skill(triggerIds=[2363], enable=True)
        self.set_skill(triggerIds=[2364], enable=True)
        self.set_skill(triggerIds=[2365], enable=True)
        self.set_skill(triggerIds=[2366], enable=True)
        self.set_skill(triggerIds=[2367], enable=True)
        self.set_skill(triggerIds=[2368], enable=True)
        self.set_skill(triggerIds=[2369], enable=True)
        self.set_skill(triggerIds=[2370], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬12대기(self.ctx)


class 스킬12대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2353], enable=False)
        self.set_skill(triggerIds=[2354], enable=False)
        self.set_skill(triggerIds=[2355], enable=False)
        self.set_skill(triggerIds=[2356], enable=False)
        self.set_skill(triggerIds=[2357], enable=False)
        self.set_skill(triggerIds=[2358], enable=False)
        self.set_skill(triggerIds=[2359], enable=False)
        self.set_skill(triggerIds=[2360], enable=False)
        self.set_skill(triggerIds=[2361], enable=False)
        self.set_skill(triggerIds=[2362], enable=False)
        self.set_skill(triggerIds=[2363], enable=False)
        self.set_skill(triggerIds=[2364], enable=False)
        self.set_skill(triggerIds=[2365], enable=False)
        self.set_skill(triggerIds=[2366], enable=False)
        self.set_skill(triggerIds=[2367], enable=False)
        self.set_skill(triggerIds=[2368], enable=False)
        self.set_skill(triggerIds=[2369], enable=False)
        self.set_skill(triggerIds=[2370], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬12(self.ctx)


class 스킬12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2359], enable=True)
        self.set_skill(triggerIds=[2360], enable=True)
        self.set_skill(triggerIds=[2361], enable=True)
        self.set_skill(triggerIds=[2362], enable=True)
        self.set_skill(triggerIds=[2363], enable=True)
        self.set_skill(triggerIds=[2364], enable=True)
        self.set_skill(triggerIds=[2365], enable=True)
        self.set_skill(triggerIds=[2366], enable=True)
        self.set_skill(triggerIds=[2367], enable=True)
        self.set_skill(triggerIds=[2368], enable=True)
        self.set_skill(triggerIds=[2369], enable=True)
        self.set_skill(triggerIds=[2370], enable=True)
        self.set_skill(triggerIds=[2371], enable=True)
        self.set_skill(triggerIds=[2372], enable=True)
        self.set_skill(triggerIds=[2373], enable=True)
        self.set_skill(triggerIds=[2374], enable=True)
        self.set_skill(triggerIds=[2375], enable=True)
        self.set_skill(triggerIds=[2376], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬13대기(self.ctx)


class 스킬13대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2359], enable=False)
        self.set_skill(triggerIds=[2360], enable=False)
        self.set_skill(triggerIds=[2361], enable=False)
        self.set_skill(triggerIds=[2362], enable=False)
        self.set_skill(triggerIds=[2363], enable=False)
        self.set_skill(triggerIds=[2364], enable=False)
        self.set_skill(triggerIds=[2365], enable=False)
        self.set_skill(triggerIds=[2366], enable=False)
        self.set_skill(triggerIds=[2367], enable=False)
        self.set_skill(triggerIds=[2368], enable=False)
        self.set_skill(triggerIds=[2369], enable=False)
        self.set_skill(triggerIds=[2370], enable=False)
        self.set_skill(triggerIds=[2371], enable=False)
        self.set_skill(triggerIds=[2372], enable=False)
        self.set_skill(triggerIds=[2373], enable=False)
        self.set_skill(triggerIds=[2374], enable=False)
        self.set_skill(triggerIds=[2375], enable=False)
        self.set_skill(triggerIds=[2376], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬13(self.ctx)


class 스킬13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2365], enable=True)
        self.set_skill(triggerIds=[2366], enable=True)
        self.set_skill(triggerIds=[2367], enable=True)
        self.set_skill(triggerIds=[2368], enable=True)
        self.set_skill(triggerIds=[2369], enable=True)
        self.set_skill(triggerIds=[2370], enable=True)
        self.set_skill(triggerIds=[2371], enable=True)
        self.set_skill(triggerIds=[2372], enable=True)
        self.set_skill(triggerIds=[2373], enable=True)
        self.set_skill(triggerIds=[2374], enable=True)
        self.set_skill(triggerIds=[2375], enable=True)
        self.set_skill(triggerIds=[2376], enable=True)
        self.set_skill(triggerIds=[2377], enable=True)
        self.set_skill(triggerIds=[2378], enable=True)
        self.set_skill(triggerIds=[2379], enable=True)
        self.set_skill(triggerIds=[2380], enable=True)
        self.set_skill(triggerIds=[2381], enable=True)
        self.set_skill(triggerIds=[2382], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬14대기(self.ctx)


class 스킬14대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2365], enable=False)
        self.set_skill(triggerIds=[2366], enable=False)
        self.set_skill(triggerIds=[2367], enable=False)
        self.set_skill(triggerIds=[2368], enable=False)
        self.set_skill(triggerIds=[2369], enable=False)
        self.set_skill(triggerIds=[2370], enable=False)
        self.set_skill(triggerIds=[2371], enable=False)
        self.set_skill(triggerIds=[2372], enable=False)
        self.set_skill(triggerIds=[2373], enable=False)
        self.set_skill(triggerIds=[2374], enable=False)
        self.set_skill(triggerIds=[2375], enable=False)
        self.set_skill(triggerIds=[2376], enable=False)
        self.set_skill(triggerIds=[2377], enable=False)
        self.set_skill(triggerIds=[2378], enable=False)
        self.set_skill(triggerIds=[2379], enable=False)
        self.set_skill(triggerIds=[2380], enable=False)
        self.set_skill(triggerIds=[2381], enable=False)
        self.set_skill(triggerIds=[2382], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬14(self.ctx)


class 스킬14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2371], enable=True)
        self.set_skill(triggerIds=[2372], enable=True)
        self.set_skill(triggerIds=[2373], enable=True)
        self.set_skill(triggerIds=[2374], enable=True)
        self.set_skill(triggerIds=[2375], enable=True)
        self.set_skill(triggerIds=[2376], enable=True)
        self.set_skill(triggerIds=[2377], enable=True)
        self.set_skill(triggerIds=[2378], enable=True)
        self.set_skill(triggerIds=[2379], enable=True)
        self.set_skill(triggerIds=[2380], enable=True)
        self.set_skill(triggerIds=[2381], enable=True)
        self.set_skill(triggerIds=[2382], enable=True)
        self.set_skill(triggerIds=[2383], enable=True)
        self.set_skill(triggerIds=[2384], enable=True)
        self.set_skill(triggerIds=[2385], enable=True)
        self.set_skill(triggerIds=[2386], enable=True)
        self.set_skill(triggerIds=[2387], enable=True)
        self.set_skill(triggerIds=[2388], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬15대기(self.ctx)


class 스킬15대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2371], enable=False)
        self.set_skill(triggerIds=[2372], enable=False)
        self.set_skill(triggerIds=[2373], enable=False)
        self.set_skill(triggerIds=[2374], enable=False)
        self.set_skill(triggerIds=[2375], enable=False)
        self.set_skill(triggerIds=[2376], enable=False)
        self.set_skill(triggerIds=[2377], enable=False)
        self.set_skill(triggerIds=[2378], enable=False)
        self.set_skill(triggerIds=[2379], enable=False)
        self.set_skill(triggerIds=[2380], enable=False)
        self.set_skill(triggerIds=[2381], enable=False)
        self.set_skill(triggerIds=[2382], enable=False)
        self.set_skill(triggerIds=[2383], enable=False)
        self.set_skill(triggerIds=[2384], enable=False)
        self.set_skill(triggerIds=[2385], enable=False)
        self.set_skill(triggerIds=[2386], enable=False)
        self.set_skill(triggerIds=[2387], enable=False)
        self.set_skill(triggerIds=[2388], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬15(self.ctx)


class 스킬15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2377], enable=True)
        self.set_skill(triggerIds=[2378], enable=True)
        self.set_skill(triggerIds=[2379], enable=True)
        self.set_skill(triggerIds=[2380], enable=True)
        self.set_skill(triggerIds=[2381], enable=True)
        self.set_skill(triggerIds=[2382], enable=True)
        self.set_skill(triggerIds=[2383], enable=True)
        self.set_skill(triggerIds=[2384], enable=True)
        self.set_skill(triggerIds=[2385], enable=True)
        self.set_skill(triggerIds=[2386], enable=True)
        self.set_skill(triggerIds=[2387], enable=True)
        self.set_skill(triggerIds=[2388], enable=True)
        self.set_skill(triggerIds=[2389], enable=True)
        self.set_skill(triggerIds=[2390], enable=True)
        self.set_skill(triggerIds=[2391], enable=True)
        self.set_skill(triggerIds=[2392], enable=True)
        self.set_skill(triggerIds=[2393], enable=True)
        self.set_skill(triggerIds=[2394], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬16대기(self.ctx)


class 스킬16대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2377], enable=False)
        self.set_skill(triggerIds=[2378], enable=False)
        self.set_skill(triggerIds=[2379], enable=False)
        self.set_skill(triggerIds=[2380], enable=False)
        self.set_skill(triggerIds=[2381], enable=False)
        self.set_skill(triggerIds=[2382], enable=False)
        self.set_skill(triggerIds=[2383], enable=False)
        self.set_skill(triggerIds=[2384], enable=False)
        self.set_skill(triggerIds=[2385], enable=False)
        self.set_skill(triggerIds=[2386], enable=False)
        self.set_skill(triggerIds=[2387], enable=False)
        self.set_skill(triggerIds=[2388], enable=False)
        self.set_skill(triggerIds=[2389], enable=False)
        self.set_skill(triggerIds=[2390], enable=False)
        self.set_skill(triggerIds=[2391], enable=False)
        self.set_skill(triggerIds=[2392], enable=False)
        self.set_skill(triggerIds=[2393], enable=False)
        self.set_skill(triggerIds=[2394], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬16(self.ctx)


class 스킬16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2383], enable=True)
        self.set_skill(triggerIds=[2384], enable=True)
        self.set_skill(triggerIds=[2385], enable=True)
        self.set_skill(triggerIds=[2386], enable=True)
        self.set_skill(triggerIds=[2387], enable=True)
        self.set_skill(triggerIds=[2388], enable=True)
        self.set_skill(triggerIds=[2389], enable=True)
        self.set_skill(triggerIds=[2390], enable=True)
        self.set_skill(triggerIds=[2391], enable=True)
        self.set_skill(triggerIds=[2392], enable=True)
        self.set_skill(triggerIds=[2393], enable=True)
        self.set_skill(triggerIds=[2394], enable=True)
        self.set_skill(triggerIds=[2395], enable=True)
        self.set_skill(triggerIds=[2396], enable=True)
        self.set_skill(triggerIds=[2397], enable=True)
        self.set_skill(triggerIds=[2398], enable=True)
        self.set_skill(triggerIds=[2399], enable=True)
        self.set_skill(triggerIds=[2400], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬17대기(self.ctx)


class 스킬17대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2383], enable=False)
        self.set_skill(triggerIds=[2384], enable=False)
        self.set_skill(triggerIds=[2385], enable=False)
        self.set_skill(triggerIds=[2386], enable=False)
        self.set_skill(triggerIds=[2387], enable=False)
        self.set_skill(triggerIds=[2388], enable=False)
        self.set_skill(triggerIds=[2389], enable=False)
        self.set_skill(triggerIds=[2390], enable=False)
        self.set_skill(triggerIds=[2391], enable=False)
        self.set_skill(triggerIds=[2392], enable=False)
        self.set_skill(triggerIds=[2393], enable=False)
        self.set_skill(triggerIds=[2394], enable=False)
        self.set_skill(triggerIds=[2395], enable=False)
        self.set_skill(triggerIds=[2396], enable=False)
        self.set_skill(triggerIds=[2397], enable=False)
        self.set_skill(triggerIds=[2398], enable=False)
        self.set_skill(triggerIds=[2399], enable=False)
        self.set_skill(triggerIds=[2400], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬17(self.ctx)


class 스킬17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2389], enable=True)
        self.set_skill(triggerIds=[2390], enable=True)
        self.set_skill(triggerIds=[2391], enable=True)
        self.set_skill(triggerIds=[2392], enable=True)
        self.set_skill(triggerIds=[2393], enable=True)
        self.set_skill(triggerIds=[2394], enable=True)
        self.set_skill(triggerIds=[2395], enable=True)
        self.set_skill(triggerIds=[2396], enable=True)
        self.set_skill(triggerIds=[2397], enable=True)
        self.set_skill(triggerIds=[2398], enable=True)
        self.set_skill(triggerIds=[2399], enable=True)
        self.set_skill(triggerIds=[2400], enable=True)
        self.set_skill(triggerIds=[2401], enable=True)
        self.set_skill(triggerIds=[2402], enable=True)
        self.set_skill(triggerIds=[2403], enable=True)
        self.set_skill(triggerIds=[2404], enable=True)
        self.set_skill(triggerIds=[2405], enable=True)
        self.set_skill(triggerIds=[2406], enable=True)
        self.set_skill(triggerIds=[2407], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬18대기(self.ctx)


class 스킬18대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2389], enable=False)
        self.set_skill(triggerIds=[2390], enable=False)
        self.set_skill(triggerIds=[2391], enable=False)
        self.set_skill(triggerIds=[2392], enable=False)
        self.set_skill(triggerIds=[2393], enable=False)
        self.set_skill(triggerIds=[2394], enable=False)
        self.set_skill(triggerIds=[2395], enable=False)
        self.set_skill(triggerIds=[2396], enable=False)
        self.set_skill(triggerIds=[2397], enable=False)
        self.set_skill(triggerIds=[2398], enable=False)
        self.set_skill(triggerIds=[2399], enable=False)
        self.set_skill(triggerIds=[2400], enable=False)
        self.set_skill(triggerIds=[2401], enable=False)
        self.set_skill(triggerIds=[2402], enable=False)
        self.set_skill(triggerIds=[2403], enable=False)
        self.set_skill(triggerIds=[2404], enable=False)
        self.set_skill(triggerIds=[2405], enable=False)
        self.set_skill(triggerIds=[2406], enable=False)
        self.set_skill(triggerIds=[2407], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬18(self.ctx)


class 스킬18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2401], enable=True)
        self.set_skill(triggerIds=[2402], enable=True)
        self.set_skill(triggerIds=[2403], enable=True)
        self.set_skill(triggerIds=[2404], enable=True)
        self.set_skill(triggerIds=[2405], enable=True)
        self.set_skill(triggerIds=[2406], enable=True)
        self.set_skill(triggerIds=[2407], enable=True)
        self.set_skill(triggerIds=[2408], enable=True)
        self.set_skill(triggerIds=[2409], enable=True)
        self.set_skill(triggerIds=[2410], enable=True)
        self.set_skill(triggerIds=[2411], enable=True)
        self.set_skill(triggerIds=[2412], enable=True)
        self.set_skill(triggerIds=[2413], enable=True)
        self.set_skill(triggerIds=[2414], enable=True)
        self.set_skill(triggerIds=[2415], enable=True)
        self.set_skill(triggerIds=[2416], enable=True)
        self.set_skill(triggerIds=[2417], enable=True)
        self.set_skill(triggerIds=[2418], enable=True)
        self.set_skill(triggerIds=[2419], enable=True)
        self.set_skill(triggerIds=[2420], enable=True)
        self.set_skill(triggerIds=[2421], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬19대기(self.ctx)


class 스킬19대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2401], enable=False)
        self.set_skill(triggerIds=[2402], enable=False)
        self.set_skill(triggerIds=[2403], enable=False)
        self.set_skill(triggerIds=[2404], enable=False)
        self.set_skill(triggerIds=[2405], enable=False)
        self.set_skill(triggerIds=[2406], enable=False)
        self.set_skill(triggerIds=[2407], enable=False)
        self.set_skill(triggerIds=[2408], enable=False)
        self.set_skill(triggerIds=[2409], enable=False)
        self.set_skill(triggerIds=[2410], enable=False)
        self.set_skill(triggerIds=[2411], enable=False)
        self.set_skill(triggerIds=[2412], enable=False)
        self.set_skill(triggerIds=[2413], enable=False)
        self.set_skill(triggerIds=[2414], enable=False)
        self.set_skill(triggerIds=[2415], enable=False)
        self.set_skill(triggerIds=[2416], enable=False)
        self.set_skill(triggerIds=[2417], enable=False)
        self.set_skill(triggerIds=[2418], enable=False)
        self.set_skill(triggerIds=[2419], enable=False)
        self.set_skill(triggerIds=[2420], enable=False)
        self.set_skill(triggerIds=[2421], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬19(self.ctx)


class 스킬19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2408], enable=True)
        self.set_skill(triggerIds=[2409], enable=True)
        self.set_skill(triggerIds=[2410], enable=True)
        self.set_skill(triggerIds=[2411], enable=True)
        self.set_skill(triggerIds=[2412], enable=True)
        self.set_skill(triggerIds=[2413], enable=True)
        self.set_skill(triggerIds=[2414], enable=True)
        self.set_skill(triggerIds=[2415], enable=True)
        self.set_skill(triggerIds=[2416], enable=True)
        self.set_skill(triggerIds=[2417], enable=True)
        self.set_skill(triggerIds=[2418], enable=True)
        self.set_skill(triggerIds=[2419], enable=True)
        self.set_skill(triggerIds=[2420], enable=True)
        self.set_skill(triggerIds=[2421], enable=True)
        self.set_skill(triggerIds=[2422], enable=True)
        self.set_skill(triggerIds=[2423], enable=True)
        self.set_skill(triggerIds=[2424], enable=True)
        self.set_skill(triggerIds=[2425], enable=True)
        self.set_skill(triggerIds=[2426], enable=True)
        self.set_skill(triggerIds=[2427], enable=True)
        self.set_skill(triggerIds=[2428], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬20대기(self.ctx)


class 스킬20대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2408], enable=False)
        self.set_skill(triggerIds=[2409], enable=False)
        self.set_skill(triggerIds=[2410], enable=False)
        self.set_skill(triggerIds=[2411], enable=False)
        self.set_skill(triggerIds=[2412], enable=False)
        self.set_skill(triggerIds=[2413], enable=False)
        self.set_skill(triggerIds=[2414], enable=False)
        self.set_skill(triggerIds=[2415], enable=False)
        self.set_skill(triggerIds=[2416], enable=False)
        self.set_skill(triggerIds=[2417], enable=False)
        self.set_skill(triggerIds=[2418], enable=False)
        self.set_skill(triggerIds=[2419], enable=False)
        self.set_skill(triggerIds=[2420], enable=False)
        self.set_skill(triggerIds=[2421], enable=False)
        self.set_skill(triggerIds=[2422], enable=False)
        self.set_skill(triggerIds=[2423], enable=False)
        self.set_skill(triggerIds=[2424], enable=False)
        self.set_skill(triggerIds=[2425], enable=False)
        self.set_skill(triggerIds=[2426], enable=False)
        self.set_skill(triggerIds=[2427], enable=False)
        self.set_skill(triggerIds=[2428], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬20(self.ctx)


class 스킬20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2415], enable=True)
        self.set_skill(triggerIds=[2416], enable=True)
        self.set_skill(triggerIds=[2417], enable=True)
        self.set_skill(triggerIds=[2418], enable=True)
        self.set_skill(triggerIds=[2419], enable=True)
        self.set_skill(triggerIds=[2420], enable=True)
        self.set_skill(triggerIds=[2421], enable=True)
        self.set_skill(triggerIds=[2422], enable=True)
        self.set_skill(triggerIds=[2423], enable=True)
        self.set_skill(triggerIds=[2424], enable=True)
        self.set_skill(triggerIds=[2425], enable=True)
        self.set_skill(triggerIds=[2426], enable=True)
        self.set_skill(triggerIds=[2427], enable=True)
        self.set_skill(triggerIds=[2428], enable=True)
        self.set_skill(triggerIds=[2429], enable=True)
        self.set_skill(triggerIds=[2430], enable=True)
        self.set_skill(triggerIds=[2431], enable=True)
        self.set_skill(triggerIds=[2432], enable=True)
        self.set_skill(triggerIds=[2433], enable=True)
        self.set_skill(triggerIds=[2434], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬21대기(self.ctx)


class 스킬21대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2415], enable=False)
        self.set_skill(triggerIds=[2416], enable=False)
        self.set_skill(triggerIds=[2417], enable=False)
        self.set_skill(triggerIds=[2418], enable=False)
        self.set_skill(triggerIds=[2419], enable=False)
        self.set_skill(triggerIds=[2420], enable=False)
        self.set_skill(triggerIds=[2421], enable=False)
        self.set_skill(triggerIds=[2422], enable=False)
        self.set_skill(triggerIds=[2423], enable=False)
        self.set_skill(triggerIds=[2424], enable=False)
        self.set_skill(triggerIds=[2425], enable=False)
        self.set_skill(triggerIds=[2426], enable=False)
        self.set_skill(triggerIds=[2427], enable=False)
        self.set_skill(triggerIds=[2428], enable=False)
        self.set_skill(triggerIds=[2429], enable=False)
        self.set_skill(triggerIds=[2430], enable=False)
        self.set_skill(triggerIds=[2431], enable=False)
        self.set_skill(triggerIds=[2432], enable=False)
        self.set_skill(triggerIds=[2433], enable=False)
        self.set_skill(triggerIds=[2434], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬21(self.ctx)


class 스킬21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2422], enable=True)
        self.set_skill(triggerIds=[2423], enable=True)
        self.set_skill(triggerIds=[2424], enable=True)
        self.set_skill(triggerIds=[2425], enable=True)
        self.set_skill(triggerIds=[2426], enable=True)
        self.set_skill(triggerIds=[2427], enable=True)
        self.set_skill(triggerIds=[2428], enable=True)
        self.set_skill(triggerIds=[2429], enable=True)
        self.set_skill(triggerIds=[2430], enable=True)
        self.set_skill(triggerIds=[2431], enable=True)
        self.set_skill(triggerIds=[2432], enable=True)
        self.set_skill(triggerIds=[2433], enable=True)
        self.set_skill(triggerIds=[2434], enable=True)
        self.set_skill(triggerIds=[2435], enable=True)
        self.set_skill(triggerIds=[2436], enable=True)
        self.set_skill(triggerIds=[2437], enable=True)
        self.set_skill(triggerIds=[2438], enable=True)
        self.set_skill(triggerIds=[2439], enable=True)
        self.set_skill(triggerIds=[2440], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬22대기(self.ctx)


class 스킬22대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2422], enable=False)
        self.set_skill(triggerIds=[2423], enable=False)
        self.set_skill(triggerIds=[2424], enable=False)
        self.set_skill(triggerIds=[2425], enable=False)
        self.set_skill(triggerIds=[2426], enable=False)
        self.set_skill(triggerIds=[2427], enable=False)
        self.set_skill(triggerIds=[2428], enable=False)
        self.set_skill(triggerIds=[2429], enable=False)
        self.set_skill(triggerIds=[2430], enable=False)
        self.set_skill(triggerIds=[2431], enable=False)
        self.set_skill(triggerIds=[2432], enable=False)
        self.set_skill(triggerIds=[2433], enable=False)
        self.set_skill(triggerIds=[2434], enable=False)
        self.set_skill(triggerIds=[2435], enable=False)
        self.set_skill(triggerIds=[2436], enable=False)
        self.set_skill(triggerIds=[2437], enable=False)
        self.set_skill(triggerIds=[2438], enable=False)
        self.set_skill(triggerIds=[2439], enable=False)
        self.set_skill(triggerIds=[2440], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬22(self.ctx)


class 스킬22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2429], enable=True)
        self.set_skill(triggerIds=[2430], enable=True)
        self.set_skill(triggerIds=[2431], enable=True)
        self.set_skill(triggerIds=[2432], enable=True)
        self.set_skill(triggerIds=[2433], enable=True)
        self.set_skill(triggerIds=[2434], enable=True)
        self.set_skill(triggerIds=[2435], enable=True)
        self.set_skill(triggerIds=[2436], enable=True)
        self.set_skill(triggerIds=[2437], enable=True)
        self.set_skill(triggerIds=[2438], enable=True)
        self.set_skill(triggerIds=[2439], enable=True)
        self.set_skill(triggerIds=[2440], enable=True)
        self.set_skill(triggerIds=[2441], enable=True)
        self.set_skill(triggerIds=[2442], enable=True)
        self.set_skill(triggerIds=[2443], enable=True)
        self.set_skill(triggerIds=[2444], enable=True)
        self.set_skill(triggerIds=[2445], enable=True)
        self.set_skill(triggerIds=[2446], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬23대기(self.ctx)


class 스킬23대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2429], enable=False)
        self.set_skill(triggerIds=[2430], enable=False)
        self.set_skill(triggerIds=[2431], enable=False)
        self.set_skill(triggerIds=[2432], enable=False)
        self.set_skill(triggerIds=[2433], enable=False)
        self.set_skill(triggerIds=[2434], enable=False)
        self.set_skill(triggerIds=[2435], enable=False)
        self.set_skill(triggerIds=[2436], enable=False)
        self.set_skill(triggerIds=[2437], enable=False)
        self.set_skill(triggerIds=[2438], enable=False)
        self.set_skill(triggerIds=[2439], enable=False)
        self.set_skill(triggerIds=[2440], enable=False)
        self.set_skill(triggerIds=[2441], enable=False)
        self.set_skill(triggerIds=[2442], enable=False)
        self.set_skill(triggerIds=[2443], enable=False)
        self.set_skill(triggerIds=[2444], enable=False)
        self.set_skill(triggerIds=[2445], enable=False)
        self.set_skill(triggerIds=[2446], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬23(self.ctx)


class 스킬23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2435], enable=True)
        self.set_skill(triggerIds=[2436], enable=True)
        self.set_skill(triggerIds=[2437], enable=True)
        self.set_skill(triggerIds=[2438], enable=True)
        self.set_skill(triggerIds=[2439], enable=True)
        self.set_skill(triggerIds=[2440], enable=True)
        self.set_skill(triggerIds=[2441], enable=True)
        self.set_skill(triggerIds=[2442], enable=True)
        self.set_skill(triggerIds=[2443], enable=True)
        self.set_skill(triggerIds=[2444], enable=True)
        self.set_skill(triggerIds=[2445], enable=True)
        self.set_skill(triggerIds=[2446], enable=True)
        self.set_skill(triggerIds=[2447], enable=True)
        self.set_skill(triggerIds=[2448], enable=True)
        self.set_skill(triggerIds=[2449], enable=True)
        self.set_skill(triggerIds=[2450], enable=True)
        self.set_skill(triggerIds=[2451], enable=True)
        self.set_skill(triggerIds=[2452], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬24대기(self.ctx)


class 스킬24대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2435], enable=False)
        self.set_skill(triggerIds=[2436], enable=False)
        self.set_skill(triggerIds=[2437], enable=False)
        self.set_skill(triggerIds=[2438], enable=False)
        self.set_skill(triggerIds=[2439], enable=False)
        self.set_skill(triggerIds=[2440], enable=False)
        self.set_skill(triggerIds=[2441], enable=False)
        self.set_skill(triggerIds=[2442], enable=False)
        self.set_skill(triggerIds=[2443], enable=False)
        self.set_skill(triggerIds=[2444], enable=False)
        self.set_skill(triggerIds=[2445], enable=False)
        self.set_skill(triggerIds=[2446], enable=False)
        self.set_skill(triggerIds=[2447], enable=False)
        self.set_skill(triggerIds=[2448], enable=False)
        self.set_skill(triggerIds=[2449], enable=False)
        self.set_skill(triggerIds=[2450], enable=False)
        self.set_skill(triggerIds=[2451], enable=False)
        self.set_skill(triggerIds=[2452], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬24(self.ctx)


class 스킬24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2441], enable=True)
        self.set_skill(triggerIds=[2442], enable=True)
        self.set_skill(triggerIds=[2443], enable=True)
        self.set_skill(triggerIds=[2444], enable=True)
        self.set_skill(triggerIds=[2445], enable=True)
        self.set_skill(triggerIds=[2446], enable=True)
        self.set_skill(triggerIds=[2447], enable=True)
        self.set_skill(triggerIds=[2448], enable=True)
        self.set_skill(triggerIds=[2449], enable=True)
        self.set_skill(triggerIds=[2450], enable=True)
        self.set_skill(triggerIds=[2451], enable=True)
        self.set_skill(triggerIds=[2452], enable=True)
        self.set_skill(triggerIds=[2453], enable=True)
        self.set_skill(triggerIds=[2454], enable=True)
        self.set_skill(triggerIds=[2455], enable=True)
        self.set_skill(triggerIds=[2456], enable=True)
        self.set_skill(triggerIds=[2457], enable=True)
        self.set_skill(triggerIds=[2458], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬25대기(self.ctx)


class 스킬25대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2441], enable=False)
        self.set_skill(triggerIds=[2442], enable=False)
        self.set_skill(triggerIds=[2443], enable=False)
        self.set_skill(triggerIds=[2444], enable=False)
        self.set_skill(triggerIds=[2445], enable=False)
        self.set_skill(triggerIds=[2446], enable=False)
        self.set_skill(triggerIds=[2447], enable=False)
        self.set_skill(triggerIds=[2448], enable=False)
        self.set_skill(triggerIds=[2449], enable=False)
        self.set_skill(triggerIds=[2450], enable=False)
        self.set_skill(triggerIds=[2451], enable=False)
        self.set_skill(triggerIds=[2452], enable=False)
        self.set_skill(triggerIds=[2453], enable=False)
        self.set_skill(triggerIds=[2454], enable=False)
        self.set_skill(triggerIds=[2455], enable=False)
        self.set_skill(triggerIds=[2456], enable=False)
        self.set_skill(triggerIds=[2457], enable=False)
        self.set_skill(triggerIds=[2458], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬25(self.ctx)


class 스킬25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2447], enable=True)
        self.set_skill(triggerIds=[2448], enable=True)
        self.set_skill(triggerIds=[2449], enable=True)
        self.set_skill(triggerIds=[2450], enable=True)
        self.set_skill(triggerIds=[2451], enable=True)
        self.set_skill(triggerIds=[2452], enable=True)
        self.set_skill(triggerIds=[2453], enable=True)
        self.set_skill(triggerIds=[2454], enable=True)
        self.set_skill(triggerIds=[2455], enable=True)
        self.set_skill(triggerIds=[2456], enable=True)
        self.set_skill(triggerIds=[2457], enable=True)
        self.set_skill(triggerIds=[2458], enable=True)
        self.set_skill(triggerIds=[2459], enable=True)
        self.set_skill(triggerIds=[2460], enable=True)
        self.set_skill(triggerIds=[2461], enable=True)
        self.set_skill(triggerIds=[2462], enable=True)
        self.set_skill(triggerIds=[2463], enable=True)
        self.set_skill(triggerIds=[2464], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬26대기(self.ctx)


class 스킬26대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2447], enable=False)
        self.set_skill(triggerIds=[2448], enable=False)
        self.set_skill(triggerIds=[2449], enable=False)
        self.set_skill(triggerIds=[2450], enable=False)
        self.set_skill(triggerIds=[2451], enable=False)
        self.set_skill(triggerIds=[2452], enable=False)
        self.set_skill(triggerIds=[2453], enable=False)
        self.set_skill(triggerIds=[2454], enable=False)
        self.set_skill(triggerIds=[2455], enable=False)
        self.set_skill(triggerIds=[2456], enable=False)
        self.set_skill(triggerIds=[2457], enable=False)
        self.set_skill(triggerIds=[2458], enable=False)
        self.set_skill(triggerIds=[2459], enable=False)
        self.set_skill(triggerIds=[2460], enable=False)
        self.set_skill(triggerIds=[2461], enable=False)
        self.set_skill(triggerIds=[2462], enable=False)
        self.set_skill(triggerIds=[2463], enable=False)
        self.set_skill(triggerIds=[2464], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬26(self.ctx)


class 스킬26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2453], enable=True)
        self.set_skill(triggerIds=[2454], enable=True)
        self.set_skill(triggerIds=[2455], enable=True)
        self.set_skill(triggerIds=[2456], enable=True)
        self.set_skill(triggerIds=[2457], enable=True)
        self.set_skill(triggerIds=[2458], enable=True)
        self.set_skill(triggerIds=[2459], enable=True)
        self.set_skill(triggerIds=[2460], enable=True)
        self.set_skill(triggerIds=[2461], enable=True)
        self.set_skill(triggerIds=[2462], enable=True)
        self.set_skill(triggerIds=[2463], enable=True)
        self.set_skill(triggerIds=[2464], enable=True)
        self.set_skill(triggerIds=[2465], enable=True)
        self.set_skill(triggerIds=[2466], enable=True)
        self.set_skill(triggerIds=[2467], enable=True)
        self.set_skill(triggerIds=[2468], enable=True)
        self.set_skill(triggerIds=[2469], enable=True)
        self.set_skill(triggerIds=[2470], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬27대기(self.ctx)


class 스킬27대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2453], enable=False)
        self.set_skill(triggerIds=[2454], enable=False)
        self.set_skill(triggerIds=[2455], enable=False)
        self.set_skill(triggerIds=[2456], enable=False)
        self.set_skill(triggerIds=[2457], enable=False)
        self.set_skill(triggerIds=[2458], enable=False)
        self.set_skill(triggerIds=[2459], enable=False)
        self.set_skill(triggerIds=[2460], enable=False)
        self.set_skill(triggerIds=[2461], enable=False)
        self.set_skill(triggerIds=[2462], enable=False)
        self.set_skill(triggerIds=[2463], enable=False)
        self.set_skill(triggerIds=[2464], enable=False)
        self.set_skill(triggerIds=[2465], enable=False)
        self.set_skill(triggerIds=[2466], enable=False)
        self.set_skill(triggerIds=[2467], enable=False)
        self.set_skill(triggerIds=[2468], enable=False)
        self.set_skill(triggerIds=[2469], enable=False)
        self.set_skill(triggerIds=[2470], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬27(self.ctx)


class 스킬27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2459], enable=True)
        self.set_skill(triggerIds=[2460], enable=True)
        self.set_skill(triggerIds=[2461], enable=True)
        self.set_skill(triggerIds=[2462], enable=True)
        self.set_skill(triggerIds=[2463], enable=True)
        self.set_skill(triggerIds=[2464], enable=True)
        self.set_skill(triggerIds=[2465], enable=True)
        self.set_skill(triggerIds=[2466], enable=True)
        self.set_skill(triggerIds=[2467], enable=True)
        self.set_skill(triggerIds=[2468], enable=True)
        self.set_skill(triggerIds=[2469], enable=True)
        self.set_skill(triggerIds=[2470], enable=True)
        self.set_skill(triggerIds=[2471], enable=True)
        self.set_skill(triggerIds=[2472], enable=True)
        self.set_skill(triggerIds=[2473], enable=True)
        self.set_skill(triggerIds=[2474], enable=True)
        self.set_skill(triggerIds=[2475], enable=True)
        self.set_skill(triggerIds=[2476], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬28대기(self.ctx)


class 스킬28대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2459], enable=False)
        self.set_skill(triggerIds=[2460], enable=False)
        self.set_skill(triggerIds=[2461], enable=False)
        self.set_skill(triggerIds=[2462], enable=False)
        self.set_skill(triggerIds=[2463], enable=False)
        self.set_skill(triggerIds=[2464], enable=False)
        self.set_skill(triggerIds=[2465], enable=False)
        self.set_skill(triggerIds=[2466], enable=False)
        self.set_skill(triggerIds=[2467], enable=False)
        self.set_skill(triggerIds=[2468], enable=False)
        self.set_skill(triggerIds=[2469], enable=False)
        self.set_skill(triggerIds=[2470], enable=False)
        self.set_skill(triggerIds=[2471], enable=False)
        self.set_skill(triggerIds=[2472], enable=False)
        self.set_skill(triggerIds=[2473], enable=False)
        self.set_skill(triggerIds=[2474], enable=False)
        self.set_skill(triggerIds=[2475], enable=False)
        self.set_skill(triggerIds=[2476], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬28(self.ctx)


class 스킬28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2465], enable=True)
        self.set_skill(triggerIds=[2466], enable=True)
        self.set_skill(triggerIds=[2467], enable=True)
        self.set_skill(triggerIds=[2468], enable=True)
        self.set_skill(triggerIds=[2469], enable=True)
        self.set_skill(triggerIds=[2470], enable=True)
        self.set_skill(triggerIds=[2471], enable=True)
        self.set_skill(triggerIds=[2472], enable=True)
        self.set_skill(triggerIds=[2473], enable=True)
        self.set_skill(triggerIds=[2474], enable=True)
        self.set_skill(triggerIds=[2475], enable=True)
        self.set_skill(triggerIds=[2476], enable=True)
        self.set_skill(triggerIds=[2477], enable=True)
        self.set_skill(triggerIds=[2478], enable=True)
        self.set_skill(triggerIds=[2479], enable=True)
        self.set_skill(triggerIds=[2480], enable=True)
        self.set_skill(triggerIds=[2481], enable=True)
        self.set_skill(triggerIds=[2482], enable=True)
        self.set_skill(triggerIds=[2483], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬29대기(self.ctx)


class 스킬29대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2465], enable=False)
        self.set_skill(triggerIds=[2466], enable=False)
        self.set_skill(triggerIds=[2467], enable=False)
        self.set_skill(triggerIds=[2468], enable=False)
        self.set_skill(triggerIds=[2469], enable=False)
        self.set_skill(triggerIds=[2470], enable=False)
        self.set_skill(triggerIds=[2471], enable=False)
        self.set_skill(triggerIds=[2472], enable=False)
        self.set_skill(triggerIds=[2473], enable=False)
        self.set_skill(triggerIds=[2474], enable=False)
        self.set_skill(triggerIds=[2475], enable=False)
        self.set_skill(triggerIds=[2476], enable=False)
        self.set_skill(triggerIds=[2477], enable=False)
        self.set_skill(triggerIds=[2478], enable=False)
        self.set_skill(triggerIds=[2479], enable=False)
        self.set_skill(triggerIds=[2480], enable=False)
        self.set_skill(triggerIds=[2481], enable=False)
        self.set_skill(triggerIds=[2482], enable=False)
        self.set_skill(triggerIds=[2483], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬29(self.ctx)


class 스킬29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2471], enable=True)
        self.set_skill(triggerIds=[2472], enable=True)
        self.set_skill(triggerIds=[2473], enable=True)
        self.set_skill(triggerIds=[2474], enable=True)
        self.set_skill(triggerIds=[2475], enable=True)
        self.set_skill(triggerIds=[2476], enable=True)
        self.set_skill(triggerIds=[2477], enable=True)
        self.set_skill(triggerIds=[2478], enable=True)
        self.set_skill(triggerIds=[2479], enable=True)
        self.set_skill(triggerIds=[2480], enable=True)
        self.set_skill(triggerIds=[2481], enable=True)
        self.set_skill(triggerIds=[2482], enable=True)
        self.set_skill(triggerIds=[2483], enable=True)
        self.set_skill(triggerIds=[2484], enable=True)
        self.set_skill(triggerIds=[2485], enable=True)
        self.set_skill(triggerIds=[2486], enable=True)
        self.set_skill(triggerIds=[2487], enable=True)
        self.set_skill(triggerIds=[2488], enable=True)
        self.set_skill(triggerIds=[2489], enable=True)
        self.set_skill(triggerIds=[2490], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬30대기(self.ctx)


class 스킬30대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2471], enable=False)
        self.set_skill(triggerIds=[2472], enable=False)
        self.set_skill(triggerIds=[2473], enable=False)
        self.set_skill(triggerIds=[2474], enable=False)
        self.set_skill(triggerIds=[2475], enable=False)
        self.set_skill(triggerIds=[2476], enable=False)
        self.set_skill(triggerIds=[2477], enable=False)
        self.set_skill(triggerIds=[2478], enable=False)
        self.set_skill(triggerIds=[2479], enable=False)
        self.set_skill(triggerIds=[2480], enable=False)
        self.set_skill(triggerIds=[2481], enable=False)
        self.set_skill(triggerIds=[2482], enable=False)
        self.set_skill(triggerIds=[2483], enable=False)
        self.set_skill(triggerIds=[2484], enable=False)
        self.set_skill(triggerIds=[2485], enable=False)
        self.set_skill(triggerIds=[2486], enable=False)
        self.set_skill(triggerIds=[2487], enable=False)
        self.set_skill(triggerIds=[2488], enable=False)
        self.set_skill(triggerIds=[2489], enable=False)
        self.set_skill(triggerIds=[2490], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬30(self.ctx)


class 스킬30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2477], enable=True)
        self.set_skill(triggerIds=[2478], enable=True)
        self.set_skill(triggerIds=[2479], enable=True)
        self.set_skill(triggerIds=[2480], enable=True)
        self.set_skill(triggerIds=[2481], enable=True)
        self.set_skill(triggerIds=[2482], enable=True)
        self.set_skill(triggerIds=[2483], enable=True)
        self.set_skill(triggerIds=[2484], enable=True)
        self.set_skill(triggerIds=[2485], enable=True)
        self.set_skill(triggerIds=[2486], enable=True)
        self.set_skill(triggerIds=[2487], enable=True)
        self.set_skill(triggerIds=[2488], enable=True)
        self.set_skill(triggerIds=[2489], enable=True)
        self.set_skill(triggerIds=[2490], enable=True)
        self.set_skill(triggerIds=[2491], enable=True)
        self.set_skill(triggerIds=[2492], enable=True)
        self.set_skill(triggerIds=[2493], enable=True)
        self.set_skill(triggerIds=[2494], enable=True)
        self.set_skill(triggerIds=[2495], enable=True)
        self.set_skill(triggerIds=[2496], enable=True)
        self.set_skill(triggerIds=[2497], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬31대기(self.ctx)


class 스킬31대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2477], enable=False)
        self.set_skill(triggerIds=[2478], enable=False)
        self.set_skill(triggerIds=[2479], enable=False)
        self.set_skill(triggerIds=[2480], enable=False)
        self.set_skill(triggerIds=[2481], enable=False)
        self.set_skill(triggerIds=[2482], enable=False)
        self.set_skill(triggerIds=[2483], enable=False)
        self.set_skill(triggerIds=[2484], enable=False)
        self.set_skill(triggerIds=[2485], enable=False)
        self.set_skill(triggerIds=[2486], enable=False)
        self.set_skill(triggerIds=[2487], enable=False)
        self.set_skill(triggerIds=[2488], enable=False)
        self.set_skill(triggerIds=[2489], enable=False)
        self.set_skill(triggerIds=[2490], enable=False)
        self.set_skill(triggerIds=[2491], enable=False)
        self.set_skill(triggerIds=[2492], enable=False)
        self.set_skill(triggerIds=[2493], enable=False)
        self.set_skill(triggerIds=[2494], enable=False)
        self.set_skill(triggerIds=[2495], enable=False)
        self.set_skill(triggerIds=[2496], enable=False)
        self.set_skill(triggerIds=[2497], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬31(self.ctx)


class 스킬31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2484], enable=True)
        self.set_skill(triggerIds=[2485], enable=True)
        self.set_skill(triggerIds=[2486], enable=True)
        self.set_skill(triggerIds=[2487], enable=True)
        self.set_skill(triggerIds=[2488], enable=True)
        self.set_skill(triggerIds=[2489], enable=True)
        self.set_skill(triggerIds=[2490], enable=True)
        self.set_skill(triggerIds=[2491], enable=True)
        self.set_skill(triggerIds=[2492], enable=True)
        self.set_skill(triggerIds=[2493], enable=True)
        self.set_skill(triggerIds=[2494], enable=True)
        self.set_skill(triggerIds=[2495], enable=True)
        self.set_skill(triggerIds=[2496], enable=True)
        self.set_skill(triggerIds=[2497], enable=True)
        self.set_skill(triggerIds=[2498], enable=True)
        self.set_skill(triggerIds=[2499], enable=True)
        self.set_skill(triggerIds=[2500], enable=True)
        self.set_skill(triggerIds=[2501], enable=True)
        self.set_skill(triggerIds=[2502], enable=True)
        self.set_skill(triggerIds=[2503], enable=True)
        self.set_skill(triggerIds=[2504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬32대기(self.ctx)


class 스킬32대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2484], enable=False)
        self.set_skill(triggerIds=[2485], enable=False)
        self.set_skill(triggerIds=[2486], enable=False)
        self.set_skill(triggerIds=[2487], enable=False)
        self.set_skill(triggerIds=[2488], enable=False)
        self.set_skill(triggerIds=[2489], enable=False)
        self.set_skill(triggerIds=[2490], enable=False)
        self.set_skill(triggerIds=[2491], enable=False)
        self.set_skill(triggerIds=[2492], enable=False)
        self.set_skill(triggerIds=[2493], enable=False)
        self.set_skill(triggerIds=[2494], enable=False)
        self.set_skill(triggerIds=[2495], enable=False)
        self.set_skill(triggerIds=[2496], enable=False)
        self.set_skill(triggerIds=[2497], enable=False)
        self.set_skill(triggerIds=[2498], enable=False)
        self.set_skill(triggerIds=[2499], enable=False)
        self.set_skill(triggerIds=[2500], enable=False)
        self.set_skill(triggerIds=[2501], enable=False)
        self.set_skill(triggerIds=[2502], enable=False)
        self.set_skill(triggerIds=[2503], enable=False)
        self.set_skill(triggerIds=[2504], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬32(self.ctx)


class 스킬32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2491], enable=True)
        self.set_skill(triggerIds=[2492], enable=True)
        self.set_skill(triggerIds=[2493], enable=True)
        self.set_skill(triggerIds=[2494], enable=True)
        self.set_skill(triggerIds=[2495], enable=True)
        self.set_skill(triggerIds=[2496], enable=True)
        self.set_skill(triggerIds=[2497], enable=True)
        self.set_skill(triggerIds=[2498], enable=True)
        self.set_skill(triggerIds=[2499], enable=True)
        self.set_skill(triggerIds=[2500], enable=True)
        self.set_skill(triggerIds=[2501], enable=True)
        self.set_skill(triggerIds=[2502], enable=True)
        self.set_skill(triggerIds=[2503], enable=True)
        self.set_skill(triggerIds=[2504], enable=True)
        self.set_skill(triggerIds=[2505], enable=True)
        self.set_skill(triggerIds=[2506], enable=True)
        self.set_skill(triggerIds=[2507], enable=True)
        self.set_skill(triggerIds=[2508], enable=True)
        self.set_skill(triggerIds=[2509], enable=True)
        self.set_skill(triggerIds=[2510], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬33대기(self.ctx)


class 스킬33대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2491], enable=False)
        self.set_skill(triggerIds=[2492], enable=False)
        self.set_skill(triggerIds=[2493], enable=False)
        self.set_skill(triggerIds=[2494], enable=False)
        self.set_skill(triggerIds=[2495], enable=False)
        self.set_skill(triggerIds=[2496], enable=False)
        self.set_skill(triggerIds=[2497], enable=False)
        self.set_skill(triggerIds=[2498], enable=False)
        self.set_skill(triggerIds=[2499], enable=False)
        self.set_skill(triggerIds=[2500], enable=False)
        self.set_skill(triggerIds=[2501], enable=False)
        self.set_skill(triggerIds=[2502], enable=False)
        self.set_skill(triggerIds=[2503], enable=False)
        self.set_skill(triggerIds=[2504], enable=False)
        self.set_skill(triggerIds=[2505], enable=False)
        self.set_skill(triggerIds=[2506], enable=False)
        self.set_skill(triggerIds=[2507], enable=False)
        self.set_skill(triggerIds=[2508], enable=False)
        self.set_skill(triggerIds=[2509], enable=False)
        self.set_skill(triggerIds=[2510], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬33(self.ctx)


class 스킬33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2498], enable=True)
        self.set_skill(triggerIds=[2499], enable=True)
        self.set_skill(triggerIds=[2500], enable=True)
        self.set_skill(triggerIds=[2501], enable=True)
        self.set_skill(triggerIds=[2502], enable=True)
        self.set_skill(triggerIds=[2503], enable=True)
        self.set_skill(triggerIds=[2504], enable=True)
        self.set_skill(triggerIds=[2505], enable=True)
        self.set_skill(triggerIds=[2506], enable=True)
        self.set_skill(triggerIds=[2507], enable=True)
        self.set_skill(triggerIds=[2508], enable=True)
        self.set_skill(triggerIds=[2509], enable=True)
        self.set_skill(triggerIds=[2510], enable=True)
        self.set_skill(triggerIds=[2511], enable=True)
        self.set_skill(triggerIds=[2512], enable=True)
        self.set_skill(triggerIds=[2513], enable=True)
        self.set_skill(triggerIds=[2514], enable=True)
        self.set_skill(triggerIds=[2515], enable=True)
        self.set_skill(triggerIds=[2516], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬34대기(self.ctx)


class 스킬34대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2498], enable=False)
        self.set_skill(triggerIds=[2499], enable=False)
        self.set_skill(triggerIds=[2500], enable=False)
        self.set_skill(triggerIds=[2501], enable=False)
        self.set_skill(triggerIds=[2502], enable=False)
        self.set_skill(triggerIds=[2503], enable=False)
        self.set_skill(triggerIds=[2504], enable=False)
        self.set_skill(triggerIds=[2505], enable=False)
        self.set_skill(triggerIds=[2506], enable=False)
        self.set_skill(triggerIds=[2507], enable=False)
        self.set_skill(triggerIds=[2508], enable=False)
        self.set_skill(triggerIds=[2509], enable=False)
        self.set_skill(triggerIds=[2510], enable=False)
        self.set_skill(triggerIds=[2511], enable=False)
        self.set_skill(triggerIds=[2512], enable=False)
        self.set_skill(triggerIds=[2513], enable=False)
        self.set_skill(triggerIds=[2514], enable=False)
        self.set_skill(triggerIds=[2515], enable=False)
        self.set_skill(triggerIds=[2516], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬34(self.ctx)


class 스킬34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2505], enable=True)
        self.set_skill(triggerIds=[2506], enable=True)
        self.set_skill(triggerIds=[2507], enable=True)
        self.set_skill(triggerIds=[2508], enable=True)
        self.set_skill(triggerIds=[2509], enable=True)
        self.set_skill(triggerIds=[2510], enable=True)
        self.set_skill(triggerIds=[2511], enable=True)
        self.set_skill(triggerIds=[2512], enable=True)
        self.set_skill(triggerIds=[2513], enable=True)
        self.set_skill(triggerIds=[2514], enable=True)
        self.set_skill(triggerIds=[2515], enable=True)
        self.set_skill(triggerIds=[2516], enable=True)
        self.set_skill(triggerIds=[2517], enable=True)
        self.set_skill(triggerIds=[2518], enable=True)
        self.set_skill(triggerIds=[2519], enable=True)
        self.set_skill(triggerIds=[2520], enable=True)
        self.set_skill(triggerIds=[2521], enable=True)
        self.set_skill(triggerIds=[2522], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬35대기(self.ctx)


class 스킬35대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2505], enable=False)
        self.set_skill(triggerIds=[2506], enable=False)
        self.set_skill(triggerIds=[2507], enable=False)
        self.set_skill(triggerIds=[2508], enable=False)
        self.set_skill(triggerIds=[2509], enable=False)
        self.set_skill(triggerIds=[2510], enable=False)
        self.set_skill(triggerIds=[2511], enable=False)
        self.set_skill(triggerIds=[2512], enable=False)
        self.set_skill(triggerIds=[2513], enable=False)
        self.set_skill(triggerIds=[2514], enable=False)
        self.set_skill(triggerIds=[2515], enable=False)
        self.set_skill(triggerIds=[2516], enable=False)
        self.set_skill(triggerIds=[2517], enable=False)
        self.set_skill(triggerIds=[2518], enable=False)
        self.set_skill(triggerIds=[2519], enable=False)
        self.set_skill(triggerIds=[2520], enable=False)
        self.set_skill(triggerIds=[2521], enable=False)
        self.set_skill(triggerIds=[2522], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.true():
            return 스킬35(self.ctx)


class 스킬35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2511], enable=True)
        self.set_skill(triggerIds=[2512], enable=True)
        self.set_skill(triggerIds=[2513], enable=True)
        self.set_skill(triggerIds=[2514], enable=True)
        self.set_skill(triggerIds=[2515], enable=True)
        self.set_skill(triggerIds=[2516], enable=True)
        self.set_skill(triggerIds=[2517], enable=True)
        self.set_skill(triggerIds=[2518], enable=True)
        self.set_skill(triggerIds=[2519], enable=True)
        self.set_skill(triggerIds=[2520], enable=True)
        self.set_skill(triggerIds=[2521], enable=True)
        self.set_skill(triggerIds=[2522], enable=True)
        self.set_skill(triggerIds=[2523], enable=True)
        self.set_skill(triggerIds=[2524], enable=True)
        self.set_skill(triggerIds=[2525], enable=True)
        self.set_skill(triggerIds=[2526], enable=True)
        self.set_skill(triggerIds=[2527], enable=True)
        self.set_skill(triggerIds=[2528], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='1'):
            return 스킬36대기(self.ctx)


class 스킬36대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[2511], enable=False)
        self.set_skill(triggerIds=[2512], enable=False)
        self.set_skill(triggerIds=[2513], enable=False)
        self.set_skill(triggerIds=[2514], enable=False)
        self.set_skill(triggerIds=[2515], enable=False)
        self.set_skill(triggerIds=[2516], enable=False)
        self.set_skill(triggerIds=[2517], enable=False)
        self.set_skill(triggerIds=[2518], enable=False)
        self.set_skill(triggerIds=[2519], enable=False)
        self.set_skill(triggerIds=[2520], enable=False)
        self.set_skill(triggerIds=[2521], enable=False)
        self.set_skill(triggerIds=[2522], enable=False)
        self.set_skill(triggerIds=[2523], enable=False)
        self.set_skill(triggerIds=[2524], enable=False)
        self.set_skill(triggerIds=[2525], enable=False)
        self.set_skill(triggerIds=[2526], enable=False)
        self.set_skill(triggerIds=[2527], enable=False)
        self.set_skill(triggerIds=[2528], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 게임오버(self.ctx)


class 게임오버(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    pass


initial_state = 대기
