using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004265: Madeng
/// </summary>
public class _11004265 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011196$
    // - Ugh, what a headache. My hard work! My paradise! This is a nightmare...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011197$
                // - Ugh, what a headache. My hard work! My paradise! This is a nightmare...
                return 10;
            case (10, 1):
                // $script:0911203207011198$
                // - Oh. Hello. Welcome to my paradise, the $map:02010058$.
                switch (selection) {
                    // $script:0911203207011199$
                    // - What's wrong? You seem really upset.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011200$
                // - It's not a good time to visit the $map:02010058$. We're dealing with some, ah, difficult guests at the moment.
                switch (selection) {
                    // $script:0911203207011201$
                    // - Who are you?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011202$
                // - Have you heard of Blackstar? The seedy group heading up all sorts of underground dealings on Maple World? Well, they arrived on Karkar not long ago, and they've taken a liking to my club...
                return 12;
            case (12, 1):
                // $script:0911203207011203$
                // - Especially that guy with the mustache. He never told me his name, but how could I not know it's $npcName:11000251[gender:0]$?
                switch (selection) {
                    // $script:0911203207011204$
                    // - Shouldn't loyal customers make you happy, even if they're seedy?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0911203207011205$
                // - Sure, business is booming, but these guys are mean! One of my waiters made a tiny mistake on an order, and those thugs pulled a gun on him. Sure, they laughed and gave him a big tip in the end, but that's not the point. I still had to buy a new mop after he peed in his pants.
                return 13;
            case (13, 1):
                // $script:0911203207011206$
                // - Listen, for me, it's about happiness, not money. I opened this joint because I was tired of being a programmer. I wanted freedom and less stress, and then this happens! I'm seriously considering closing this place and begging for my old job back.
                switch (selection) {
                    // $script:0913151207011302$
                    // - Never give up on your dreams!
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0913151207011303$
                // - My paradise! Give me back my joy!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
