using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000878: 
/// </summary>
public class _11000878 : NpcScript {
    protected override void FirstScript() {
        // TODO: RandomPick 10;20
        // (Id, Button) = (10, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (20, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0831180407003204$ 
                // - Huh?
                return default;
            case 10:
                // $script:0831180407003205$ 
                // - Hey, got some $itemPlural:30000193$?
                switch (selection) {
                    // $script:0831180407003206$
                    // - No.
                    case 0:
                        return (11, NpcTalkButton.SelectableDistractor);
                }
                return default;
            case 11:
                // $script:0831180407003207$ 
                // - Don't you? You're broke, aren't you? If you find $itemPlural:30000193$, don't waste them on useless things. Bring them to me.
                switch (selection) {
                    // $script:0831180407003208$
                    // - What can you give me for $itemPlural:30000193$?
                    case 0:
                        return (12, NpcTalkButton.Next);
                    // $script:0831180407003209$
                    // - Why are you collecting $itemPlural:30000193$?
                    case 1:
                        return (13, NpcTalkButton.Close);
                }
                return default;
            case 12:
                switch (Index++) {
                    case 0:
                        // $script:0831180407003210$ 
                        // - I can help you become stronger more quickly than any hunting you could do. I'm not just talking about equipment, either. With my help, you can become even mightier than before.
                        return (12, NpcTalkButton.Next);
                    case 1:
                        // $script:0831180407003211$ 
                        // - That's got to be more appealing than just buying a new sword or whatever with your $itemPlural:30000193$, right? Think about what's going to help you the most.
                        return (12, NpcTalkButton.Close);
                    case 2:
                        // $script:0831180407003212$ 
                        // - I'm not just talking about a couple of $itemPlural:30000193$, though. You're going to need a couple dozen or maybe a hundred if you want my help. Got it?
                        return default;
                }
                break;
            case 13:
                // $script:0831180407003213$ 
                // - That's none of your business. Bring me at least 10 $itemPlural:30000193$, and we'll talk.
                return default;
            case 20:
                // $script:0831180407003214$ 
                // - Did you bring me some $itemPlural:30000193$?
                switch (selection) {
                    // $script:0831180407003215$
                    // - Yeah, here's 10 $itemPlural:30000193$.
                    case 0:
                        // TODO: goto 21
                        // (Id, Button) = (21, NpcTalkButton.Close);
                        // TODO: gotoFail 22
                        // (Id, Button) = (22, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0831180407003216$
                    // - Yeah, here's 100 $itemPlural:30000193$.
                    case 1:
                        // TODO: goto 23
                        // (Id, Button) = (23, NpcTalkButton.Close);
                        // TODO: gotoFail 24
                        // (Id, Button) = (24, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 21:
                // $script:0831180407003217$ functionID=1 
                // - Nice, nice. I'll make sure these $itemPlural:30000193$ go to a good cause. See you around.
                return default;
            case 22:
                // $script:0831180407003218$ 
                // - What? You punk, how dare you try to cheat me out of my $itemPlural:30000193$? Get out of my sight!
                return default;
            case 23:
                // $script:0831180407003219$ functionID=2 
                // - Nice, nice. I'll make sure these $itemPlural:30000193$ go to a good cause. See you around.
                return default;
            case 24:
                // $script:0831180407003220$ 
                // - What? You punk, how dare you try to cheat me out of my $itemPlural:30000193$? Get out of my sight!
                return default;
        }
        
        return default;
    }
}
