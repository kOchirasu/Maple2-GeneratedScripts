using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000515: Jayce
/// </summary>
public class _11000515 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;60
    }

    // Select 0:
    // $script:0831180407002209$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002210$
                // - If you're looking for the $map:2000216$, you came to the right place.
                switch (selection) {
                    // $script:0831180407002211$
                    // - What's the $map:02000216$?
                    case 0:
                        return 51;
                    // $script:0831180407002212$
                    // - I'm curious about Blackstar.
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0831180407002213$
                // - I'm not surprised you haven't heard of it. This is a place that services people with extraordinary taste.
                return 51;
            case (51, 1):
                // $script:0831180407002214$
                // - Looking for items to invest in? Have rare items to sell? This is the place to do it.
                return 51;
            case (51, 2):
                // $script:0831180407002215$
                // - Whatever your business, you'll find that the goods we broker here are a far cry from those you find in $map:2000100$.
                return 51;
            case (51, 3):
                // $script:0831180407002216$
                // - Talk to one of my brokers below to browse or sell items.
                return 51;
            case (51, 4):
                // $script:0831180407002217$
                // - Note that epic and above items can only be brokered through the $map:2000216$. We'll <i>know</i> if you try to move them without us, and trust me, we will not be pleased.
                return 51;
            case (51, 5):
                // $script:0831180407002218$
                // - Now, if you'll excuse me...
                return -1;
            case (52, 0):
                // $script:0831180407002219$
                // - Well, aren't you the joker. If you're smart, you won't repeat that question to anyone else.
                return 52;
            case (52, 1):
                // $script:0831180407002220$
                // - For the record, we aren't doing anything illegal here.
                return 52;
            case (52, 2):
                // $script:0831180407002221$
                // - The $map:2000216$ attracts adventurers and tourists from all over Maple World, and that's advantageous to $map:2000100$.
                return 52;
            case (52, 3):
                // $script:0831180407002222$
                // - In fact, the majority of $map:2000100$'s residents support us. The polls all say so.
                return -1;
            case (60, 0):
                // $script:0711184007006708$
                // - Ah, Gray Wolf. You have business with me? If you're looking for the $map:2000216$, you've come to the right place.
                switch (selection) {
                    // $script:0711184007006709$
                    // - What's the $map:02000216$?
                    case 0:
                        return 61;
                    // $script:0711184007006710$
                    // - I'm curious about Blackstar.
                    case 1:
                        return 62;
                }
                return -1;
            case (61, 0):
                // $script:0711184007006711$
                // - I'm not surprised you haven't heard of it. This is a place that services people with extraordinary taste. Our clientèle does not typically mix with rough-and-tumble fighter types.
                return 61;
            case (61, 1):
                // $script:0711184007006712$
                // - I'll have to check what items I have that are suitable for your skills. Are you looking for something in particular? Or do you have a rare item that you'd like to sell?
                return 61;
            case (61, 2):
                // $script:0711184007006713$
                // - I don't care either way. The products here are incomparable to those available in $map:2000100$. Heh.
                return 61;
            case (61, 3):
                // $script:0711184007006714$
                // - Simply talk to the traders here to browse their wares or sell your items on the $map:2000216$. They'll do their best to help you. Probably.
                return 61;
            case (61, 4):
                // $script:0711184007006715$
                // - Keep in mind that the only place to trade epic and better items is the $map:2000216$. And if you try to secretly trade such items without us, we'll know. You may be the famous Gray Wolf, but this is our field of expertise.
                return 61;
            case (61, 5):
                // $script:0711184007006716$
                // - Now, if you'll excuse me...
                return -1;
            case (62, 0):
                // $script:0711184007006717$
                // - I'm telling you this for your own good. A place like this draws a lot of attention. Even now, agents from many organizations are watching us.
                return 62;
            case (62, 1):
                // $script:0711184007006718$
                // - Not many people recognize you as a threat. But if you keep asking questions like that, they'll start to take notice. You don't want that. Understand?
                return 62;
            case (62, 2):
                // $script:0711184007006719$
                // - You may not be Blackstar's biggest fan, but not everything it does is bad. The $map:2000216$ has drawn adventurers and traders from all over Maple World. I'd say that it's single-handedly put $map:2000100$ and $map:2000135$ on the map.
                return 62;
            case (62, 3):
                // $script:0711184007006720$
                // - The people of $map:2000100$ are thankful for what we've done for the community. So I suggest you keep your opinions about Blackstar to yourself while you're here.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Next,
            (51, 2) => NpcTalkButton.Next,
            (51, 3) => NpcTalkButton.Next,
            (51, 4) => NpcTalkButton.Next,
            (51, 5) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Next,
            (52, 2) => NpcTalkButton.Next,
            (52, 3) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Next,
            (61, 1) => NpcTalkButton.Next,
            (61, 2) => NpcTalkButton.Next,
            (61, 3) => NpcTalkButton.Next,
            (61, 4) => NpcTalkButton.Next,
            (61, 5) => NpcTalkButton.Close,
            (62, 0) => NpcTalkButton.Next,
            (62, 1) => NpcTalkButton.Next,
            (62, 2) => NpcTalkButton.Next,
            (62, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
