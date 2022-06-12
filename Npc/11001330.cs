using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001330: Mr. Arthur
/// </summary>
public class _11001330 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217012607005239$
    // - It's getting late already.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1217012607005243$
                // - She's been shopping all day. You'd think all that running around would be decent exercise...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
