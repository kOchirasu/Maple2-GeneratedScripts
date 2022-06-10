using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001985: Cathy Catalina
/// </summary>
public class _11001985 : NpcScript {
    internal _11001985(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0109143707007702$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0109143707007705$ 
                // - You're here for work? Great! Let's get started.
                switch (selection) {
                    // $script:0109143707007706$
                    // - What's this new business of yours?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0109143707007707$
                    // - What should I be doing?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:0109143707007708$
                    // - What are the job requirements?
                    case 2:
                        Id = 60;
                        return false;
                }
                return true;
            case 40:
                // $script:0109143707007709$ 
                // - Hehe. It really is a novel business model, isn't it? I guess I can tell you, if you're going to be working here.
                // $script:0109143707007710$ 
                // - Maple World's a pretty big place, but as we've developed newer, faster ways to travel, our systems of trade haven't really kept up.
                // $script:0109143707007711$ 
                // - People want things they can't get locally. Some people in $map:02000023$ might be starved for electronics from $map:02000100$, or others in $map:02010002$  might want handicrafts from Nerman artists.
                // $script:0109143707007712$ 
                // - The thing is, not everybody can afford to trot around the globe shopping for things they want. That's where my shop comes in.
                // $script:0109143707007713$ 
                // - Customers place their orders online for an item, and I acquire it for them. Then all they have to do is come in and pick up their merchandise. No muss, no fuss!
                // $script:0109143707007714$ 
                // - I've spent a long time building this business, and I've pretty much cornered the market. To do what I do, you need all kinds of connections and a shrewd business acumen. Luckily, I've got that in spades!
                return true;
            case 50:
                // $script:0109143707007715$ 
                // - You will be working as a team with your three friends. One of you will work the cash register, the rest of you will work in the warehouse.
                // $script:0109143707007716$ 
                // - Customers come to the store to pick up their orders. All you have to do is find their items in the warehouse and ring them up at the counter. Easy, right?
                // $script:0109143707007717$ 
                // - When a customer comes to the counter, the cashier must greet them. The customer will tell you which item they've come to pick up, and the cashier relays that information to the warehouse workers.
                // $script:0109143707007718$ 
                // - The warehouse workers will need to find and bring the item to the cashier. Cathy Mart prides itself in its service, so the faster the better.
                // $script:0109143707007719$ 
                // - Also, keep in mind that the store has an automatic cleaning system to keep the place nice and tidy.
                // $script:0109143707007720$ 
                // - That means that any item from the warehouse you leave lying around will be removed very soon after. That's why it's crucial you give the item to the customer directly.
                return true;
            case 60:
                // $script:0109143707007721$ 
                // - Do you have two or more grasping appendages? Can you lift things? You're hired! I don't care about your age, job, level, or any of that nonsense. All I need you to do is work together to fulfill customers' orders with blinding speed.
                // $script:0109143707007722$ 
                // - The four of you must work together from the moment the store opens until it closes. No quitting, and no breaks!
                switch (selection) {
                    // $script:0109143707007723$
                    // - Wait, what happens if someone quits?
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0109143707007724$ 
                // - For your own sake, let's hope that doesn't happen.
                return true;
            default:
                return true;
        }
    }
}
