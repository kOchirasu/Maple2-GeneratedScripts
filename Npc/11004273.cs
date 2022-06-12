using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004273: Meeke
/// </summary>
public class _11004273 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011253$
    // - The moonlight is nice tonight. Very beautiful, very beautiful!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011254$
                // - The moonlight is nice tonight. Very beautiful, very beautiful!
                return 10;
            case (10, 1):
                // $script:0911203207011255$
                // - And what brings you here tonight, human?
                switch (selection) {
                    // $script:0911203207011256$
                    // - I'm just passing through.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011257$
                // - Then you must visit our camp in the $map:02010033$! I'm sure they won't mind you dropping by. Probably.
                return 11;
            case (11, 1):
                // $script:0911203207011258$
                // - The moonlight in our city is different from the moonlight out here, but no matter what, the moonlight is always beautiful!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
