using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004238: Junta
/// </summary>
public class _11004238 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010932$
    // - Hmph.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010933$
                // - Hmph.
                return 10;
            case (10, 1):
                // $script:0809223207010934$
                // - I'm sorry I wasn't of more help...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
