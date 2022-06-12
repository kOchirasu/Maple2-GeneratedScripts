using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004562: Rolling Thunder
/// </summary>
public class _11004562 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014515$
    // - Hey!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014516$
                // - Ha! I should've known you'd be here. Someone like you can't resist a good rumble.
                switch (selection) {
                    // $script:0220211107014517$
                    // - You've got me there.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014518$
                // - That's the $MyPCName$ I remember! Hold on... This means we might have to fight each other.
                return 20;
            case (20, 1):
                // $script:0220211107014519$
                // - Well, well. Now I've got some real competition! Let's do our best, okay?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
