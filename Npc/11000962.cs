using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000962: Rhys
/// </summary>
public class _11000962 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003342$
    // - Things aren't as good as they used to be. Ahh well. What did you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003344$
                // - The Green Hoods never surrender, no matter how bad the situation is. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
