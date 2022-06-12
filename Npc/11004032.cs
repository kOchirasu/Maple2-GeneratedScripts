using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004032: Lanemone
/// </summary>
public class _11004032 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010049$
    // - What is it, kid? You want to know about lapenshards?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010050$
                // - What is it, kid? You want to know about lapenshards?
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
