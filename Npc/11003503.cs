using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003503: Ranshu
/// </summary>
public class _11003503 : NpcScript {
    internal _11003503(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115008986$ 
                // - What is it?
                return true;
            case 30:
                // $script:0816160115008987$ 
                // - The Team Mushroom has people all over the world. You'll find them wherever you find monsters!
                return true;
            case 40:
                // $script:0816160115008988$ 
                // - Team Mushroom and Dryad Co. don't have much in common. Dryad sells the tools of the pet-taming trade. Team Mushroom is working to protect the world from devastation, and unite all peoples across the nation!
                return true;
            case 50:
                // $script:0816160115008989$ 
                // - I work alone, but I'll be in need of a partner in the future.
                switch (selection) {
                    // $script:0816211715009063$
                    // - What about me?
                    case 0:
                        Id = 0; // TODO: 51,52 | 
                        return false;
                }
                return true;
            case 51:
                // $script:0816211715009064$ 
                // - Hey... Are you serious...?
                return true;
            case 52:
                // $script:0816211715009065$ 
                // - Not right now. But... maybe later.
                return true;
            default:
                return true;
        }
    }
}
