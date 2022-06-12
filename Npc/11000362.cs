using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000362: Stan
/// </summary>
public class _11000362 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001502$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001505$
                // - Not many people know this, but cooked $npcName:21000059$ can be incredible. I'm getting ready to sell $npcName:21000059$ dishes made from my own secret recipe.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
