using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004135: Landevian
/// </summary>
public class _11004135 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010535$
    // - So much power...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010536$
                // - All this power... I want to test it on something...
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
