using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000636: Prisoner 140919
/// </summary>
public class _11000636 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002589$
    // - I'm innocent!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002593$
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:0831180407002594$
                    // - How did you end up in here?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002595$
                // - Argh, don't get me started. Why can't I change my own profile image to something I like? So what if the picture is a little bit... lewd?
                return -1;
            case (50, 0):
                // $script:1210061907004895$
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:1210061907004896$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004897$
                // - ...You're one of <i>them</i>, aren't you?
                switch (selection) {
                    // $script:1210061907004898$
                    // - Uh... Sure I am. $npcName:11001231[gender:0]$ sent me.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1210061907004899$
                // - Quiet, or the warden will hear you! You came to see how things are coming along, is that it?
                switch (selection) {
                    // $script:1210061907004900$
                    // - That's right.
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:1210061907004901$
                // - Then talk to the supervisor. He's the one in charge here.
                switch (selection) {
                    // $script:1210061907004902$
                    // - Of course. And the supervisor is...?
                    case 0:
                        return 54;
                }
                return -1;
            case (54, 0):
                // $script:1210061907004903$
                // - $npcName:11000651[gender:0]$. You'll need the password, of course. We change it every three days to keep the guards off our trail.
                switch (selection) {
                    // $script:1210061907004904$
                    // - What's the latest password?
                    case 0:
                        return 55;
                }
                return -1;
            case (55, 0):
                // $script:1210061907004905$
                // - The latest password is... Shoot, what was it? Thick shadows... something. Ask one of the other guys.
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
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.SelectableDistractor,
            (54, 0) => NpcTalkButton.SelectableDistractor,
            (55, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
