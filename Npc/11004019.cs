using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004019: Surnuny
/// </summary>
public class _11004019 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010025$
    // - Something's wrong... My fur's standing on end.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010026$
                // - Something's wrong... My fur's standing on end.
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
