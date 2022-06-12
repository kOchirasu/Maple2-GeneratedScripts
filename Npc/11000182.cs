using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000182: Junkyard Worker
/// </summary>
public class _11000182 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407000762$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000767$
                // - Scram, I got work to do.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
