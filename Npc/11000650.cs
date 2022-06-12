using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000650: Prisoner 170122
/// </summary>
public class _11000650 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002663$
    // - When can I get out of here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002667$
                // - Huh? You don't look like an inmate.
                switch (selection) {
                    // $script:0831180407002668$
                    // - What are you doing?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002669$
                // - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Ugh, I'll grow old before I can pull that many weeds.
                return -1;
            case (50, 0):
                // $script:1210061907004920$
                // - Huh? You don't look like an inmate.
                switch (selection) {
                    // $script:1210061907004921$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1214232707004979$
                // - How do you know <i>that man</i>?
                switch (selection) {
                    // $script:1214232707004980$
                    // - I'm working with him.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1214232707004981$
                // - Hm... Yes, there is something special about you. What brings you here, then?
                switch (selection) {
                    // $script:1214232707004982$
                    // - I'm here on $npcName:11001231[gender:0]$'s behalf.
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:1214232707004983$
                // - He's just as impatient as the supervisor, eh? Well, if you're here on business, you better talk to him.
                switch (selection) {
                    // $script:1214232707004984$
                    // - Who is this supervisor?
                    case 0:
                        return 54;
                }
                return -1;
            case (54, 0):
                // $script:1214232707004985$
                // - $npcName:11000651[gender:0]$. But he doesn't talk to nobody without the password. That's the rule. And, to keep things nice and secure, we change it every three days.
                switch (selection) {
                    // $script:1214232707004986$
                    // - What's the password?
                    case 0:
                        return 55;
                }
                return -1;
            case (55, 0):
                // $script:1214232707004987$
                // - I wrote it down somewhere. Ahem. "In the middle of the shadows..." Drat! The rest got erased.
                return 55;
            case (55, 1):
                // $script:1214232707004988$
                // - Sorry, that's all I know. You'll have to ask someone else for the rest of the password.
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
            (55, 0) => NpcTalkButton.Next,
            (55, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
