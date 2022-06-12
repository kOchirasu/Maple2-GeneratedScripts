using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004053: Blackeye
/// </summary>
public class _11004053 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010079$
    // - We are ready to head out at a moment's notice.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010080$
                // - We are ready to head out at a moment's notice.
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
