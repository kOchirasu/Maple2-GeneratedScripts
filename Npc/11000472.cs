using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000472: Tonk
/// </summary>
public class _11000472 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407002065$
    // - Hmph. WHAT?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002067$
                // - Real men aren't scared of spiders! They squash them flat as soon as they see them!
                return -1;
            case (30, 0):
                // $script:0831180407002068$
                // - This place behind me is loaded with spiders. If you're in a hurry, you can squash them yourself.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
