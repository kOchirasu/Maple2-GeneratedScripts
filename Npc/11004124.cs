using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004124: Dark Wind Agent
/// </summary>
public class _11004124 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010491$
    // - The road to victory is paved with good intel.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010492$
                // - I've never seen anything so spooky.
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
