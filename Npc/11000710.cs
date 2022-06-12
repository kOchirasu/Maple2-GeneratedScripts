using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000710: Hudru
/// </summary>
public class _11000710 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002843$
    // - Did you call me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002846$
                // - I think I can cross this bridge if I don't look down. But... what if I lose my footing because I can't see where I'm going?
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
