using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000651: Prisoner 170123
/// </summary>
public class _11000651 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002670$
    // - When can I get out of here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002674$
                // - I'm busy. Scram!
                switch (selection) {
                    // $script:0831180407002675$
                    // - What are you doing?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002676$
                // - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Ugh, I'll grow old before I can pull that many weeds.
                return -1;
            case (50, 0):
                // $script:1210061907004923$
                // - I'm busy. Scram!
                switch (selection) {
                    // $script:1210061907004924$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004925$
                // - You want to talk? Fine. But first, what's the password?
                switch (selection) {
                    // $script:1214233907004997$
                    // - What's the password?
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1214233907004998$
                // - Haw! You don't know the password? Then we got nothing to talk about.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
