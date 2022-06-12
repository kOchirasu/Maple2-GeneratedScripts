using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000116: Anthony
/// </summary>
public class _11000116 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000490$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000493$
                // - $MyPCName$, do you think this is just a simple earthquake?
                switch (selection) {
                    // $script:0831180407000494$
                    // - Yep!
                    case 0:
                        return 31;
                    // $script:0831180407000495$
                    // - Seems unlikely.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0831180407000496$
                // - ...
                return 31;
            case (31, 1):
                // $script:0831180407000497$
                // - All right. Fine. Just keep thinking that way.
                return -1;
            case (32, 0):
                // $script:0831180407000498$
                // - I don't have proof yet, but I'm certain this wasn't a simple earthquake. I suspect a massive shadow gate has opened somewhere, causing this upheaval.
                switch (selection) {
                    // $script:0831180407000499$
                    // - What is a shadow gate?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0831180407000500$
                // - You've never seen a shadow gate? Lucky you. They're doorways to the Land of Darkness. The empress herself has forbidden anyone from using such gates.
                return 33;
            case (33, 1):
                // $script:0831180407000501$
                // - Our forces have the Shadow Gate blockaded and guarded to ensure nothing escapes. There are rumored to be unguarded passages hidden around Maple World, and some shady types use those to pass through to the Land of Darkness.
                return 33;
            case (33, 2):
                // $script:0831180407000502$
                // - I was told that those who dare enter the Land of Darkness would have both their bodies and souls devoured by demons. However, that sounds like something made up to keep people from exploring. My plan is to find a shadow gate and travel to the Land of Darkness myself, so don't tell anyone.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.Next,
            (33, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
