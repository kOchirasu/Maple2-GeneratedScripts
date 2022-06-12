using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000181: Gilbert
/// </summary>
public class _11000181 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000750$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000754$
                // - I've been working at this junkyard for over a decade, and this must be the strangest thing that has ever happened.
                switch (selection) {
                    // $script:0831180407000755$
                    // - What is it?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407000756$
                // - A while back, a carriage full of junk came in with some Royal Guard weapons. I figured it must have been a mistake, so I checked with $npcName:11000171[gender:0]$. He said they were to be melted down, now that the court was canceled.
                return 41;
            case (41, 1):
                // $script:0831180407000757$
                // - If that were the case, the palace should've sent them to the forge instead of a junkyard. Right?
                switch (selection) {
                    // $script:0831180407000758$
                    // - Yeah.
                    case 0:
                        return 42;
                    // $script:0831180407000759$
                    // - Nah.
                    case 1:
                        return 43;
                }
                return -1;
            case (42, 0):
                // $script:0831180407000760$
                // - Right on. And I even saw $npcName:11000171[gender:0]$ sell the iron from the palace weapons to some dealer. How crazy do you have to be to steal from the palace? 
                return -1;
            case (43, 0):
                // $script:0831180407000761$
                // - Really? Huh. Maybe it's just me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
