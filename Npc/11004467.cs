using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004467: Lenni
/// </summary>
public class _11004467 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012103$
    // - I'm worried about $npcName:11004472[gender:0]$. He's got his heart set on joining the rebellion...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012104$
                // - I'm worried about $npcName:11004472[gender:0]$. He's got his heart set on joining the rebellion...
                switch (selection) {
                    // $script:1227192907012105$
                    // - What's his story?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012106$
                // - $npcName:11004472[gender:0]$'s family was expelled from Tairen during one of the purges, so they signed on with the freedom fighters. Then... they went missing.
                return 11;
            case (11, 1):
                // $script:1227192907012107$
                // - Ever since then, he spends all his time exercising so that he can join the fight and save his family.
                switch (selection) {
                    // $script:1227192907012108$
                    // - That's so sad!
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012109$
                // - I hope he never has to see the battlefield. We told him he could be a freedom fighter if he trained hard enough, but it was really to keep him from running off and getting himself killed.
                return 12;
            case (12, 1):
                // $script:1227192907012110$
                // - And now I have to spend my free time babysitting him... Hey, you look free. Mind watching him for an hour or two?
                switch (selection) {
                    // $script:1227192907012111$
                    // - I'm actually really busy!
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1227192907012112$
                // - Hmph. You don't look like it. Oh well! I'd probably get in trouble if I left him with a stranger, anyway.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
