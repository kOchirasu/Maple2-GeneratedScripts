using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004206: Dodo
/// </summary>
public class _11004206 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0803202415009085$
    // - Mushrooms make mistakes, too...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0803202415009086$
                // - I don't feel like chatting today...
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
