using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000096: Deke
/// </summary>
public class _11000096 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407000375$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000378$
                // - I sailed here with my girlfriend, $npc:11000151[gender:1]$. We're going to check out the Empress's court.
                switch (selection) {
                    // $script:0831180407000379$
                    // - So where is she?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000380$
                // - I'm sure she's around here somewhere. She got off before I did. Man, she was so excited, she pushed through the crowd and ran ashore. Guess she didn't notice she left me behind! Ha, ha...
                return -1;
            case (40, 0):
                // $script:1219181807005430$
                // - We finally made it to $map:02000062$! My lady and I are gonna have so much fun!
                return -1;
            case (50, 0):
                // $script:0809153207007162$
                // - We finally made it to $map:02000062$! My lady and I are gonna have so much fun!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
