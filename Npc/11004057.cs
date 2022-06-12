using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004057: Blackeye
/// </summary>
public class _11004057 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010087$
    // - We will aid you with your search.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010088$
                // - Talk to me whenever you need assistance.
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
