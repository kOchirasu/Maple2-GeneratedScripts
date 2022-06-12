using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000075: Ereve
/// </summary>
public class _11000075 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30;40
    }

    // Select 0:
    // $script:0831180407000349$
    // - $MyPCName$, what brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000350$
                // - We must gather the $itemPlural:30000181$ as soon as possible. They are all that stand between our world and utter darkness.
                return -1;
            case (20, 0):
                // $script:0831180407000351$
                // - I've asked much of you, but there is still so much more left to do.
                return -1;
            case (30, 0):
                // $script:0831180407000352$
                // - I owe a debt of gratitude to the minister. I hope he returns soon.
                return -1;
            case (40, 0):
                // $script:0831180407000353$
                // - It was $npcName:11000044[gender:0]$ who suggested I hold an open court for the people. I suppose it was part of his plan all along...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
