using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004046: Surnuny
/// </summary>
public class _11004046 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010065$
    // - The king will come back... He just has to!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010066$
                // - The king will come back... He just has to!
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
