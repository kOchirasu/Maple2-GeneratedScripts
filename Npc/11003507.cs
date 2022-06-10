using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003507: Karyan
/// </summary>
public class _11003507 : NpcScript {
    internal _11003507(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009007$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0816160115009008$ 
                // - I'm a member of Team Mushroom, but I'm also a freelance pet-tamer. 
                switch (selection) {
                    // $script:0816160115009009$
                    // - Can I hire you?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0816160115009010$ 
                // - Not now. I'm on vacation. 
                return true;
            case 40:
                // $script:0816211415009058$ 
                // - Apparently, Dryad Co. set their R&D department loose on monsters' tastebuds and developed these new monster candies. The $itemPlural:63000000$ are pretty popular. 
                switch (selection) {
                    // $script:0816211415009059$
                    // - Where can I get these monster candies?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0816211415009060$
                    // - Tell me about Dryad Co.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0816211415009061$ 
                // - Most major supply shops should carry $itemPlural:63000000$. I'm pretty sure $npcName:11003506[gender:1]$ has some in stock. 
                return true;
            case 42:
                // $script:0816211415009062$ 
                // - I don't really know much, myself. It's a tech giant with lots of next-gen products. Rumor has it one of the founders of Dryad Co. recently retired, but nobody really knows much about them, or even what they look like. 
                return true;
            default:
                return true;
        }
    }
}
