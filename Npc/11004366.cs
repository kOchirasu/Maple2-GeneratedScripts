using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004366: Mia
/// </summary>
public class _11004366 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011777$
    // - I doubt you understand the joys of a freshly-baked cake. And the holidays are the perfect time for perfect cakes!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011778$
                // - I do love baking, you know. It's one of my little personal joys. And there's nothing like baking for your family over the holidays.
                switch (selection) {
                    // $script:1120173007011852$
                    // - Do you like cake?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1120173007011853$
                // - What a ridiculous question. I <i>love</i> cake. And I love it so much that I cannot tolerate cakes that disappoint me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
