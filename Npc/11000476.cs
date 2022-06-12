using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000476: Goldus's Secretary
/// </summary>
public class _11000476 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002075$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002077$
                // - $map:02000100$ would never have been developed without the help of $npcName:11000252[gender:0]$!
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
