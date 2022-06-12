using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004056: Allon
/// </summary>
public class _11004056 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010085$
    // - Losing the leadership of Terrun Calibre was too great a loss.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010086$
                // - Losing the leadership of Terrun Calibre was too great a loss.
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
