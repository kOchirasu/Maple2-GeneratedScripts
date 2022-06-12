using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004018: Surnuny
/// </summary>
public class _11004018 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010023$
    // - Hey! I've seen you around Tria!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010024$
                // - I'm Surnuny, Tria's best weapons merchant. I came here to trade.
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
