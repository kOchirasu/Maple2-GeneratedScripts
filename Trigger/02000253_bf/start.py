""" trigger/02000253_bf/start.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=True)
        set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=False)
        set_effect(triggerIds=[8013], visible=False)
        set_effect(triggerIds=[8014], visible=False)
        set_effect(triggerIds=[8015], visible=False)
        set_effect(triggerIds=[8016], visible=False)
        set_effect(triggerIds=[8017], visible=False)
        set_effect(triggerIds=[8018], visible=False)
        set_effect(triggerIds=[8019], visible=False)
        set_effect(triggerIds=[8020], visible=False)
        set_effect(triggerIds=[8021], visible=False)
        set_effect(triggerIds=[8022], visible=False)
        set_effect(triggerIds=[8023], visible=False)
        set_effect(triggerIds=[8024], visible=False)
        set_effect(triggerIds=[8025], visible=False)
        set_effect(triggerIds=[8026], visible=False)
        set_effect(triggerIds=[8027], visible=False)
        set_effect(triggerIds=[8028], visible=False)
        set_effect(triggerIds=[8029], visible=False)
        set_effect(triggerIds=[8030], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=905, boxId=1):
            return 예고이펙트()


class 예고이펙트(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4021], arg2=True)
        create_monster(spawnIds=[4022], arg2=True)
        create_monster(spawnIds=[4023], arg2=True)
        create_monster(spawnIds=[4024], arg2=True)
        create_monster(spawnIds=[4025], arg2=True)
        create_monster(spawnIds=[4026], arg2=True)
        create_monster(spawnIds=[4027], arg2=True)
        create_monster(spawnIds=[4028], arg2=True)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='5'):
            return 스킬시작대기()


class 스킬시작대기(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            set_effect(triggerIds=[8013], visible=False)
            set_effect(triggerIds=[8014], visible=False)
            set_effect(triggerIds=[8015], visible=False)
            set_effect(triggerIds=[8016], visible=False)
            set_effect(triggerIds=[8017], visible=False)
            set_effect(triggerIds=[8018], visible=False)
            set_effect(triggerIds=[8019], visible=False)
            set_effect(triggerIds=[8020], visible=False)
            set_effect(triggerIds=[8021], visible=False)
            set_effect(triggerIds=[8022], visible=False)
            set_effect(triggerIds=[8023], visible=False)
            set_effect(triggerIds=[8024], visible=False)
            set_effect(triggerIds=[8025], visible=False)
            set_effect(triggerIds=[8026], visible=False)
            set_effect(triggerIds=[8027], visible=False)
            set_effect(triggerIds=[8028], visible=False)
            set_effect(triggerIds=[8029], visible=False)
            set_effect(triggerIds=[8030], visible=False)
            return 스킬01()


class 스킬01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2301], isEnable=True)
        set_skill(triggerIds=[2302], isEnable=True)
        set_skill(triggerIds=[2303], isEnable=True)
        set_skill(triggerIds=[2304], isEnable=True)
        set_skill(triggerIds=[2305], isEnable=True)
        set_skill(triggerIds=[2306], isEnable=True)
        set_skill(triggerIds=[2307], isEnable=True)
        set_skill(triggerIds=[2308], isEnable=True)
        set_skill(triggerIds=[2309], isEnable=True)
        set_skill(triggerIds=[2310], isEnable=True)
        set_skill(triggerIds=[2311], isEnable=True)
        set_skill(triggerIds=[2312], isEnable=True)
        set_skill(triggerIds=[2313], isEnable=True)
        set_skill(triggerIds=[2314], isEnable=True)
        set_skill(triggerIds=[2315], isEnable=True)
        set_skill(triggerIds=[2316], isEnable=True)
        set_skill(triggerIds=[2317], isEnable=True)
        set_skill(triggerIds=[2318], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬02대기()


class 스킬02대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1004])
        set_skill(triggerIds=[2301], isEnable=False)
        set_skill(triggerIds=[2302], isEnable=False)
        set_skill(triggerIds=[2303], isEnable=False)
        set_skill(triggerIds=[2304], isEnable=False)
        set_skill(triggerIds=[2305], isEnable=False)
        set_skill(triggerIds=[2306], isEnable=False)
        set_skill(triggerIds=[2307], isEnable=False)
        set_skill(triggerIds=[2308], isEnable=False)
        set_skill(triggerIds=[2309], isEnable=False)
        set_skill(triggerIds=[2310], isEnable=False)
        set_skill(triggerIds=[2311], isEnable=False)
        set_skill(triggerIds=[2312], isEnable=False)
        set_skill(triggerIds=[2313], isEnable=False)
        set_skill(triggerIds=[2314], isEnable=False)
        set_skill(triggerIds=[2315], isEnable=False)
        set_skill(triggerIds=[2316], isEnable=False)
        set_skill(triggerIds=[2317], isEnable=False)
        set_skill(triggerIds=[2318], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬02()


class 스킬02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2307], isEnable=True)
        set_skill(triggerIds=[2308], isEnable=True)
        set_skill(triggerIds=[2309], isEnable=True)
        set_skill(triggerIds=[2310], isEnable=True)
        set_skill(triggerIds=[2311], isEnable=True)
        set_skill(triggerIds=[2312], isEnable=True)
        set_skill(triggerIds=[2313], isEnable=True)
        set_skill(triggerIds=[2314], isEnable=True)
        set_skill(triggerIds=[2315], isEnable=True)
        set_skill(triggerIds=[2316], isEnable=True)
        set_skill(triggerIds=[2317], isEnable=True)
        set_skill(triggerIds=[2318], isEnable=True)
        set_skill(triggerIds=[2319], isEnable=True)
        set_skill(triggerIds=[2320], isEnable=True)
        set_skill(triggerIds=[2321], isEnable=True)
        set_skill(triggerIds=[2322], isEnable=True)
        set_skill(triggerIds=[2323], isEnable=True)
        set_skill(triggerIds=[2324], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬03대기()


class 스킬03대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2307], isEnable=False)
        set_skill(triggerIds=[2308], isEnable=False)
        set_skill(triggerIds=[2309], isEnable=False)
        set_skill(triggerIds=[2310], isEnable=False)
        set_skill(triggerIds=[2311], isEnable=False)
        set_skill(triggerIds=[2312], isEnable=False)
        set_skill(triggerIds=[2313], isEnable=False)
        set_skill(triggerIds=[2314], isEnable=False)
        set_skill(triggerIds=[2315], isEnable=False)
        set_skill(triggerIds=[2316], isEnable=False)
        set_skill(triggerIds=[2317], isEnable=False)
        set_skill(triggerIds=[2318], isEnable=False)
        set_skill(triggerIds=[2319], isEnable=False)
        set_skill(triggerIds=[2320], isEnable=False)
        set_skill(triggerIds=[2321], isEnable=False)
        set_skill(triggerIds=[2322], isEnable=False)
        set_skill(triggerIds=[2323], isEnable=False)
        set_skill(triggerIds=[2324], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬03()


class 스킬03(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2313], isEnable=True)
        set_skill(triggerIds=[2314], isEnable=True)
        set_skill(triggerIds=[2315], isEnable=True)
        set_skill(triggerIds=[2316], isEnable=True)
        set_skill(triggerIds=[2317], isEnable=True)
        set_skill(triggerIds=[2318], isEnable=True)
        set_skill(triggerIds=[2319], isEnable=True)
        set_skill(triggerIds=[2320], isEnable=True)
        set_skill(triggerIds=[2321], isEnable=True)
        set_skill(triggerIds=[2322], isEnable=True)
        set_skill(triggerIds=[2323], isEnable=True)
        set_skill(triggerIds=[2324], isEnable=True)
        set_skill(triggerIds=[2325], isEnable=True)
        set_skill(triggerIds=[2326], isEnable=True)
        set_skill(triggerIds=[2327], isEnable=True)
        set_skill(triggerIds=[2328], isEnable=True)
        set_skill(triggerIds=[2329], isEnable=True)
        set_skill(triggerIds=[2330], isEnable=True)
        set_skill(triggerIds=[2331], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬04대기()


class 스킬04대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2313], isEnable=False)
        set_skill(triggerIds=[2314], isEnable=False)
        set_skill(triggerIds=[2315], isEnable=False)
        set_skill(triggerIds=[2316], isEnable=False)
        set_skill(triggerIds=[2317], isEnable=False)
        set_skill(triggerIds=[2318], isEnable=False)
        set_skill(triggerIds=[2319], isEnable=False)
        set_skill(triggerIds=[2320], isEnable=False)
        set_skill(triggerIds=[2321], isEnable=False)
        set_skill(triggerIds=[2322], isEnable=False)
        set_skill(triggerIds=[2323], isEnable=False)
        set_skill(triggerIds=[2324], isEnable=False)
        set_skill(triggerIds=[2325], isEnable=False)
        set_skill(triggerIds=[2326], isEnable=False)
        set_skill(triggerIds=[2327], isEnable=False)
        set_skill(triggerIds=[2328], isEnable=False)
        set_skill(triggerIds=[2329], isEnable=False)
        set_skill(triggerIds=[2330], isEnable=False)
        set_skill(triggerIds=[2331], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬05()


class 스킬05(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2319], isEnable=True)
        set_skill(triggerIds=[2320], isEnable=True)
        set_skill(triggerIds=[2321], isEnable=True)
        set_skill(triggerIds=[2322], isEnable=True)
        set_skill(triggerIds=[2323], isEnable=True)
        set_skill(triggerIds=[2324], isEnable=True)
        set_skill(triggerIds=[2325], isEnable=True)
        set_skill(triggerIds=[2326], isEnable=True)
        set_skill(triggerIds=[2327], isEnable=True)
        set_skill(triggerIds=[2328], isEnable=True)
        set_skill(triggerIds=[2329], isEnable=True)
        set_skill(triggerIds=[2330], isEnable=True)
        set_skill(triggerIds=[2331], isEnable=True)
        set_skill(triggerIds=[2332], isEnable=True)
        set_skill(triggerIds=[2333], isEnable=True)
        set_skill(triggerIds=[2334], isEnable=True)
        set_skill(triggerIds=[2335], isEnable=True)
        set_skill(triggerIds=[2336], isEnable=True)
        set_skill(triggerIds=[2337], isEnable=True)
        set_skill(triggerIds=[2338], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬06대기()


class 스킬06대기(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002522)
        set_skill(triggerIds=[2319], isEnable=False)
        set_skill(triggerIds=[2320], isEnable=False)
        set_skill(triggerIds=[2321], isEnable=False)
        set_skill(triggerIds=[2322], isEnable=False)
        set_skill(triggerIds=[2323], isEnable=False)
        set_skill(triggerIds=[2324], isEnable=False)
        set_skill(triggerIds=[2325], isEnable=False)
        set_skill(triggerIds=[2326], isEnable=False)
        set_skill(triggerIds=[2327], isEnable=False)
        set_skill(triggerIds=[2328], isEnable=False)
        set_skill(triggerIds=[2329], isEnable=False)
        set_skill(triggerIds=[2330], isEnable=False)
        set_skill(triggerIds=[2331], isEnable=False)
        set_skill(triggerIds=[2332], isEnable=False)
        set_skill(triggerIds=[2333], isEnable=False)
        set_skill(triggerIds=[2334], isEnable=False)
        set_skill(triggerIds=[2335], isEnable=False)
        set_skill(triggerIds=[2336], isEnable=False)
        set_skill(triggerIds=[2337], isEnable=False)
        set_skill(triggerIds=[2338], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬07()


class 스킬07(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2325], isEnable=True)
        set_skill(triggerIds=[2326], isEnable=True)
        set_skill(triggerIds=[2327], isEnable=True)
        set_skill(triggerIds=[2328], isEnable=True)
        set_skill(triggerIds=[2329], isEnable=True)
        set_skill(triggerIds=[2330], isEnable=True)
        set_skill(triggerIds=[2331], isEnable=True)
        set_skill(triggerIds=[2332], isEnable=True)
        set_skill(triggerIds=[2333], isEnable=True)
        set_skill(triggerIds=[2334], isEnable=True)
        set_skill(triggerIds=[2335], isEnable=True)
        set_skill(triggerIds=[2336], isEnable=True)
        set_skill(triggerIds=[2337], isEnable=True)
        set_skill(triggerIds=[2338], isEnable=True)
        set_skill(triggerIds=[2339], isEnable=True)
        set_skill(triggerIds=[2340], isEnable=True)
        set_skill(triggerIds=[2341], isEnable=True)
        set_skill(triggerIds=[2342], isEnable=True)
        set_skill(triggerIds=[2343], isEnable=True)
        set_skill(triggerIds=[2344], isEnable=True)
        set_skill(triggerIds=[2345], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬08대기()


class 스킬08대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2325], isEnable=False)
        set_skill(triggerIds=[2326], isEnable=False)
        set_skill(triggerIds=[2327], isEnable=False)
        set_skill(triggerIds=[2328], isEnable=False)
        set_skill(triggerIds=[2329], isEnable=False)
        set_skill(triggerIds=[2330], isEnable=False)
        set_skill(triggerIds=[2331], isEnable=False)
        set_skill(triggerIds=[2332], isEnable=False)
        set_skill(triggerIds=[2333], isEnable=False)
        set_skill(triggerIds=[2334], isEnable=False)
        set_skill(triggerIds=[2335], isEnable=False)
        set_skill(triggerIds=[2336], isEnable=False)
        set_skill(triggerIds=[2337], isEnable=False)
        set_skill(triggerIds=[2338], isEnable=False)
        set_skill(triggerIds=[2339], isEnable=False)
        set_skill(triggerIds=[2340], isEnable=False)
        set_skill(triggerIds=[2341], isEnable=False)
        set_skill(triggerIds=[2342], isEnable=False)
        set_skill(triggerIds=[2343], isEnable=False)
        set_skill(triggerIds=[2344], isEnable=False)
        set_skill(triggerIds=[2345], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬08()


class 스킬08(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2332], isEnable=True)
        set_skill(triggerIds=[2333], isEnable=True)
        set_skill(triggerIds=[2334], isEnable=True)
        set_skill(triggerIds=[2335], isEnable=True)
        set_skill(triggerIds=[2336], isEnable=True)
        set_skill(triggerIds=[2337], isEnable=True)
        set_skill(triggerIds=[2338], isEnable=True)
        set_skill(triggerIds=[2339], isEnable=True)
        set_skill(triggerIds=[2340], isEnable=True)
        set_skill(triggerIds=[2341], isEnable=True)
        set_skill(triggerIds=[2342], isEnable=True)
        set_skill(triggerIds=[2343], isEnable=True)
        set_skill(triggerIds=[2344], isEnable=True)
        set_skill(triggerIds=[2345], isEnable=True)
        set_skill(triggerIds=[2346], isEnable=True)
        set_skill(triggerIds=[2347], isEnable=True)
        set_skill(triggerIds=[2348], isEnable=True)
        set_skill(triggerIds=[2349], isEnable=True)
        set_skill(triggerIds=[2350], isEnable=True)
        set_skill(triggerIds=[2351], isEnable=True)
        set_skill(triggerIds=[2352], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬09대기()


class 스킬09대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2332], isEnable=False)
        set_skill(triggerIds=[2333], isEnable=False)
        set_skill(triggerIds=[2334], isEnable=False)
        set_skill(triggerIds=[2335], isEnable=False)
        set_skill(triggerIds=[2336], isEnable=False)
        set_skill(triggerIds=[2337], isEnable=False)
        set_skill(triggerIds=[2338], isEnable=False)
        set_skill(triggerIds=[2339], isEnable=False)
        set_skill(triggerIds=[2340], isEnable=False)
        set_skill(triggerIds=[2341], isEnable=False)
        set_skill(triggerIds=[2342], isEnable=False)
        set_skill(triggerIds=[2343], isEnable=False)
        set_skill(triggerIds=[2344], isEnable=False)
        set_skill(triggerIds=[2345], isEnable=False)
        set_skill(triggerIds=[2346], isEnable=False)
        set_skill(triggerIds=[2347], isEnable=False)
        set_skill(triggerIds=[2348], isEnable=False)
        set_skill(triggerIds=[2349], isEnable=False)
        set_skill(triggerIds=[2350], isEnable=False)
        set_skill(triggerIds=[2351], isEnable=False)
        set_skill(triggerIds=[2352], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬09()


class 스킬09(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2339], isEnable=True)
        set_skill(triggerIds=[2340], isEnable=True)
        set_skill(triggerIds=[2341], isEnable=True)
        set_skill(triggerIds=[2342], isEnable=True)
        set_skill(triggerIds=[2343], isEnable=True)
        set_skill(triggerIds=[2344], isEnable=True)
        set_skill(triggerIds=[2345], isEnable=True)
        set_skill(triggerIds=[2346], isEnable=True)
        set_skill(triggerIds=[2347], isEnable=True)
        set_skill(triggerIds=[2348], isEnable=True)
        set_skill(triggerIds=[2349], isEnable=True)
        set_skill(triggerIds=[2350], isEnable=True)
        set_skill(triggerIds=[2351], isEnable=True)
        set_skill(triggerIds=[2352], isEnable=True)
        set_skill(triggerIds=[2353], isEnable=True)
        set_skill(triggerIds=[2354], isEnable=True)
        set_skill(triggerIds=[2355], isEnable=True)
        set_skill(triggerIds=[2356], isEnable=True)
        set_skill(triggerIds=[2357], isEnable=True)
        set_skill(triggerIds=[2358], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬10대기()


class 스킬10대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2339], isEnable=False)
        set_skill(triggerIds=[2340], isEnable=False)
        set_skill(triggerIds=[2341], isEnable=False)
        set_skill(triggerIds=[2342], isEnable=False)
        set_skill(triggerIds=[2343], isEnable=False)
        set_skill(triggerIds=[2344], isEnable=False)
        set_skill(triggerIds=[2345], isEnable=False)
        set_skill(triggerIds=[2346], isEnable=False)
        set_skill(triggerIds=[2347], isEnable=False)
        set_skill(triggerIds=[2348], isEnable=False)
        set_skill(triggerIds=[2349], isEnable=False)
        set_skill(triggerIds=[2350], isEnable=False)
        set_skill(triggerIds=[2351], isEnable=False)
        set_skill(triggerIds=[2352], isEnable=False)
        set_skill(triggerIds=[2353], isEnable=False)
        set_skill(triggerIds=[2354], isEnable=False)
        set_skill(triggerIds=[2355], isEnable=False)
        set_skill(triggerIds=[2356], isEnable=False)
        set_skill(triggerIds=[2357], isEnable=False)
        set_skill(triggerIds=[2358], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬10()


class 스킬10(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2346], isEnable=True)
        set_skill(triggerIds=[2347], isEnable=True)
        set_skill(triggerIds=[2348], isEnable=True)
        set_skill(triggerIds=[2349], isEnable=True)
        set_skill(triggerIds=[2350], isEnable=True)
        set_skill(triggerIds=[2351], isEnable=True)
        set_skill(triggerIds=[2352], isEnable=True)
        set_skill(triggerIds=[2353], isEnable=True)
        set_skill(triggerIds=[2354], isEnable=True)
        set_skill(triggerIds=[2355], isEnable=True)
        set_skill(triggerIds=[2356], isEnable=True)
        set_skill(triggerIds=[2357], isEnable=True)
        set_skill(triggerIds=[2358], isEnable=True)
        set_skill(triggerIds=[2359], isEnable=True)
        set_skill(triggerIds=[2360], isEnable=True)
        set_skill(triggerIds=[2361], isEnable=True)
        set_skill(triggerIds=[2362], isEnable=True)
        set_skill(triggerIds=[2363], isEnable=True)
        set_skill(triggerIds=[2364], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬11대기()


class 스킬11대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2346], isEnable=False)
        set_skill(triggerIds=[2347], isEnable=False)
        set_skill(triggerIds=[2348], isEnable=False)
        set_skill(triggerIds=[2349], isEnable=False)
        set_skill(triggerIds=[2350], isEnable=False)
        set_skill(triggerIds=[2351], isEnable=False)
        set_skill(triggerIds=[2352], isEnable=False)
        set_skill(triggerIds=[2353], isEnable=False)
        set_skill(triggerIds=[2354], isEnable=False)
        set_skill(triggerIds=[2355], isEnable=False)
        set_skill(triggerIds=[2356], isEnable=False)
        set_skill(triggerIds=[2357], isEnable=False)
        set_skill(triggerIds=[2358], isEnable=False)
        set_skill(triggerIds=[2359], isEnable=False)
        set_skill(triggerIds=[2360], isEnable=False)
        set_skill(triggerIds=[2361], isEnable=False)
        set_skill(triggerIds=[2362], isEnable=False)
        set_skill(triggerIds=[2363], isEnable=False)
        set_skill(triggerIds=[2364], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬11()


class 스킬11(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2353], isEnable=True)
        set_skill(triggerIds=[2354], isEnable=True)
        set_skill(triggerIds=[2355], isEnable=True)
        set_skill(triggerIds=[2356], isEnable=True)
        set_skill(triggerIds=[2357], isEnable=True)
        set_skill(triggerIds=[2358], isEnable=True)
        set_skill(triggerIds=[2359], isEnable=True)
        set_skill(triggerIds=[2360], isEnable=True)
        set_skill(triggerIds=[2361], isEnable=True)
        set_skill(triggerIds=[2362], isEnable=True)
        set_skill(triggerIds=[2363], isEnable=True)
        set_skill(triggerIds=[2364], isEnable=True)
        set_skill(triggerIds=[2365], isEnable=True)
        set_skill(triggerIds=[2366], isEnable=True)
        set_skill(triggerIds=[2367], isEnable=True)
        set_skill(triggerIds=[2368], isEnable=True)
        set_skill(triggerIds=[2369], isEnable=True)
        set_skill(triggerIds=[2370], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬12대기()


class 스킬12대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2353], isEnable=False)
        set_skill(triggerIds=[2354], isEnable=False)
        set_skill(triggerIds=[2355], isEnable=False)
        set_skill(triggerIds=[2356], isEnable=False)
        set_skill(triggerIds=[2357], isEnable=False)
        set_skill(triggerIds=[2358], isEnable=False)
        set_skill(triggerIds=[2359], isEnable=False)
        set_skill(triggerIds=[2360], isEnable=False)
        set_skill(triggerIds=[2361], isEnable=False)
        set_skill(triggerIds=[2362], isEnable=False)
        set_skill(triggerIds=[2363], isEnable=False)
        set_skill(triggerIds=[2364], isEnable=False)
        set_skill(triggerIds=[2365], isEnable=False)
        set_skill(triggerIds=[2366], isEnable=False)
        set_skill(triggerIds=[2367], isEnable=False)
        set_skill(triggerIds=[2368], isEnable=False)
        set_skill(triggerIds=[2369], isEnable=False)
        set_skill(triggerIds=[2370], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬12()


class 스킬12(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2359], isEnable=True)
        set_skill(triggerIds=[2360], isEnable=True)
        set_skill(triggerIds=[2361], isEnable=True)
        set_skill(triggerIds=[2362], isEnable=True)
        set_skill(triggerIds=[2363], isEnable=True)
        set_skill(triggerIds=[2364], isEnable=True)
        set_skill(triggerIds=[2365], isEnable=True)
        set_skill(triggerIds=[2366], isEnable=True)
        set_skill(triggerIds=[2367], isEnable=True)
        set_skill(triggerIds=[2368], isEnable=True)
        set_skill(triggerIds=[2369], isEnable=True)
        set_skill(triggerIds=[2370], isEnable=True)
        set_skill(triggerIds=[2371], isEnable=True)
        set_skill(triggerIds=[2372], isEnable=True)
        set_skill(triggerIds=[2373], isEnable=True)
        set_skill(triggerIds=[2374], isEnable=True)
        set_skill(triggerIds=[2375], isEnable=True)
        set_skill(triggerIds=[2376], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬13대기()


class 스킬13대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2359], isEnable=False)
        set_skill(triggerIds=[2360], isEnable=False)
        set_skill(triggerIds=[2361], isEnable=False)
        set_skill(triggerIds=[2362], isEnable=False)
        set_skill(triggerIds=[2363], isEnable=False)
        set_skill(triggerIds=[2364], isEnable=False)
        set_skill(triggerIds=[2365], isEnable=False)
        set_skill(triggerIds=[2366], isEnable=False)
        set_skill(triggerIds=[2367], isEnable=False)
        set_skill(triggerIds=[2368], isEnable=False)
        set_skill(triggerIds=[2369], isEnable=False)
        set_skill(triggerIds=[2370], isEnable=False)
        set_skill(triggerIds=[2371], isEnable=False)
        set_skill(triggerIds=[2372], isEnable=False)
        set_skill(triggerIds=[2373], isEnable=False)
        set_skill(triggerIds=[2374], isEnable=False)
        set_skill(triggerIds=[2375], isEnable=False)
        set_skill(triggerIds=[2376], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬13()


class 스킬13(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2365], isEnable=True)
        set_skill(triggerIds=[2366], isEnable=True)
        set_skill(triggerIds=[2367], isEnable=True)
        set_skill(triggerIds=[2368], isEnable=True)
        set_skill(triggerIds=[2369], isEnable=True)
        set_skill(triggerIds=[2370], isEnable=True)
        set_skill(triggerIds=[2371], isEnable=True)
        set_skill(triggerIds=[2372], isEnable=True)
        set_skill(triggerIds=[2373], isEnable=True)
        set_skill(triggerIds=[2374], isEnable=True)
        set_skill(triggerIds=[2375], isEnable=True)
        set_skill(triggerIds=[2376], isEnable=True)
        set_skill(triggerIds=[2377], isEnable=True)
        set_skill(triggerIds=[2378], isEnable=True)
        set_skill(triggerIds=[2379], isEnable=True)
        set_skill(triggerIds=[2380], isEnable=True)
        set_skill(triggerIds=[2381], isEnable=True)
        set_skill(triggerIds=[2382], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬14대기()


class 스킬14대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2365], isEnable=False)
        set_skill(triggerIds=[2366], isEnable=False)
        set_skill(triggerIds=[2367], isEnable=False)
        set_skill(triggerIds=[2368], isEnable=False)
        set_skill(triggerIds=[2369], isEnable=False)
        set_skill(triggerIds=[2370], isEnable=False)
        set_skill(triggerIds=[2371], isEnable=False)
        set_skill(triggerIds=[2372], isEnable=False)
        set_skill(triggerIds=[2373], isEnable=False)
        set_skill(triggerIds=[2374], isEnable=False)
        set_skill(triggerIds=[2375], isEnable=False)
        set_skill(triggerIds=[2376], isEnable=False)
        set_skill(triggerIds=[2377], isEnable=False)
        set_skill(triggerIds=[2378], isEnable=False)
        set_skill(triggerIds=[2379], isEnable=False)
        set_skill(triggerIds=[2380], isEnable=False)
        set_skill(triggerIds=[2381], isEnable=False)
        set_skill(triggerIds=[2382], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬14()


class 스킬14(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2371], isEnable=True)
        set_skill(triggerIds=[2372], isEnable=True)
        set_skill(triggerIds=[2373], isEnable=True)
        set_skill(triggerIds=[2374], isEnable=True)
        set_skill(triggerIds=[2375], isEnable=True)
        set_skill(triggerIds=[2376], isEnable=True)
        set_skill(triggerIds=[2377], isEnable=True)
        set_skill(triggerIds=[2378], isEnable=True)
        set_skill(triggerIds=[2379], isEnable=True)
        set_skill(triggerIds=[2380], isEnable=True)
        set_skill(triggerIds=[2381], isEnable=True)
        set_skill(triggerIds=[2382], isEnable=True)
        set_skill(triggerIds=[2383], isEnable=True)
        set_skill(triggerIds=[2384], isEnable=True)
        set_skill(triggerIds=[2385], isEnable=True)
        set_skill(triggerIds=[2386], isEnable=True)
        set_skill(triggerIds=[2387], isEnable=True)
        set_skill(triggerIds=[2388], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬15대기()


class 스킬15대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2371], isEnable=False)
        set_skill(triggerIds=[2372], isEnable=False)
        set_skill(triggerIds=[2373], isEnable=False)
        set_skill(triggerIds=[2374], isEnable=False)
        set_skill(triggerIds=[2375], isEnable=False)
        set_skill(triggerIds=[2376], isEnable=False)
        set_skill(triggerIds=[2377], isEnable=False)
        set_skill(triggerIds=[2378], isEnable=False)
        set_skill(triggerIds=[2379], isEnable=False)
        set_skill(triggerIds=[2380], isEnable=False)
        set_skill(triggerIds=[2381], isEnable=False)
        set_skill(triggerIds=[2382], isEnable=False)
        set_skill(triggerIds=[2383], isEnable=False)
        set_skill(triggerIds=[2384], isEnable=False)
        set_skill(triggerIds=[2385], isEnable=False)
        set_skill(triggerIds=[2386], isEnable=False)
        set_skill(triggerIds=[2387], isEnable=False)
        set_skill(triggerIds=[2388], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬15()


class 스킬15(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2377], isEnable=True)
        set_skill(triggerIds=[2378], isEnable=True)
        set_skill(triggerIds=[2379], isEnable=True)
        set_skill(triggerIds=[2380], isEnable=True)
        set_skill(triggerIds=[2381], isEnable=True)
        set_skill(triggerIds=[2382], isEnable=True)
        set_skill(triggerIds=[2383], isEnable=True)
        set_skill(triggerIds=[2384], isEnable=True)
        set_skill(triggerIds=[2385], isEnable=True)
        set_skill(triggerIds=[2386], isEnable=True)
        set_skill(triggerIds=[2387], isEnable=True)
        set_skill(triggerIds=[2388], isEnable=True)
        set_skill(triggerIds=[2389], isEnable=True)
        set_skill(triggerIds=[2390], isEnable=True)
        set_skill(triggerIds=[2391], isEnable=True)
        set_skill(triggerIds=[2392], isEnable=True)
        set_skill(triggerIds=[2393], isEnable=True)
        set_skill(triggerIds=[2394], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬16대기()


class 스킬16대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2377], isEnable=False)
        set_skill(triggerIds=[2378], isEnable=False)
        set_skill(triggerIds=[2379], isEnable=False)
        set_skill(triggerIds=[2380], isEnable=False)
        set_skill(triggerIds=[2381], isEnable=False)
        set_skill(triggerIds=[2382], isEnable=False)
        set_skill(triggerIds=[2383], isEnable=False)
        set_skill(triggerIds=[2384], isEnable=False)
        set_skill(triggerIds=[2385], isEnable=False)
        set_skill(triggerIds=[2386], isEnable=False)
        set_skill(triggerIds=[2387], isEnable=False)
        set_skill(triggerIds=[2388], isEnable=False)
        set_skill(triggerIds=[2389], isEnable=False)
        set_skill(triggerIds=[2390], isEnable=False)
        set_skill(triggerIds=[2391], isEnable=False)
        set_skill(triggerIds=[2392], isEnable=False)
        set_skill(triggerIds=[2393], isEnable=False)
        set_skill(triggerIds=[2394], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬16()


class 스킬16(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2383], isEnable=True)
        set_skill(triggerIds=[2384], isEnable=True)
        set_skill(triggerIds=[2385], isEnable=True)
        set_skill(triggerIds=[2386], isEnable=True)
        set_skill(triggerIds=[2387], isEnable=True)
        set_skill(triggerIds=[2388], isEnable=True)
        set_skill(triggerIds=[2389], isEnable=True)
        set_skill(triggerIds=[2390], isEnable=True)
        set_skill(triggerIds=[2391], isEnable=True)
        set_skill(triggerIds=[2392], isEnable=True)
        set_skill(triggerIds=[2393], isEnable=True)
        set_skill(triggerIds=[2394], isEnable=True)
        set_skill(triggerIds=[2395], isEnable=True)
        set_skill(triggerIds=[2396], isEnable=True)
        set_skill(triggerIds=[2397], isEnable=True)
        set_skill(triggerIds=[2398], isEnable=True)
        set_skill(triggerIds=[2399], isEnable=True)
        set_skill(triggerIds=[2400], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬17대기()


class 스킬17대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2383], isEnable=False)
        set_skill(triggerIds=[2384], isEnable=False)
        set_skill(triggerIds=[2385], isEnable=False)
        set_skill(triggerIds=[2386], isEnable=False)
        set_skill(triggerIds=[2387], isEnable=False)
        set_skill(triggerIds=[2388], isEnable=False)
        set_skill(triggerIds=[2389], isEnable=False)
        set_skill(triggerIds=[2390], isEnable=False)
        set_skill(triggerIds=[2391], isEnable=False)
        set_skill(triggerIds=[2392], isEnable=False)
        set_skill(triggerIds=[2393], isEnable=False)
        set_skill(triggerIds=[2394], isEnable=False)
        set_skill(triggerIds=[2395], isEnable=False)
        set_skill(triggerIds=[2396], isEnable=False)
        set_skill(triggerIds=[2397], isEnable=False)
        set_skill(triggerIds=[2398], isEnable=False)
        set_skill(triggerIds=[2399], isEnable=False)
        set_skill(triggerIds=[2400], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬17()


class 스킬17(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2389], isEnable=True)
        set_skill(triggerIds=[2390], isEnable=True)
        set_skill(triggerIds=[2391], isEnable=True)
        set_skill(triggerIds=[2392], isEnable=True)
        set_skill(triggerIds=[2393], isEnable=True)
        set_skill(triggerIds=[2394], isEnable=True)
        set_skill(triggerIds=[2395], isEnable=True)
        set_skill(triggerIds=[2396], isEnable=True)
        set_skill(triggerIds=[2397], isEnable=True)
        set_skill(triggerIds=[2398], isEnable=True)
        set_skill(triggerIds=[2399], isEnable=True)
        set_skill(triggerIds=[2400], isEnable=True)
        set_skill(triggerIds=[2401], isEnable=True)
        set_skill(triggerIds=[2402], isEnable=True)
        set_skill(triggerIds=[2403], isEnable=True)
        set_skill(triggerIds=[2404], isEnable=True)
        set_skill(triggerIds=[2405], isEnable=True)
        set_skill(triggerIds=[2406], isEnable=True)
        set_skill(triggerIds=[2407], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬18대기()


class 스킬18대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2389], isEnable=False)
        set_skill(triggerIds=[2390], isEnable=False)
        set_skill(triggerIds=[2391], isEnable=False)
        set_skill(triggerIds=[2392], isEnable=False)
        set_skill(triggerIds=[2393], isEnable=False)
        set_skill(triggerIds=[2394], isEnable=False)
        set_skill(triggerIds=[2395], isEnable=False)
        set_skill(triggerIds=[2396], isEnable=False)
        set_skill(triggerIds=[2397], isEnable=False)
        set_skill(triggerIds=[2398], isEnable=False)
        set_skill(triggerIds=[2399], isEnable=False)
        set_skill(triggerIds=[2400], isEnable=False)
        set_skill(triggerIds=[2401], isEnable=False)
        set_skill(triggerIds=[2402], isEnable=False)
        set_skill(triggerIds=[2403], isEnable=False)
        set_skill(triggerIds=[2404], isEnable=False)
        set_skill(triggerIds=[2405], isEnable=False)
        set_skill(triggerIds=[2406], isEnable=False)
        set_skill(triggerIds=[2407], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬18()


class 스킬18(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2401], isEnable=True)
        set_skill(triggerIds=[2402], isEnable=True)
        set_skill(triggerIds=[2403], isEnable=True)
        set_skill(triggerIds=[2404], isEnable=True)
        set_skill(triggerIds=[2405], isEnable=True)
        set_skill(triggerIds=[2406], isEnable=True)
        set_skill(triggerIds=[2407], isEnable=True)
        set_skill(triggerIds=[2408], isEnable=True)
        set_skill(triggerIds=[2409], isEnable=True)
        set_skill(triggerIds=[2410], isEnable=True)
        set_skill(triggerIds=[2411], isEnable=True)
        set_skill(triggerIds=[2412], isEnable=True)
        set_skill(triggerIds=[2413], isEnable=True)
        set_skill(triggerIds=[2414], isEnable=True)
        set_skill(triggerIds=[2415], isEnable=True)
        set_skill(triggerIds=[2416], isEnable=True)
        set_skill(triggerIds=[2417], isEnable=True)
        set_skill(triggerIds=[2418], isEnable=True)
        set_skill(triggerIds=[2419], isEnable=True)
        set_skill(triggerIds=[2420], isEnable=True)
        set_skill(triggerIds=[2421], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬19대기()


class 스킬19대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2401], isEnable=False)
        set_skill(triggerIds=[2402], isEnable=False)
        set_skill(triggerIds=[2403], isEnable=False)
        set_skill(triggerIds=[2404], isEnable=False)
        set_skill(triggerIds=[2405], isEnable=False)
        set_skill(triggerIds=[2406], isEnable=False)
        set_skill(triggerIds=[2407], isEnable=False)
        set_skill(triggerIds=[2408], isEnable=False)
        set_skill(triggerIds=[2409], isEnable=False)
        set_skill(triggerIds=[2410], isEnable=False)
        set_skill(triggerIds=[2411], isEnable=False)
        set_skill(triggerIds=[2412], isEnable=False)
        set_skill(triggerIds=[2413], isEnable=False)
        set_skill(triggerIds=[2414], isEnable=False)
        set_skill(triggerIds=[2415], isEnable=False)
        set_skill(triggerIds=[2416], isEnable=False)
        set_skill(triggerIds=[2417], isEnable=False)
        set_skill(triggerIds=[2418], isEnable=False)
        set_skill(triggerIds=[2419], isEnable=False)
        set_skill(triggerIds=[2420], isEnable=False)
        set_skill(triggerIds=[2421], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬19()


class 스킬19(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2408], isEnable=True)
        set_skill(triggerIds=[2409], isEnable=True)
        set_skill(triggerIds=[2410], isEnable=True)
        set_skill(triggerIds=[2411], isEnable=True)
        set_skill(triggerIds=[2412], isEnable=True)
        set_skill(triggerIds=[2413], isEnable=True)
        set_skill(triggerIds=[2414], isEnable=True)
        set_skill(triggerIds=[2415], isEnable=True)
        set_skill(triggerIds=[2416], isEnable=True)
        set_skill(triggerIds=[2417], isEnable=True)
        set_skill(triggerIds=[2418], isEnable=True)
        set_skill(triggerIds=[2419], isEnable=True)
        set_skill(triggerIds=[2420], isEnable=True)
        set_skill(triggerIds=[2421], isEnable=True)
        set_skill(triggerIds=[2422], isEnable=True)
        set_skill(triggerIds=[2423], isEnable=True)
        set_skill(triggerIds=[2424], isEnable=True)
        set_skill(triggerIds=[2425], isEnable=True)
        set_skill(triggerIds=[2426], isEnable=True)
        set_skill(triggerIds=[2427], isEnable=True)
        set_skill(triggerIds=[2428], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬20대기()


class 스킬20대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2408], isEnable=False)
        set_skill(triggerIds=[2409], isEnable=False)
        set_skill(triggerIds=[2410], isEnable=False)
        set_skill(triggerIds=[2411], isEnable=False)
        set_skill(triggerIds=[2412], isEnable=False)
        set_skill(triggerIds=[2413], isEnable=False)
        set_skill(triggerIds=[2414], isEnable=False)
        set_skill(triggerIds=[2415], isEnable=False)
        set_skill(triggerIds=[2416], isEnable=False)
        set_skill(triggerIds=[2417], isEnable=False)
        set_skill(triggerIds=[2418], isEnable=False)
        set_skill(triggerIds=[2419], isEnable=False)
        set_skill(triggerIds=[2420], isEnable=False)
        set_skill(triggerIds=[2421], isEnable=False)
        set_skill(triggerIds=[2422], isEnable=False)
        set_skill(triggerIds=[2423], isEnable=False)
        set_skill(triggerIds=[2424], isEnable=False)
        set_skill(triggerIds=[2425], isEnable=False)
        set_skill(triggerIds=[2426], isEnable=False)
        set_skill(triggerIds=[2427], isEnable=False)
        set_skill(triggerIds=[2428], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬20()


class 스킬20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2415], isEnable=True)
        set_skill(triggerIds=[2416], isEnable=True)
        set_skill(triggerIds=[2417], isEnable=True)
        set_skill(triggerIds=[2418], isEnable=True)
        set_skill(triggerIds=[2419], isEnable=True)
        set_skill(triggerIds=[2420], isEnable=True)
        set_skill(triggerIds=[2421], isEnable=True)
        set_skill(triggerIds=[2422], isEnable=True)
        set_skill(triggerIds=[2423], isEnable=True)
        set_skill(triggerIds=[2424], isEnable=True)
        set_skill(triggerIds=[2425], isEnable=True)
        set_skill(triggerIds=[2426], isEnable=True)
        set_skill(triggerIds=[2427], isEnable=True)
        set_skill(triggerIds=[2428], isEnable=True)
        set_skill(triggerIds=[2429], isEnable=True)
        set_skill(triggerIds=[2430], isEnable=True)
        set_skill(triggerIds=[2431], isEnable=True)
        set_skill(triggerIds=[2432], isEnable=True)
        set_skill(triggerIds=[2433], isEnable=True)
        set_skill(triggerIds=[2434], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬21대기()


class 스킬21대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2415], isEnable=False)
        set_skill(triggerIds=[2416], isEnable=False)
        set_skill(triggerIds=[2417], isEnable=False)
        set_skill(triggerIds=[2418], isEnable=False)
        set_skill(triggerIds=[2419], isEnable=False)
        set_skill(triggerIds=[2420], isEnable=False)
        set_skill(triggerIds=[2421], isEnable=False)
        set_skill(triggerIds=[2422], isEnable=False)
        set_skill(triggerIds=[2423], isEnable=False)
        set_skill(triggerIds=[2424], isEnable=False)
        set_skill(triggerIds=[2425], isEnable=False)
        set_skill(triggerIds=[2426], isEnable=False)
        set_skill(triggerIds=[2427], isEnable=False)
        set_skill(triggerIds=[2428], isEnable=False)
        set_skill(triggerIds=[2429], isEnable=False)
        set_skill(triggerIds=[2430], isEnable=False)
        set_skill(triggerIds=[2431], isEnable=False)
        set_skill(triggerIds=[2432], isEnable=False)
        set_skill(triggerIds=[2433], isEnable=False)
        set_skill(triggerIds=[2434], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬21()


class 스킬21(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2422], isEnable=True)
        set_skill(triggerIds=[2423], isEnable=True)
        set_skill(triggerIds=[2424], isEnable=True)
        set_skill(triggerIds=[2425], isEnable=True)
        set_skill(triggerIds=[2426], isEnable=True)
        set_skill(triggerIds=[2427], isEnable=True)
        set_skill(triggerIds=[2428], isEnable=True)
        set_skill(triggerIds=[2429], isEnable=True)
        set_skill(triggerIds=[2430], isEnable=True)
        set_skill(triggerIds=[2431], isEnable=True)
        set_skill(triggerIds=[2432], isEnable=True)
        set_skill(triggerIds=[2433], isEnable=True)
        set_skill(triggerIds=[2434], isEnable=True)
        set_skill(triggerIds=[2435], isEnable=True)
        set_skill(triggerIds=[2436], isEnable=True)
        set_skill(triggerIds=[2437], isEnable=True)
        set_skill(triggerIds=[2438], isEnable=True)
        set_skill(triggerIds=[2439], isEnable=True)
        set_skill(triggerIds=[2440], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬22대기()


class 스킬22대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2422], isEnable=False)
        set_skill(triggerIds=[2423], isEnable=False)
        set_skill(triggerIds=[2424], isEnable=False)
        set_skill(triggerIds=[2425], isEnable=False)
        set_skill(triggerIds=[2426], isEnable=False)
        set_skill(triggerIds=[2427], isEnable=False)
        set_skill(triggerIds=[2428], isEnable=False)
        set_skill(triggerIds=[2429], isEnable=False)
        set_skill(triggerIds=[2430], isEnable=False)
        set_skill(triggerIds=[2431], isEnable=False)
        set_skill(triggerIds=[2432], isEnable=False)
        set_skill(triggerIds=[2433], isEnable=False)
        set_skill(triggerIds=[2434], isEnable=False)
        set_skill(triggerIds=[2435], isEnable=False)
        set_skill(triggerIds=[2436], isEnable=False)
        set_skill(triggerIds=[2437], isEnable=False)
        set_skill(triggerIds=[2438], isEnable=False)
        set_skill(triggerIds=[2439], isEnable=False)
        set_skill(triggerIds=[2440], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬22()


class 스킬22(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2429], isEnable=True)
        set_skill(triggerIds=[2430], isEnable=True)
        set_skill(triggerIds=[2431], isEnable=True)
        set_skill(triggerIds=[2432], isEnable=True)
        set_skill(triggerIds=[2433], isEnable=True)
        set_skill(triggerIds=[2434], isEnable=True)
        set_skill(triggerIds=[2435], isEnable=True)
        set_skill(triggerIds=[2436], isEnable=True)
        set_skill(triggerIds=[2437], isEnable=True)
        set_skill(triggerIds=[2438], isEnable=True)
        set_skill(triggerIds=[2439], isEnable=True)
        set_skill(triggerIds=[2440], isEnable=True)
        set_skill(triggerIds=[2441], isEnable=True)
        set_skill(triggerIds=[2442], isEnable=True)
        set_skill(triggerIds=[2443], isEnable=True)
        set_skill(triggerIds=[2444], isEnable=True)
        set_skill(triggerIds=[2445], isEnable=True)
        set_skill(triggerIds=[2446], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬23대기()


class 스킬23대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2429], isEnable=False)
        set_skill(triggerIds=[2430], isEnable=False)
        set_skill(triggerIds=[2431], isEnable=False)
        set_skill(triggerIds=[2432], isEnable=False)
        set_skill(triggerIds=[2433], isEnable=False)
        set_skill(triggerIds=[2434], isEnable=False)
        set_skill(triggerIds=[2435], isEnable=False)
        set_skill(triggerIds=[2436], isEnable=False)
        set_skill(triggerIds=[2437], isEnable=False)
        set_skill(triggerIds=[2438], isEnable=False)
        set_skill(triggerIds=[2439], isEnable=False)
        set_skill(triggerIds=[2440], isEnable=False)
        set_skill(triggerIds=[2441], isEnable=False)
        set_skill(triggerIds=[2442], isEnable=False)
        set_skill(triggerIds=[2443], isEnable=False)
        set_skill(triggerIds=[2444], isEnable=False)
        set_skill(triggerIds=[2445], isEnable=False)
        set_skill(triggerIds=[2446], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬23()


class 스킬23(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2435], isEnable=True)
        set_skill(triggerIds=[2436], isEnable=True)
        set_skill(triggerIds=[2437], isEnable=True)
        set_skill(triggerIds=[2438], isEnable=True)
        set_skill(triggerIds=[2439], isEnable=True)
        set_skill(triggerIds=[2440], isEnable=True)
        set_skill(triggerIds=[2441], isEnable=True)
        set_skill(triggerIds=[2442], isEnable=True)
        set_skill(triggerIds=[2443], isEnable=True)
        set_skill(triggerIds=[2444], isEnable=True)
        set_skill(triggerIds=[2445], isEnable=True)
        set_skill(triggerIds=[2446], isEnable=True)
        set_skill(triggerIds=[2447], isEnable=True)
        set_skill(triggerIds=[2448], isEnable=True)
        set_skill(triggerIds=[2449], isEnable=True)
        set_skill(triggerIds=[2450], isEnable=True)
        set_skill(triggerIds=[2451], isEnable=True)
        set_skill(triggerIds=[2452], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬24대기()


class 스킬24대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2435], isEnable=False)
        set_skill(triggerIds=[2436], isEnable=False)
        set_skill(triggerIds=[2437], isEnable=False)
        set_skill(triggerIds=[2438], isEnable=False)
        set_skill(triggerIds=[2439], isEnable=False)
        set_skill(triggerIds=[2440], isEnable=False)
        set_skill(triggerIds=[2441], isEnable=False)
        set_skill(triggerIds=[2442], isEnable=False)
        set_skill(triggerIds=[2443], isEnable=False)
        set_skill(triggerIds=[2444], isEnable=False)
        set_skill(triggerIds=[2445], isEnable=False)
        set_skill(triggerIds=[2446], isEnable=False)
        set_skill(triggerIds=[2447], isEnable=False)
        set_skill(triggerIds=[2448], isEnable=False)
        set_skill(triggerIds=[2449], isEnable=False)
        set_skill(triggerIds=[2450], isEnable=False)
        set_skill(triggerIds=[2451], isEnable=False)
        set_skill(triggerIds=[2452], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬24()


class 스킬24(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2441], isEnable=True)
        set_skill(triggerIds=[2442], isEnable=True)
        set_skill(triggerIds=[2443], isEnable=True)
        set_skill(triggerIds=[2444], isEnable=True)
        set_skill(triggerIds=[2445], isEnable=True)
        set_skill(triggerIds=[2446], isEnable=True)
        set_skill(triggerIds=[2447], isEnable=True)
        set_skill(triggerIds=[2448], isEnable=True)
        set_skill(triggerIds=[2449], isEnable=True)
        set_skill(triggerIds=[2450], isEnable=True)
        set_skill(triggerIds=[2451], isEnable=True)
        set_skill(triggerIds=[2452], isEnable=True)
        set_skill(triggerIds=[2453], isEnable=True)
        set_skill(triggerIds=[2454], isEnable=True)
        set_skill(triggerIds=[2455], isEnable=True)
        set_skill(triggerIds=[2456], isEnable=True)
        set_skill(triggerIds=[2457], isEnable=True)
        set_skill(triggerIds=[2458], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬25대기()


class 스킬25대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2441], isEnable=False)
        set_skill(triggerIds=[2442], isEnable=False)
        set_skill(triggerIds=[2443], isEnable=False)
        set_skill(triggerIds=[2444], isEnable=False)
        set_skill(triggerIds=[2445], isEnable=False)
        set_skill(triggerIds=[2446], isEnable=False)
        set_skill(triggerIds=[2447], isEnable=False)
        set_skill(triggerIds=[2448], isEnable=False)
        set_skill(triggerIds=[2449], isEnable=False)
        set_skill(triggerIds=[2450], isEnable=False)
        set_skill(triggerIds=[2451], isEnable=False)
        set_skill(triggerIds=[2452], isEnable=False)
        set_skill(triggerIds=[2453], isEnable=False)
        set_skill(triggerIds=[2454], isEnable=False)
        set_skill(triggerIds=[2455], isEnable=False)
        set_skill(triggerIds=[2456], isEnable=False)
        set_skill(triggerIds=[2457], isEnable=False)
        set_skill(triggerIds=[2458], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬25()


class 스킬25(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2447], isEnable=True)
        set_skill(triggerIds=[2448], isEnable=True)
        set_skill(triggerIds=[2449], isEnable=True)
        set_skill(triggerIds=[2450], isEnable=True)
        set_skill(triggerIds=[2451], isEnable=True)
        set_skill(triggerIds=[2452], isEnable=True)
        set_skill(triggerIds=[2453], isEnable=True)
        set_skill(triggerIds=[2454], isEnable=True)
        set_skill(triggerIds=[2455], isEnable=True)
        set_skill(triggerIds=[2456], isEnable=True)
        set_skill(triggerIds=[2457], isEnable=True)
        set_skill(triggerIds=[2458], isEnable=True)
        set_skill(triggerIds=[2459], isEnable=True)
        set_skill(triggerIds=[2460], isEnable=True)
        set_skill(triggerIds=[2461], isEnable=True)
        set_skill(triggerIds=[2462], isEnable=True)
        set_skill(triggerIds=[2463], isEnable=True)
        set_skill(triggerIds=[2464], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬26대기()


class 스킬26대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2447], isEnable=False)
        set_skill(triggerIds=[2448], isEnable=False)
        set_skill(triggerIds=[2449], isEnable=False)
        set_skill(triggerIds=[2450], isEnable=False)
        set_skill(triggerIds=[2451], isEnable=False)
        set_skill(triggerIds=[2452], isEnable=False)
        set_skill(triggerIds=[2453], isEnable=False)
        set_skill(triggerIds=[2454], isEnable=False)
        set_skill(triggerIds=[2455], isEnable=False)
        set_skill(triggerIds=[2456], isEnable=False)
        set_skill(triggerIds=[2457], isEnable=False)
        set_skill(triggerIds=[2458], isEnable=False)
        set_skill(triggerIds=[2459], isEnable=False)
        set_skill(triggerIds=[2460], isEnable=False)
        set_skill(triggerIds=[2461], isEnable=False)
        set_skill(triggerIds=[2462], isEnable=False)
        set_skill(triggerIds=[2463], isEnable=False)
        set_skill(triggerIds=[2464], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬26()


class 스킬26(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2453], isEnable=True)
        set_skill(triggerIds=[2454], isEnable=True)
        set_skill(triggerIds=[2455], isEnable=True)
        set_skill(triggerIds=[2456], isEnable=True)
        set_skill(triggerIds=[2457], isEnable=True)
        set_skill(triggerIds=[2458], isEnable=True)
        set_skill(triggerIds=[2459], isEnable=True)
        set_skill(triggerIds=[2460], isEnable=True)
        set_skill(triggerIds=[2461], isEnable=True)
        set_skill(triggerIds=[2462], isEnable=True)
        set_skill(triggerIds=[2463], isEnable=True)
        set_skill(triggerIds=[2464], isEnable=True)
        set_skill(triggerIds=[2465], isEnable=True)
        set_skill(triggerIds=[2466], isEnable=True)
        set_skill(triggerIds=[2467], isEnable=True)
        set_skill(triggerIds=[2468], isEnable=True)
        set_skill(triggerIds=[2469], isEnable=True)
        set_skill(triggerIds=[2470], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬27대기()


class 스킬27대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2453], isEnable=False)
        set_skill(triggerIds=[2454], isEnable=False)
        set_skill(triggerIds=[2455], isEnable=False)
        set_skill(triggerIds=[2456], isEnable=False)
        set_skill(triggerIds=[2457], isEnable=False)
        set_skill(triggerIds=[2458], isEnable=False)
        set_skill(triggerIds=[2459], isEnable=False)
        set_skill(triggerIds=[2460], isEnable=False)
        set_skill(triggerIds=[2461], isEnable=False)
        set_skill(triggerIds=[2462], isEnable=False)
        set_skill(triggerIds=[2463], isEnable=False)
        set_skill(triggerIds=[2464], isEnable=False)
        set_skill(triggerIds=[2465], isEnable=False)
        set_skill(triggerIds=[2466], isEnable=False)
        set_skill(triggerIds=[2467], isEnable=False)
        set_skill(triggerIds=[2468], isEnable=False)
        set_skill(triggerIds=[2469], isEnable=False)
        set_skill(triggerIds=[2470], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬27()


class 스킬27(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2459], isEnable=True)
        set_skill(triggerIds=[2460], isEnable=True)
        set_skill(triggerIds=[2461], isEnable=True)
        set_skill(triggerIds=[2462], isEnable=True)
        set_skill(triggerIds=[2463], isEnable=True)
        set_skill(triggerIds=[2464], isEnable=True)
        set_skill(triggerIds=[2465], isEnable=True)
        set_skill(triggerIds=[2466], isEnable=True)
        set_skill(triggerIds=[2467], isEnable=True)
        set_skill(triggerIds=[2468], isEnable=True)
        set_skill(triggerIds=[2469], isEnable=True)
        set_skill(triggerIds=[2470], isEnable=True)
        set_skill(triggerIds=[2471], isEnable=True)
        set_skill(triggerIds=[2472], isEnable=True)
        set_skill(triggerIds=[2473], isEnable=True)
        set_skill(triggerIds=[2474], isEnable=True)
        set_skill(triggerIds=[2475], isEnable=True)
        set_skill(triggerIds=[2476], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬28대기()


class 스킬28대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2459], isEnable=False)
        set_skill(triggerIds=[2460], isEnable=False)
        set_skill(triggerIds=[2461], isEnable=False)
        set_skill(triggerIds=[2462], isEnable=False)
        set_skill(triggerIds=[2463], isEnable=False)
        set_skill(triggerIds=[2464], isEnable=False)
        set_skill(triggerIds=[2465], isEnable=False)
        set_skill(triggerIds=[2466], isEnable=False)
        set_skill(triggerIds=[2467], isEnable=False)
        set_skill(triggerIds=[2468], isEnable=False)
        set_skill(triggerIds=[2469], isEnable=False)
        set_skill(triggerIds=[2470], isEnable=False)
        set_skill(triggerIds=[2471], isEnable=False)
        set_skill(triggerIds=[2472], isEnable=False)
        set_skill(triggerIds=[2473], isEnable=False)
        set_skill(triggerIds=[2474], isEnable=False)
        set_skill(triggerIds=[2475], isEnable=False)
        set_skill(triggerIds=[2476], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬28()


class 스킬28(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2465], isEnable=True)
        set_skill(triggerIds=[2466], isEnable=True)
        set_skill(triggerIds=[2467], isEnable=True)
        set_skill(triggerIds=[2468], isEnable=True)
        set_skill(triggerIds=[2469], isEnable=True)
        set_skill(triggerIds=[2470], isEnable=True)
        set_skill(triggerIds=[2471], isEnable=True)
        set_skill(triggerIds=[2472], isEnable=True)
        set_skill(triggerIds=[2473], isEnable=True)
        set_skill(triggerIds=[2474], isEnable=True)
        set_skill(triggerIds=[2475], isEnable=True)
        set_skill(triggerIds=[2476], isEnable=True)
        set_skill(triggerIds=[2477], isEnable=True)
        set_skill(triggerIds=[2478], isEnable=True)
        set_skill(triggerIds=[2479], isEnable=True)
        set_skill(triggerIds=[2480], isEnable=True)
        set_skill(triggerIds=[2481], isEnable=True)
        set_skill(triggerIds=[2482], isEnable=True)
        set_skill(triggerIds=[2483], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬29대기()


class 스킬29대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2465], isEnable=False)
        set_skill(triggerIds=[2466], isEnable=False)
        set_skill(triggerIds=[2467], isEnable=False)
        set_skill(triggerIds=[2468], isEnable=False)
        set_skill(triggerIds=[2469], isEnable=False)
        set_skill(triggerIds=[2470], isEnable=False)
        set_skill(triggerIds=[2471], isEnable=False)
        set_skill(triggerIds=[2472], isEnable=False)
        set_skill(triggerIds=[2473], isEnable=False)
        set_skill(triggerIds=[2474], isEnable=False)
        set_skill(triggerIds=[2475], isEnable=False)
        set_skill(triggerIds=[2476], isEnable=False)
        set_skill(triggerIds=[2477], isEnable=False)
        set_skill(triggerIds=[2478], isEnable=False)
        set_skill(triggerIds=[2479], isEnable=False)
        set_skill(triggerIds=[2480], isEnable=False)
        set_skill(triggerIds=[2481], isEnable=False)
        set_skill(triggerIds=[2482], isEnable=False)
        set_skill(triggerIds=[2483], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬29()


class 스킬29(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2471], isEnable=True)
        set_skill(triggerIds=[2472], isEnable=True)
        set_skill(triggerIds=[2473], isEnable=True)
        set_skill(triggerIds=[2474], isEnable=True)
        set_skill(triggerIds=[2475], isEnable=True)
        set_skill(triggerIds=[2476], isEnable=True)
        set_skill(triggerIds=[2477], isEnable=True)
        set_skill(triggerIds=[2478], isEnable=True)
        set_skill(triggerIds=[2479], isEnable=True)
        set_skill(triggerIds=[2480], isEnable=True)
        set_skill(triggerIds=[2481], isEnable=True)
        set_skill(triggerIds=[2482], isEnable=True)
        set_skill(triggerIds=[2483], isEnable=True)
        set_skill(triggerIds=[2484], isEnable=True)
        set_skill(triggerIds=[2485], isEnable=True)
        set_skill(triggerIds=[2486], isEnable=True)
        set_skill(triggerIds=[2487], isEnable=True)
        set_skill(triggerIds=[2488], isEnable=True)
        set_skill(triggerIds=[2489], isEnable=True)
        set_skill(triggerIds=[2490], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬30대기()


class 스킬30대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2471], isEnable=False)
        set_skill(triggerIds=[2472], isEnable=False)
        set_skill(triggerIds=[2473], isEnable=False)
        set_skill(triggerIds=[2474], isEnable=False)
        set_skill(triggerIds=[2475], isEnable=False)
        set_skill(triggerIds=[2476], isEnable=False)
        set_skill(triggerIds=[2477], isEnable=False)
        set_skill(triggerIds=[2478], isEnable=False)
        set_skill(triggerIds=[2479], isEnable=False)
        set_skill(triggerIds=[2480], isEnable=False)
        set_skill(triggerIds=[2481], isEnable=False)
        set_skill(triggerIds=[2482], isEnable=False)
        set_skill(triggerIds=[2483], isEnable=False)
        set_skill(triggerIds=[2484], isEnable=False)
        set_skill(triggerIds=[2485], isEnable=False)
        set_skill(triggerIds=[2486], isEnable=False)
        set_skill(triggerIds=[2487], isEnable=False)
        set_skill(triggerIds=[2488], isEnable=False)
        set_skill(triggerIds=[2489], isEnable=False)
        set_skill(triggerIds=[2490], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬30()


class 스킬30(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2477], isEnable=True)
        set_skill(triggerIds=[2478], isEnable=True)
        set_skill(triggerIds=[2479], isEnable=True)
        set_skill(triggerIds=[2480], isEnable=True)
        set_skill(triggerIds=[2481], isEnable=True)
        set_skill(triggerIds=[2482], isEnable=True)
        set_skill(triggerIds=[2483], isEnable=True)
        set_skill(triggerIds=[2484], isEnable=True)
        set_skill(triggerIds=[2485], isEnable=True)
        set_skill(triggerIds=[2486], isEnable=True)
        set_skill(triggerIds=[2487], isEnable=True)
        set_skill(triggerIds=[2488], isEnable=True)
        set_skill(triggerIds=[2489], isEnable=True)
        set_skill(triggerIds=[2490], isEnable=True)
        set_skill(triggerIds=[2491], isEnable=True)
        set_skill(triggerIds=[2492], isEnable=True)
        set_skill(triggerIds=[2493], isEnable=True)
        set_skill(triggerIds=[2494], isEnable=True)
        set_skill(triggerIds=[2495], isEnable=True)
        set_skill(triggerIds=[2496], isEnable=True)
        set_skill(triggerIds=[2497], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬31대기()


class 스킬31대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2477], isEnable=False)
        set_skill(triggerIds=[2478], isEnable=False)
        set_skill(triggerIds=[2479], isEnable=False)
        set_skill(triggerIds=[2480], isEnable=False)
        set_skill(triggerIds=[2481], isEnable=False)
        set_skill(triggerIds=[2482], isEnable=False)
        set_skill(triggerIds=[2483], isEnable=False)
        set_skill(triggerIds=[2484], isEnable=False)
        set_skill(triggerIds=[2485], isEnable=False)
        set_skill(triggerIds=[2486], isEnable=False)
        set_skill(triggerIds=[2487], isEnable=False)
        set_skill(triggerIds=[2488], isEnable=False)
        set_skill(triggerIds=[2489], isEnable=False)
        set_skill(triggerIds=[2490], isEnable=False)
        set_skill(triggerIds=[2491], isEnable=False)
        set_skill(triggerIds=[2492], isEnable=False)
        set_skill(triggerIds=[2493], isEnable=False)
        set_skill(triggerIds=[2494], isEnable=False)
        set_skill(triggerIds=[2495], isEnable=False)
        set_skill(triggerIds=[2496], isEnable=False)
        set_skill(triggerIds=[2497], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬31()


class 스킬31(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2484], isEnable=True)
        set_skill(triggerIds=[2485], isEnable=True)
        set_skill(triggerIds=[2486], isEnable=True)
        set_skill(triggerIds=[2487], isEnable=True)
        set_skill(triggerIds=[2488], isEnable=True)
        set_skill(triggerIds=[2489], isEnable=True)
        set_skill(triggerIds=[2490], isEnable=True)
        set_skill(triggerIds=[2491], isEnable=True)
        set_skill(triggerIds=[2492], isEnable=True)
        set_skill(triggerIds=[2493], isEnable=True)
        set_skill(triggerIds=[2494], isEnable=True)
        set_skill(triggerIds=[2495], isEnable=True)
        set_skill(triggerIds=[2496], isEnable=True)
        set_skill(triggerIds=[2497], isEnable=True)
        set_skill(triggerIds=[2498], isEnable=True)
        set_skill(triggerIds=[2499], isEnable=True)
        set_skill(triggerIds=[2500], isEnable=True)
        set_skill(triggerIds=[2501], isEnable=True)
        set_skill(triggerIds=[2502], isEnable=True)
        set_skill(triggerIds=[2503], isEnable=True)
        set_skill(triggerIds=[2504], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬32대기()


class 스킬32대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2484], isEnable=False)
        set_skill(triggerIds=[2485], isEnable=False)
        set_skill(triggerIds=[2486], isEnable=False)
        set_skill(triggerIds=[2487], isEnable=False)
        set_skill(triggerIds=[2488], isEnable=False)
        set_skill(triggerIds=[2489], isEnable=False)
        set_skill(triggerIds=[2490], isEnable=False)
        set_skill(triggerIds=[2491], isEnable=False)
        set_skill(triggerIds=[2492], isEnable=False)
        set_skill(triggerIds=[2493], isEnable=False)
        set_skill(triggerIds=[2494], isEnable=False)
        set_skill(triggerIds=[2495], isEnable=False)
        set_skill(triggerIds=[2496], isEnable=False)
        set_skill(triggerIds=[2497], isEnable=False)
        set_skill(triggerIds=[2498], isEnable=False)
        set_skill(triggerIds=[2499], isEnable=False)
        set_skill(triggerIds=[2500], isEnable=False)
        set_skill(triggerIds=[2501], isEnable=False)
        set_skill(triggerIds=[2502], isEnable=False)
        set_skill(triggerIds=[2503], isEnable=False)
        set_skill(triggerIds=[2504], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬32()


class 스킬32(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2491], isEnable=True)
        set_skill(triggerIds=[2492], isEnable=True)
        set_skill(triggerIds=[2493], isEnable=True)
        set_skill(triggerIds=[2494], isEnable=True)
        set_skill(triggerIds=[2495], isEnable=True)
        set_skill(triggerIds=[2496], isEnable=True)
        set_skill(triggerIds=[2497], isEnable=True)
        set_skill(triggerIds=[2498], isEnable=True)
        set_skill(triggerIds=[2499], isEnable=True)
        set_skill(triggerIds=[2500], isEnable=True)
        set_skill(triggerIds=[2501], isEnable=True)
        set_skill(triggerIds=[2502], isEnable=True)
        set_skill(triggerIds=[2503], isEnable=True)
        set_skill(triggerIds=[2504], isEnable=True)
        set_skill(triggerIds=[2505], isEnable=True)
        set_skill(triggerIds=[2506], isEnable=True)
        set_skill(triggerIds=[2507], isEnable=True)
        set_skill(triggerIds=[2508], isEnable=True)
        set_skill(triggerIds=[2509], isEnable=True)
        set_skill(triggerIds=[2510], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬33대기()


class 스킬33대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2491], isEnable=False)
        set_skill(triggerIds=[2492], isEnable=False)
        set_skill(triggerIds=[2493], isEnable=False)
        set_skill(triggerIds=[2494], isEnable=False)
        set_skill(triggerIds=[2495], isEnable=False)
        set_skill(triggerIds=[2496], isEnable=False)
        set_skill(triggerIds=[2497], isEnable=False)
        set_skill(triggerIds=[2498], isEnable=False)
        set_skill(triggerIds=[2499], isEnable=False)
        set_skill(triggerIds=[2500], isEnable=False)
        set_skill(triggerIds=[2501], isEnable=False)
        set_skill(triggerIds=[2502], isEnable=False)
        set_skill(triggerIds=[2503], isEnable=False)
        set_skill(triggerIds=[2504], isEnable=False)
        set_skill(triggerIds=[2505], isEnable=False)
        set_skill(triggerIds=[2506], isEnable=False)
        set_skill(triggerIds=[2507], isEnable=False)
        set_skill(triggerIds=[2508], isEnable=False)
        set_skill(triggerIds=[2509], isEnable=False)
        set_skill(triggerIds=[2510], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬33()


class 스킬33(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2498], isEnable=True)
        set_skill(triggerIds=[2499], isEnable=True)
        set_skill(triggerIds=[2500], isEnable=True)
        set_skill(triggerIds=[2501], isEnable=True)
        set_skill(triggerIds=[2502], isEnable=True)
        set_skill(triggerIds=[2503], isEnable=True)
        set_skill(triggerIds=[2504], isEnable=True)
        set_skill(triggerIds=[2505], isEnable=True)
        set_skill(triggerIds=[2506], isEnable=True)
        set_skill(triggerIds=[2507], isEnable=True)
        set_skill(triggerIds=[2508], isEnable=True)
        set_skill(triggerIds=[2509], isEnable=True)
        set_skill(triggerIds=[2510], isEnable=True)
        set_skill(triggerIds=[2511], isEnable=True)
        set_skill(triggerIds=[2512], isEnable=True)
        set_skill(triggerIds=[2513], isEnable=True)
        set_skill(triggerIds=[2514], isEnable=True)
        set_skill(triggerIds=[2515], isEnable=True)
        set_skill(triggerIds=[2516], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬34대기()


class 스킬34대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2498], isEnable=False)
        set_skill(triggerIds=[2499], isEnable=False)
        set_skill(triggerIds=[2500], isEnable=False)
        set_skill(triggerIds=[2501], isEnable=False)
        set_skill(triggerIds=[2502], isEnable=False)
        set_skill(triggerIds=[2503], isEnable=False)
        set_skill(triggerIds=[2504], isEnable=False)
        set_skill(triggerIds=[2505], isEnable=False)
        set_skill(triggerIds=[2506], isEnable=False)
        set_skill(triggerIds=[2507], isEnable=False)
        set_skill(triggerIds=[2508], isEnable=False)
        set_skill(triggerIds=[2509], isEnable=False)
        set_skill(triggerIds=[2510], isEnable=False)
        set_skill(triggerIds=[2511], isEnable=False)
        set_skill(triggerIds=[2512], isEnable=False)
        set_skill(triggerIds=[2513], isEnable=False)
        set_skill(triggerIds=[2514], isEnable=False)
        set_skill(triggerIds=[2515], isEnable=False)
        set_skill(triggerIds=[2516], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬34()


class 스킬34(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2505], isEnable=True)
        set_skill(triggerIds=[2506], isEnable=True)
        set_skill(triggerIds=[2507], isEnable=True)
        set_skill(triggerIds=[2508], isEnable=True)
        set_skill(triggerIds=[2509], isEnable=True)
        set_skill(triggerIds=[2510], isEnable=True)
        set_skill(triggerIds=[2511], isEnable=True)
        set_skill(triggerIds=[2512], isEnable=True)
        set_skill(triggerIds=[2513], isEnable=True)
        set_skill(triggerIds=[2514], isEnable=True)
        set_skill(triggerIds=[2515], isEnable=True)
        set_skill(triggerIds=[2516], isEnable=True)
        set_skill(triggerIds=[2517], isEnable=True)
        set_skill(triggerIds=[2518], isEnable=True)
        set_skill(triggerIds=[2519], isEnable=True)
        set_skill(triggerIds=[2520], isEnable=True)
        set_skill(triggerIds=[2521], isEnable=True)
        set_skill(triggerIds=[2522], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬35대기()


class 스킬35대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2505], isEnable=False)
        set_skill(triggerIds=[2506], isEnable=False)
        set_skill(triggerIds=[2507], isEnable=False)
        set_skill(triggerIds=[2508], isEnable=False)
        set_skill(triggerIds=[2509], isEnable=False)
        set_skill(triggerIds=[2510], isEnable=False)
        set_skill(triggerIds=[2511], isEnable=False)
        set_skill(triggerIds=[2512], isEnable=False)
        set_skill(triggerIds=[2513], isEnable=False)
        set_skill(triggerIds=[2514], isEnable=False)
        set_skill(triggerIds=[2515], isEnable=False)
        set_skill(triggerIds=[2516], isEnable=False)
        set_skill(triggerIds=[2517], isEnable=False)
        set_skill(triggerIds=[2518], isEnable=False)
        set_skill(triggerIds=[2519], isEnable=False)
        set_skill(triggerIds=[2520], isEnable=False)
        set_skill(triggerIds=[2521], isEnable=False)
        set_skill(triggerIds=[2522], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if true():
            return 스킬35()


class 스킬35(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2511], isEnable=True)
        set_skill(triggerIds=[2512], isEnable=True)
        set_skill(triggerIds=[2513], isEnable=True)
        set_skill(triggerIds=[2514], isEnable=True)
        set_skill(triggerIds=[2515], isEnable=True)
        set_skill(triggerIds=[2516], isEnable=True)
        set_skill(triggerIds=[2517], isEnable=True)
        set_skill(triggerIds=[2518], isEnable=True)
        set_skill(triggerIds=[2519], isEnable=True)
        set_skill(triggerIds=[2520], isEnable=True)
        set_skill(triggerIds=[2521], isEnable=True)
        set_skill(triggerIds=[2522], isEnable=True)
        set_skill(triggerIds=[2523], isEnable=True)
        set_skill(triggerIds=[2524], isEnable=True)
        set_skill(triggerIds=[2525], isEnable=True)
        set_skill(triggerIds=[2526], isEnable=True)
        set_skill(triggerIds=[2527], isEnable=True)
        set_skill(triggerIds=[2528], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()
        if time_expired(timerId='1'):
            return 스킬36대기()


class 스킬36대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2511], isEnable=False)
        set_skill(triggerIds=[2512], isEnable=False)
        set_skill(triggerIds=[2513], isEnable=False)
        set_skill(triggerIds=[2514], isEnable=False)
        set_skill(triggerIds=[2515], isEnable=False)
        set_skill(triggerIds=[2516], isEnable=False)
        set_skill(triggerIds=[2517], isEnable=False)
        set_skill(triggerIds=[2518], isEnable=False)
        set_skill(triggerIds=[2519], isEnable=False)
        set_skill(triggerIds=[2520], isEnable=False)
        set_skill(triggerIds=[2521], isEnable=False)
        set_skill(triggerIds=[2522], isEnable=False)
        set_skill(triggerIds=[2523], isEnable=False)
        set_skill(triggerIds=[2524], isEnable=False)
        set_skill(triggerIds=[2525], isEnable=False)
        set_skill(triggerIds=[2526], isEnable=False)
        set_skill(triggerIds=[2527], isEnable=False)
        set_skill(triggerIds=[2528], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 게임오버()


class 게임오버(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 강제이동()


class 강제이동(state.State):
    pass


