using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000515: Jayce
/// </summary>
public class _11000515 : NpcScript {
    internal _11000515(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002209$ 
                // - Can I help you? 
                return true;
            case 50:
                // $script:0831180407002210$ 
                // - If you're looking for the $map:2000216$, you came to the right place. 
                switch (selection) {
                    // $script:0831180407002211$
                    // - What's the $map:02000216$?
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407002212$
                    // - I'm curious about Blackstar.
                    case 1:
                        Id = 52;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407002213$ 
                // - I'm not surprised you haven't heard of it. This is a place that services people with extraordinary taste. 
                // $script:0831180407002214$ 
                // - Looking for items to invest in? Have rare items to sell? This is the place to do it. 
                // $script:0831180407002215$ 
                // - Whatever your business, you'll find that the goods we broker here are a far cry from those you find in $map:2000100$. 
                // $script:0831180407002216$ 
                // - Talk to one of my brokers below to browse or sell items. 
                // $script:0831180407002217$ 
                // - Note that epic and above items can only be brokered through the $map:2000216$. We'll <i>know</i> if you try to move them without us, and trust me, we will not be pleased. 
                // $script:0831180407002218$ 
                // - Now, if you'll excuse me... 
                return true;
            case 52:
                // $script:0831180407002219$ 
                // - Well, aren't you the joker. If you're smart, you won't repeat that question to anyone else. 
                // $script:0831180407002220$ 
                // - For the record, we aren't doing anything illegal here. 
                // $script:0831180407002221$ 
                // - The $map:2000216$ attracts adventurers and tourists from all over Maple World, and that's advantageous to $map:2000100$. 
                // $script:0831180407002222$ 
                // - In fact, the majority of $map:2000100$'s residents support us. The polls all say so. 
                return true;
            case 60:
                // $script:0711184007006708$ 
                // - Ah, Gray Wolf. You have business with me? If you're looking for the $map:2000216$, you've come to the right place. 
                switch (selection) {
                    // $script:0711184007006709$
                    // - What's the $map:02000216$?
                    case 0:
                        Id = 61;
                        return false;
                    // $script:0711184007006710$
                    // - I'm curious about Blackstar.
                    case 1:
                        Id = 62;
                        return false;
                }
                return true;
            case 61:
                // $script:0711184007006711$ 
                // - I'm not surprised you haven't heard of it. This is a place that services people with extraordinary taste. Our clientèle does not typically mix with rough-and-tumble fighter types. 
                // $script:0711184007006712$ 
                // - I'll have to check what items I have that are suitable for your skills. Are you looking for something in particular? Or do you have a rare item that you'd like to sell? 
                // $script:0711184007006713$ 
                // - I don't care either way. The products here are incomparable to those available in $map:2000100$. Heh. 
                // $script:0711184007006714$ 
                // - Simply talk to the traders here to browse their wares or sell your items on the $map:2000216$. They'll do their best to help you. Probably. 
                // $script:0711184007006715$ 
                // - Keep in mind that the only place to trade epic and better items is the $map:2000216$. And if you try to secretly trade such items without us, we'll know. You may be the famous Gray Wolf, but this is our field of expertise. 
                // $script:0711184007006716$ 
                // - Now, if you'll excuse me... 
                return true;
            case 62:
                // $script:0711184007006717$ 
                // - I'm telling you this for your own good. A place like this draws a lot of attention. Even now, agents from many organizations are watching us. 
                // $script:0711184007006718$ 
                // - Not many people recognize you as a threat. But if you keep asking questions like that, they'll start to take notice. You don't want that. Understand? 
                // $script:0711184007006719$ 
                // - You may not be Blackstar's biggest fan, but not everything it does is bad. The $map:2000216$ has drawn adventurers and traders from all over Maple World. I'd say that it's single-handedly put $map:2000100$ and $map:2000135$ on the map. 
                // $script:0711184007006720$ 
                // - The people of $map:2000100$ are thankful for what we've done for the community. So I suggest you keep your opinions about Blackstar to yourself while you're here. 
                return true;
            default:
                return true;
        }
    }
}
