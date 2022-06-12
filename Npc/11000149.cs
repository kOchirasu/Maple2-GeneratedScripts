using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000149: Collin
/// </summary>
public class _11000149 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000635$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000637$
                // - Have you seen a puppy around here?
                switch (selection) {
                    // $script:0831180407000638$
                    // - Nope.
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000639$
                // - Ahhh... Whitey, where are you? I should never have taken him outside. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
