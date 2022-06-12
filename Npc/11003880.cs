using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003880: Gardener
/// </summary>
public class _11003880 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0417135107009876$
    // - Doesn't this flower look like me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009877$
                // - Doesn't this flower look like me?
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
