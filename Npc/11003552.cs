using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003552: Yoharang
/// </summary>
public class _11003552 : NpcScript {
    internal _11003552(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0905163707008895$ 
                // - I miss $map:63000044$...  
                return true;
            case 30:
                // $script:0905163707008898$ 
                // - I wonder how the weather on $map:63000044$ is today... 
                switch (selection) {
                    // $script:0905163707008899$
                    // - Tell me about $map:63000044$.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0905163707008900$
                    // - I want to see $map:63000044$ at its most pristine.
                    case 1:
                        Id = 32;
                        return false;
                    // $script:0905163707008901$
                    // - Show me $map:52000058$ when it's poisoned.
                    case 2:
                        Id = 33;
                        return false;
                    // $script:0905163707008902$
                    // - Bring me to $map:52000059$ during an eruption! 
                    case 3:
                        Id = 34;
                        return false;
                }
                return true;
            case 31:
                // $script:0905163707008903$ 
                // - If you've ever been to $map:63000044$, then you know that it was once a peaceful haven. The water was clean and clear, the fish flourished... My beloved hometown... 
                // $script:0905163707008904$ 
                // - I'm not sure why, but the water's become muddy and poisonous, and weird fish have started showing up. There was nothing we could do...   
                // $script:0905163707008905$ 
                // - Then, a little later, $map:63000044$ erupted into a giant volcano! Some folks thought it was a mermaid's curse, and others claimed that it was a government plot. Personally, I think the volcano was always there, sleeping... Waiting... 
                // $script:0905163707008906$ 
                // - Anyway, I can send you to any version of $map:63000044$ that you like. Whether you seek the pristine lake or a sea of molten lava... How can I do that? It's simple. 
                // $script:0905163707008907$ 
                // - But it's nearly time for my nap, so I won't go into the details now. Besides, what's the point of life without a bit of mystery?  
                return true;
            case 32:
                // $script:0905163707008908$ functionID=1 
                // - When it was clean and peaceful, huh? Well, guess what? I can send you back there if you want!  
                return true;
            case 33:
                // $script:0905163707008909$ functionID=2 
                // - When it was mysteriously contaminated, huh? Well, guess what? I can send you back there if you want!  
                return true;
            case 34:
                // $script:0905163707008910$ functionID=3 
                // - When it was covered in hot lava, huh? Well, guess what? I can send you back there if you want!  
                return true;
            case 40:
                // $script:0905163707008911$ 
                // - Have you ever been to $map:63000044$? It's quiet and empty... the perfect fishing spot! 
                switch (selection) {
                    // $script:0905163707008912$
                    // - How do I get there?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0905163707008913$ 
                // - You can go there after you finish the fishing quest in the Maple Guide. Every fisher should visit that place at least once in their life. 
                return true;
            default:
                return true;
        }
    }
}
