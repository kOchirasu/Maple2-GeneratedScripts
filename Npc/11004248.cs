using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004248: Moonsweetie
/// </summary>
public class _11004248 : NpcScript {
    protected override int First() {
        return 90;
    }

    // Select 0:
    // $script:0905135907011041$
    // - I come from a long line of proud moon bunnies. I'm here to give you the blessings of the moon!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (90, 0):
                // $script:0823163507015094$
                // - Are you enjoying the anniversary party?
                switch (selection) {
                    // $script:0823163507015095$
                    // - I sure am!
                    case 0:
                        return 91;
                    // $script:0823163507015096$
                    // - No. It's terrible.
                    case 1:
                        return 93;
                }
                return -1;
            case (91, 0):
                // $script:0823163507015097$
                // - You know how to have fun! Did you find the special treasure chests at the top of $map:63000089$?
                switch (selection) {
                    // $script:0823163507015098$
                    // - How do I get to them?
                    case 0:
                        return 92;
                }
                return -1;
            case (92, 0):
                // $script:0823163507015099$
                // - Climb all the way up the cliff to the north of $map:63000089$ and you'll find a whole heap of golden treasure chests!
                return 92;
            case (92, 1):
                // $script:0823163507015100$
                // - It'll be a piece of cake for an adventurer like you. Anyway, good luck!
                return -1;
            case (93, 0):
                // $script:0823163507015101$
                // - R-really? Maybe... maybe you just need to find something fun to do? Like... did you know about the treasure chests at the highest point in $map:63000089$?
                switch (selection) {
                    // $script:0823163507015102$
                    // - I don't! How do you get to them?
                    case 0:
                        return 92;
                    // $script:0823163507015103$
                    // - I don't care!
                    case 1:
                        return 94;
                }
                return -1;
            case (94, 0):
                // $script:0823163507015104$
                // - Waaaaah... 
                return 94;
            case (94, 1):
                // $script:0823163507015105$
                // - Can't you... can't you just <i>pretend</i> to care? I worked sooo hard to put this party together... Waaah... 
                switch (selection) {
                    // $script:0823163507015106$
                    // - Oh, just tell me, already.
                    case 0:
                        return 92;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (91, 0) => NpcTalkButton.SelectableDistractor,
            (92, 0) => NpcTalkButton.Next,
            (92, 1) => NpcTalkButton.Close,
            (93, 0) => NpcTalkButton.SelectableDistractor,
            (94, 0) => NpcTalkButton.Next,
            (94, 1) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
