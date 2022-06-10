using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003166: Joddy
/// </summary>
public class _11003166 : NpcScript {
    internal _11003166(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516084007008466$ 
                // - I sure hope $npcName:11003163[gender:0]$ comes back soon. 
                return true;
            case 30:
                // $script:0516084007008469$ 
                // - I hear $npcName:11003163[gender:0]$ is one of the most dutiful, most devoted, most loving sons in all of Maple World. 
                switch (selection) {
                    // $script:0516084007008470$
                    // - He's a devoted... son?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0516084007008471$ 
                // - Yeah! He's always off visiting his sick ma, who lives really far away. When I finally graduate, I'm gonna be a good son, too! 
                switch (selection) {
                    // $script:0516084007008472$
                    // - Why wait until then?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0516084007008473$ 
                // - If my mom and dad saw me the way I am now, they'd die of shame. Gotta prove myself, first! 
                return true;
            default:
                return true;
        }
    }
}
