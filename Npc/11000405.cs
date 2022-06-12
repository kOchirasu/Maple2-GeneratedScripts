using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000405: Dark Wind Bulletin
/// </summary>
public class _11000405 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407001640$
    // - This is the Dark Wind Bulletin Board.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001641$
                // - Eliminate $npcName:29000023$ and bring me proof for your reward.
                //   - Captain $npcName:11000044[gender:0]$
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
