using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004047: Surmany
/// </summary>
public class _11004047 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010067$
    // - I'll do my best to help the queen.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010068$
                // - I'll do my best to help the queen.
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
