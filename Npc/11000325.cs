using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000325: Gordon
/// </summary>
public class _11000325 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001312$
    // - Hello. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001315$
                // - Welcome to the Tuning Motors Showroom! Are you looking for something in particular?
                switch (selection) {
                    // $script:0909184507003771$
                    // - I want to know about mounts.
                    case 0:
                        return 38;
                    // $script:0909184507003772$
                    // - I came to see the cars.
                    case 1:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407001316$
                // - I'm here to help you find the perfect car for your style and needs. What kind of car do you like?
                switch (selection) {
                    // $script:0831180407001317$
                    // - Rugged 4-wheel-drives.
                    case 0:
                        // TODO: goto 33,37
                        // TODO: gotoFail 34
                        return 34;
                    // $script:0831180407001318$
                    // - Luxurious sports cars.
                    case 1:
                        return 35;
                    // $script:0831180407001319$
                    // - No cage for me! I want a bike.
                    case 2:
                        return 36;
                }
                return -1;
            case (33, 0):
                // functionID=1 
                // $script:0831180407001320$
                // - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on.
                return 33;
            case (33, 1):
                // openTalkReward=True 
                // $script:0831180407001321$
                // - Lucky for you, I've got one 4-wheel-drive model brochure left. Would you like to take a look?
                return -1;
            case (34, 0):
                // $script:0831180407001322$
                // - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on. Lucky for you, I've got one 4-wheel-drive model brochure left.
                return 34;
            case (34, 1):
                // $script:0831180407001323$
                // - Oh dear, you don't seem to have enough room in your bag for this brochure. It must be completely stuffed! Make some room if you'd like it, please.
                return -1;
            case (35, 0):
                // $script:0831180407001324$
                // - I knew it! You had that look that says "I've got a need... for speed".
                return 35;
            case (35, 1):
                // $script:0831180407001325$
                // - The Tuning Motors Enpilar series features a high-performance engine slotted into a low-riding, stable chassis to minimize air resistance and give more power to the speed-sensitive steering and brakes. $MyPCName$, it won't disappoint you!
                return -1;
            case (36, 0):
                // $script:0831180407001326$
                // - Ooh, we're kindred spirits! With a bike, you can fly through narrow alleyways and congested freeways at high speed. And don't forget the sense of freedom that you don't get in a car!  
                return 36;
            case (36, 1):
                // $script:0831180407001327$
                // - The Tuning Motors Chopper series is the king of Maple World touring bikes, and it's been the most popular bike on the market for years. It has a much larger displacement than street bikes, and its engine makes a throaty roar that you can't help but love!
                return -1;
            case (37, 0):
                // $script:0831180407001328$
                // - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on.
                return 37;
            case (37, 1):
                // $script:0831180407001329$
                // - Good, you already have our 4-wheel-drive model brochure. Read through it, and let me know if you have any questions. And it wouldn't hurt to have a look at our other models, too.
                return -1;
            case (38, 0):
                // $script:0909184507003773$
                // - Mounts? I'll tell you anything you want to know. What'll it be?
                switch (selection) {
                    // $script:0909184507003774$
                    // - What exactly are mounts?
                    case 0:
                        return 39;
                    // $script:0909184507003775$
                    // - Where can I get mounts?
                    case 1:
                        return 40;
                    // $script:0909184507003776$
                    // - How do I use my mounts?
                    case 2:
                        return 41;
                }
                return -1;
            case (39, 0):
                // $script:0909184507003777$
                // - Mounts are very convenient modes of transportation. Riding a mount is faster than running, and much more convenient too! Plus, there's a wide variety of mounts to choose from. So... which one looks good to you?
                switch (selection) {
                    // $script:0910171307003816$
                    // - I need to ask something else.
                    case 0:
                        return 42;
                }
                return -1;
            case (40, 0):
                // $script:0909184507003778$
                // - You can buy cute animal mounts from the Mount Merchant in town. I've heard some animal mounts can even swim. There's also some pretty awesome cars and bikes available for purchase on the Meret Market.
                return 40;
            case (40, 1):
                // $script:0909184507003779$
                // - You can buy mounts with all kinds of currencies, including mesos, treva, valor tokens, and merets. But to get an extremely fast rare mount, you'll need to earn certain Trophies.
                switch (selection) {
                    // $script:0910171307003817$
                    // - I need to ask something else.
                    case 0:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0909184507003780$
                // - You can use a mount by double-clicking it in your inventory, or by adding it to a quickslot. Mounts perform a special action when you press the Basic Attack key while riding them. You'll have a lot of fun just checking out all the different special actions.
                return 41;
            case (41, 1):
                // $script:0910171307003818$
                // - But there's a catch... the special actions activated by the Basic Attack key consume stamina every time they're used. But it won't be a problem as long as you use them in moderation.
                switch (selection) {
                    // $script:0910171307003819$
                    // - I need to ask something else.
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0910171307003820$
                // - Is there anything else you want to know about mounts?
                switch (selection) {
                    // $script:0910171307003821$
                    // - What exactly are mounts?
                    case 0:
                        return 39;
                    // $script:0910171307003822$
                    // - Where can I get mounts?
                    case 1:
                        return 40;
                    // $script:0910171307003823$
                    // - How do I use my mounts?
                    case 2:
                        return 41;
                    // $script:0910171307003824$
                    // - I need to be going.
                    case 3:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:0910171307003825$
                // - While you're here, why don't you peruse the vehicles on display?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.Next,
            (35, 1) => NpcTalkButton.Close,
            (36, 0) => NpcTalkButton.Next,
            (36, 1) => NpcTalkButton.Close,
            (37, 0) => NpcTalkButton.Next,
            (37, 1) => NpcTalkButton.Close,
            (38, 0) => NpcTalkButton.SelectableDistractor,
            (39, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
