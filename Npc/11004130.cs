using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004130: Eupheria
/// </summary>
public class _11004130 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720143007010503$
    // - My head hurts...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720143007010504$
                // - Just what did we see in the darkness...?
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
