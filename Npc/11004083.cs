using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004083: Junjun
/// </summary>
public class _11004083 : NpcScript {
    internal _11004083(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010276$ 
                // - Hm... The schedule's tight, but we should be able to finish sector B today. 
                return true;
            case 10:
                // $script:0622133907010277$ 
                // - Hm... The schedule's tight, but we should be able to finish sector B today. 
                // $script:0622133907010278$ 
                // - Ah, a new face. What do you want? 
                switch (selection) {
                    // $script:0622133907010279$
                    // - What are you building here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0622133907010280$ 
                // - Ah, I see you've got an inquisitive mind. Good. I like it! 
                // $script:0622133907010281$ 
                // - We're building a geothermal plant here. Just you wait. In a few years' time, we'll be providing all the power to the nearby towns! 
                // $script:0622133907010282$ 
                // - The old... erm, tenants used this place to build a smelting furnace, but they didn't have the know-how to handle this much heat. 
                // $script:0622133907010283$ 
                // - Anyway, since this place is basically abandoned, we decided to take things over. If you want to lend a hand, we can always use another strong back or two! 
                return true;
            default:
                return true;
        }
    }
}
