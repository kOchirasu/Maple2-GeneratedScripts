using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003848: Condor
/// </summary>
public class _11003848 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0117175907009811$
    // - Let's get to business.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0117175907009812$
                // - In my day, we protected the world just fine without these fancy gadgets.
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
