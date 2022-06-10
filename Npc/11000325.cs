using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000325: Gordon
/// </summary>
public class _11000325 : NpcScript {
    internal _11000325(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001312$ 
                // - Hello.  
                return true;
            case 30:
                // $script:0831180407001315$ 
                // - Welcome to the Tuning Motors Showroom! Are you looking for something in particular? 
                switch (selection) {
                    // $script:0909184507003771$
                    // - I want to know about mounts.
                    case 0:
                        Id = 38;
                        return false;
                    // $script:0909184507003772$
                    // - I came to see the cars.
                    case 1:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407001316$ 
                // - I'm here to help you find the perfect car for your style and needs. What kind of car do you like? 
                switch (selection) {
                    // $script:0831180407001317$
                    // - Rugged 4-wheel-drives.
                    case 0:
                        Id = 0; // TODO: 33,37 | 34
                        return false;
                    // $script:0831180407001318$
                    // - Luxurious sports cars.
                    case 1:
                        Id = 35;
                        return false;
                    // $script:0831180407001319$
                    // - No cage for me! I want a bike.
                    case 2:
                        Id = 36;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407001320$ functionID=1 
                // - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on. 
                // $script:0831180407001321$ 
                // - Lucky for you, I've got one 4-wheel-drive model brochure left. Would you like to take a look? 
                return true;
            case 34:
                // $script:0831180407001322$ 
                // - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on. Lucky for you, I've got one 4-wheel-drive model brochure left. 
                // $script:0831180407001323$ 
                // - Oh dear, you don't seem to have enough room in your bag for this brochure. It must be completely stuffed! Make some room if you'd like it, please. 
                return true;
            case 35:
                // $script:0831180407001324$ 
                // - I knew it! You had that look that says "I've got a need... for speed". 
                // $script:0831180407001325$ 
                // - The Tuning Motors Enpilar series features a high-performance engine slotted into a low-riding, stable chassis to minimize air resistance and give more power to the speed-sensitive steering and brakes. $MyPCName$, it won't disappoint you! 
                return true;
            case 36:
                // $script:0831180407001326$ 
                // - Ooh, we're kindred spirits! With a bike, you can fly through narrow alleyways and congested freeways at high speed. And don't forget the sense of freedom that you don't get in a car!   
                // $script:0831180407001327$ 
                // - The Tuning Motors Chopper series is the king of Maple World touring bikes, and it's been the most popular bike on the market for years. It has a much larger displacement than street bikes, and its engine makes a throaty roar that you can't help but love! 
                return true;
            case 37:
                // $script:0831180407001328$ 
                // - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on. 
                // $script:0831180407001329$ 
                // - Good, you already have our 4-wheel-drive model brochure. Read through it, and let me know if you have any questions. And it wouldn't hurt to have a look at our other models, too. 
                return true;
            case 38:
                // $script:0909184507003773$ 
                // - Mounts? I'll tell you anything you want to know. What'll it be? 
                switch (selection) {
                    // $script:0909184507003774$
                    // - What exactly are mounts?
                    case 0:
                        Id = 39;
                        return false;
                    // $script:0909184507003775$
                    // - Where can I get mounts?
                    case 1:
                        Id = 40;
                        return false;
                    // $script:0909184507003776$
                    // - How do I use my mounts?
                    case 2:
                        Id = 41;
                        return false;
                }
                return true;
            case 39:
                // $script:0909184507003777$ 
                // - Mounts are very convenient modes of transportation. Riding a mount is faster than running, and much more convenient too! Plus, there's a wide variety of mounts to choose from. So... which one looks good to you? 
                switch (selection) {
                    // $script:0910171307003816$
                    // - I need to ask something else.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 40:
                // $script:0909184507003778$ 
                // - You can buy cute animal mounts from the Mount Merchant in town. I've heard some animal mounts can even swim. There's also some pretty awesome cars and bikes available for purchase on the Meret Market. 
                // $script:0909184507003779$ 
                // - You can buy mounts with all kinds of currencies, including mesos, treva, valor tokens, and merets. But to get an extremely fast rare mount, you'll need to earn certain Trophies. 
                switch (selection) {
                    // $script:0910171307003817$
                    // - I need to ask something else.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0909184507003780$ 
                // - You can use a mount by double-clicking it in your inventory, or by adding it to a quickslot. Mounts perform a special action when you press the Basic Attack key while riding them. You'll have a lot of fun just checking out all the different special actions. 
                // $script:0910171307003818$ 
                // - But there's a catch... the special actions activated by the Basic Attack key consume stamina every time they're used. But it won't be a problem as long as you use them in moderation. 
                switch (selection) {
                    // $script:0910171307003819$
                    // - I need to ask something else.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0910171307003820$ 
                // - Is there anything else you want to know about mounts? 
                switch (selection) {
                    // $script:0910171307003821$
                    // - What exactly are mounts?
                    case 0:
                        Id = 39;
                        return false;
                    // $script:0910171307003822$
                    // - Where can I get mounts?
                    case 1:
                        Id = 40;
                        return false;
                    // $script:0910171307003823$
                    // - How do I use my mounts?
                    case 2:
                        Id = 41;
                        return false;
                    // $script:0910171307003824$
                    // - I need to be going.
                    case 3:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:0910171307003825$ 
                // - While you're here, why don't you peruse the vehicles on display? 
                return true;
            default:
                return true;
        }
    }
}
