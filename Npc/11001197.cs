using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001197: Ropey
/// </summary>
public class _11001197 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016142906000509$
    // - Only those who know the true value of Trophies can appreciate the value I offer.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016142906000512$
                // - What's this? What business do you have with the Trophy expert? Are you interested in Trophies?
                switch (selection) {
                    // $script:1016142906000513$
                    // - Isn't everyone interested in Trophies?
                    case 0:
                        return 31;
                    // $script:1016142906000514$
                    // - I don't have time for useless junk like Trophies.
                    case 1:
                        return 34;
                }
                return -1;
            case (31, 0):
                // $script:1016142906000515$
                // - Ah, another Trophy connoisseur like myself! If you aspire to be an expert in Trophies like me, you'd better work hard. It'll take you a long time to become as savvy as I!
                switch (selection) {
                    // $script:1016142906000516$
                    // - What do I get if I have a lot of Trophies?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1016142906000517$
                // - Hmpf! Collecting Trophies is about more than just what you can get! Of course, there are precious few who collect for the sheer joy of it anymore.
                return 32;
            case (32, 1):
                // $script:1016142906000518$
                // - In any case, I have some Trophies, and I'm always looking for more. You can never have enough Trophies, you know! If you happen to find any, I'll trade something equally valuable for them.
                switch (selection) {
                    // $script:1016142906000519$
                    // - Do you even have something equally valuable?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1016142906000520$
                // - Of course I do! I've got all kinds of treasures from traveling around Maple World. I can't believe you doubt me.
                return -1;
            case (34, 0):
                // $script:1016142906000521$
                // - How dare you call my beautiful Trophies junk! Insulting my trophies is like personally insulting me, the Trophy expert! You should be ashamed of yourself for being so insulting!
                switch (selection) {
                    // $script:1016142906000522$
                    // - All right! All right! I'm sorry! I shouldn't have called them junk.
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:1016142906000523$
                // - Hmpf! I suppose I'll forgive you this time. Not everyone understands the true beauty of Trophies, after all. But don't let it happen again! Trophy experts demand respect, I tell you!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
