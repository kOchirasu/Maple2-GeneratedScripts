using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001279: Ishura
/// </summary>
public class _11001279 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1208175407004839$
    // - $npcName:11001231[gender:0]$ has struck again...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1208175407004842$
                // - We can discuss it later.
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
