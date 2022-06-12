using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004121: Green Hood
/// </summary>
public class _11004121 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010485$
    // - I'll let you know if I detect any unusual movement inside the blast radius.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010486$
                // - See something, say something!
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
