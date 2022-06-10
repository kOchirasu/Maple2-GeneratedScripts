using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001145: Juko
/// </summary>
public class _11001145 : NpcScript {
    internal _11001145(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0915220707003959$ 
                // - I'm confused... 
                return true;
            case 30:
                // $script:0915220707003962$ 
                // - Mmm... Do you like candy?
                switch (selection) {
                    // $script:0915220707003963$
                    // - No. I hate candy, because I am a monster.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0915220707003964$ 
                // - Whaaaat? I'm sure you'd change your mind if you tried my Mom's $item:30000395$. It's awesome!
                switch (selection) {
                    // $script:0915220707003965$
                    // - That's nice.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0915220707003966$ 
                // - <font color="#909090">(He whines pitifully)</font>
                //   Just try a piece! I promise you'll love it. My mom also bakes cakes and pies that are crazy good. She's like a <i>witch</i>!
                switch (selection) {
                    // $script:0915220707003967$
                    // - Anyone can bake.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0915220707003968$ 
                // - Not like my mom! When I grow up, I'm going to be a culinary wizard, and make snacks just as good as hers. 
                return true;
            default:
                return true;
        }
    }
}
