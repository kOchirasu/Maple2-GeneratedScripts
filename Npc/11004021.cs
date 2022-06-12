using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004021: Tinchai
/// </summary>
public class _11004021 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010029$
    // - I really hope Brother Junta and the expedition members get better soon.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010030$
                // - I really hope Brother Junta and the expedition members get better soon.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
