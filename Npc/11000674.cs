using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000674: Altar of Rage
/// </summary>
public class _11000674 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180610000464$
    // - <font color="#909090">(The altar has faded letters written on it.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180610000465$
                // - <font color="#909090">(Read the message.)</font>
                return 10;
            case (10, 1):
                // $script:0831180610000466$
                // - <i>Shadow World is an angry land...
                //   Where no blessing upon anyone can make any difference.</i>
                return 10;
            case (10, 2):
                // $script:0831180610000467$
                // - <i>Lo, if you are one who thirsts for blood, will you absorb the wrathful energy and rid yourself of $skill:70000029$?</i>
                switch (selection) {
                    // $script:0831180610000468$
                    // - Lose $skill:70000029$.
                    case 0:
                        return 11;
                    // $script:0831180610000469$
                    // - Retain $skill:70000029$.
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180610000470$
                // - <i>The wrathful shadows have devoured every one of your blessings and taken over your mind.
                //   Now, you see that friendship is a myth, and everyone is your enemy!</i>
                return -1;
            case (12, 0):
                // $script:0831180610000471$
                // - <i>In the end, nothing can truly shield you from reality.</i>
                return -1;
            case (20, 0):
                // $script:0831180610000472$
                // - <font color="#909090">(Reading the words on the altar, Turka's anger is almost palpable.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
