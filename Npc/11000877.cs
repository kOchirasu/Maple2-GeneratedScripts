using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000877: 
/// </summary>
public class _11000877 : NpcScript {
    internal _11000877(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003187$ 
                // - Huh? 
                return true;
            case 10:
                // $script:0831180407003188$ 
                // - Hey, got some $itemPlural:30000193$? 
                switch (selection) {
                    // $script:0831180407003189$
                    // - No.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180407003190$ 
                // - Don't you? You're broke, aren't you? If you find $itemPlural:30000193$, don't waste them on useless things. Bring them to me. 
                switch (selection) {
                    // $script:0831180407003191$
                    // - What can you give me for $itemPlural:30000193$?
                    case 0:
                        Id = 12;
                        return false;
                    // $script:0831180407003192$
                    // - Why are you collecting $itemPlural:30000193$?
                    case 1:
                        Id = 13;
                        return false;
                }
                return true;
            case 12:
                // $script:0831180407003193$ 
                // - I can help you become stronger more quickly than any hunting you could do. I'm not just talking about equipment, either. With my help, you can become even mightier than before. 
                // $script:0831180407003194$ 
                // - That's got to be more appealing than just buying a new sword or whatever with your $itemPlural:30000193$, right? Think about what's going to help you the most. 
                // $script:0831180407003195$ 
                // - I'm not just talking about a couple of $itemPlural:30000193$, though. You're going to need a couple dozen or maybe a hundred if you want my help. Got it? 
                return true;
            case 13:
                // $script:0831180407003196$ 
                // - That's none of your business. Bring me at least 10 $itemPlural:30000193$, and we'll talk. 
                return true;
            case 20:
                // $script:0831180407003197$ 
                // - Did you bring me some $itemPlural:30000193$? 
                switch (selection) {
                    // $script:0831180407003198$
                    // - Yeah, here's 10 $itemPlural:30000193$.
                    case 0:
                        Id = 0; // TODO: 21 | 22
                        return false;
                    // $script:0831180407003199$
                    // - Yeah, here's 100 $itemPlural:30000193$.
                    case 1:
                        Id = 0; // TODO: 23 | 24
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407003200$ functionID=1 
                // - Nice, nice. I'll make sure these $itemPlural:30000193$ go to a good cause. See you around. 
                return true;
            case 22:
                // $script:0831180407003201$ 
                // - What? You punk, how dare you try to cheat me out of my $itemPlural:30000193$? Get out of my sight! 
                return true;
            case 23:
                // $script:0831180407003202$ functionID=2 
                // - Nice, nice. I'll make sure these $itemPlural:30000193$ go to a good cause. See you around. 
                return true;
            case 24:
                // $script:0831180407003203$ 
                // - What? You punk, how dare you try to cheat me out of my $itemPlural:30000193$? Get out of my sight! 
                return true;
            default:
                return true;
        }
    }
}
