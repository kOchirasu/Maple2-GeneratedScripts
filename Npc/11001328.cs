using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001328: Lakachi
/// </summary>
public class _11001328 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005231$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005234$
                // - Just keep walking. I don't have time for wimps like you!
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
