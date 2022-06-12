using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000610: Kama
/// </summary>
public class _11000610 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002506$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002507$
                // - Stop bothering me and scram.
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
