using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001181: Godar
/// </summary>
public class _11001181 : NpcScript {
    internal _11001181(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1014150507004129$ 
                // - Ah, I should update my travel journal!
                return true;
            case 30:
                // $script:1014150507004132$ 
                // - Ah, a local! <font color="#ffd200">Yalario!</font> It always been my dream to explore strange new worlds, and seek out new life and new civilizations! Traveling this land has been an awesome experience.
                // $script:1014150507004133$ 
                // - ...Ah, but I'm sure these sights seem so plain to you. Well, I hope I'll get to keep visiting new places and writing about them in my travel journal.
                switch (selection) {
                    // $script:1014150507004134$
                    // - Yala-what-io?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1014150507004135$
                    // - I take it you like to travel?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1014150507004136$
                    // - Where exactly are you from?
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:1014150507004137$ 
                // - New friend! This is how we greet strangers who we want to be our friends. $npcName:11001179[gender:0]$ shouted it out when we first arrived in $map:02000064$, so I guess it can also be used for villages. Well, at least it can be by our captain.
                return true;
            case 32:
                // $script:1014150507004138$ 
                // - Of course! Setting foot in a new land, leaving proof of your journey... There's nothing more exciting! I bet everyone in the <b>Allicari Merchant Society</b> would agree.
                return true;
            case 33:
                // $script:1014150507004139$ 
                // - I'm from a place far, far away! On the other side of the sea. To get there from here you have to go north... no wait, south... Err, east? We sort of stumbled upon this land by accident. My homeland is beautiful, although it's much different than here.
                return true;
            case 40:
                // $script:1026143107004294$ 
                // - Ah, yalario! What can I do for you?
                switch (selection) {
                    // $script:1026143107004295$
                    // - I'm looking for some $item:30000421$.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1026143107004296$ 
                // - Ah, those. The smuggler called $npcName:11001212[gender:0]$ sells them, but I wouldn't do business with him if I were you.
                switch (selection) {
                    // $script:1026143107004297$
                    // - Why do you say that?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1026143107004298$ 
                // - He snuck onto our vessel because he did not want to pay a simple fare. No one who does such a thing could be considered trustworthy.
                switch (selection) {
                    // $script:1026143107004299$
                    // - Where can I find $npcName:11001212[gender:0]$ now?
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:1026143107004300$ 
                // - Captain $npcName:11001179[gender:0]$ kicked him off the ship. Last I saw, he was running off toward $map:03000014$.
                return true;
            default:
                return true;
        }
    }
}
