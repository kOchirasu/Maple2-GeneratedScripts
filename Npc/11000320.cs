using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000320: Lyn
/// </summary>
public class _11000320 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001250$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001254$
                // - Everyone thinks they're special, but the world keeps turning without them.
                switch (selection) {
                    // $script:0831180407001255$
                    // - What's wrong?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001256$
                // - Nothing. I just understand the way of the world.
                return 41;
            case (41, 1):
                // $script:0831180407001257$
                // - Dust thou art, and to dust shalt thou return. Come empty, return empty. In the end, there's nothing in this world that is truly yours.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
