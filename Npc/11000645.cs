using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000645: Prisoner 160918
/// </summary>
public class _11000645 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002633$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002637$
                // - I know all the guards, and you ain't one of them.
                switch (selection) {
                    // $script:0831180407002638$
                    // - How did you end up in here?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002639$
                // - I used some swear words for my character's name. That's how I want to express myself! Why should I care about other people's feelings?
                switch (selection) {
                    // $script:0831180407002640$
                    // - You've got a problem in how you think.
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0831180407002641$
                // - Shut up!  I don't need your lecturing! Go away!
                return -1;
            case (50, 0):
                // $script:1210061907004917$
                // - I know all the guards, and you ain't one of them.
                switch (selection) {
                    // $script:1210061907004918$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004919$
                // - No, I don't. And I don't wanna.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
