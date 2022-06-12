using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000420: Moma
/// </summary>
public class _11000420 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 90;100
    }

    // Select 0:
    // $script:0831180407001748$
    // - You got something to say? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (90, 0):
                // $script:0831180407001754$
                // - Are you sightseeing? Head north to the condominium complex. The staff is nice, and it's really pretty around there. Just sayin'.
                return -1;
            case (100, 0):
                // $script:0831180407001755$
                // - $MyPCName$, do you like fish?
                switch (selection) {
                    // $script:0831180407001756$
                    // - Yep.
                    case 0:
                        return 101;
                    // $script:0831180407001757$
                    // - Nope.
                    case 1:
                        return 102;
                }
                return -1;
            case (101, 0):
                // $script:0831180407001758$
                // - Well $MyPCName$, you're more health-conscious than I thought. Fish is an excellent source of protein and other essential nutrients.
                return -1;
            case (102, 0):
                // $script:0831180407001759$
                // - Oh, you should eat fish regularly. I thought you knew that, $MyPCName$. Do you only eat red meat? It's too fatty. Eating fish helps you lose weight.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (90, 0) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (101, 0) => NpcTalkButton.Close,
            (102, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
