using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003893: Madria
/// </summary>
public class _11003893 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009945$
    // - Why is the $npc:11003894[gender:0]$ constantly calling meetings? What a chore!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009946$
                // - Why is the $npc:11003894[gender:0]$ constantly calling meetings? What a chore!
                return -1;
            case (30, 0):
                // $script:0515102507009947$
                // - Gah, I'm so bored. I want to head back to the castle soon.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
