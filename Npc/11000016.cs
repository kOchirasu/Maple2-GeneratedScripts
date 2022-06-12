using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000016: Tru
/// </summary>
public class _11000016 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180610000001$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1101173110001798$
                // - You want to go to $map:02000001$? Why are you asking me? You should go to the Chief.
                switch (selection) {
                    // $script:1101173110001799$
                    // - I thought sea dogs were adventurous, and yet you won't even let a friendly stranger onto your boat?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1101173110001800$
                // - You sail to $map:02000001$ by first going to $map:02000062$, and right now the water's too choppy for this boat. Besides, when conditions are like that, only the Chief can authorize the departure of a large ship.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
