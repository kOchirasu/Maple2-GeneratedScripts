using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000871: Tuner
/// </summary>
public class _11000871 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003148$
    // - Huh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003150$
                // - $MyPCName$, would you like to know what's going on here? You look a little... bewildered.
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
