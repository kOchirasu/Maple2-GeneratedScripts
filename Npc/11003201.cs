using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003201: Katvan
/// </summary>
public class _11003201 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008228$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008229$
                // - What brings you here?
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
