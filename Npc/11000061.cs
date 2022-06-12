using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000061: Samantha
/// </summary>
public class _11000061 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000279$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000282$
                // - If you came to see $npcName:11000016[gender:0]$, you can find him in $map:63000003$. The chief called him to talk about the ship for the court.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
