using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004561: Startz
/// </summary>
public class _11004561 : NpcScript {
    internal _11004561(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014508$ 
                // - Hey. 
                return true;
            case 10:
                // $script:0220211107014509$ 
                // - Hey. 
                // $script:0220211107014510$ 
                // - Didn't think I'd see you here. 
                switch (selection) {
                    // $script:0220211107014511$
                    // - Same.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014512$ 
                // - The Pink Beans dragged me out here to fight in their idiotic rumble. 
                // $script:0220211107014513$ 
                // - I don't know how they found out that I'm a decent fighter. What a hassle... 
                // $script:0220211107014514$ 
                // - If we end up facing off in the ring, I'll have to show you a thing or two. 
                return true;
            default:
                return true;
        }
    }
}
