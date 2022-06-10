using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001538: Teresa
/// </summary>
public class _11001538 : NpcScript {
    internal _11001538(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0322222107005987$ 
                // - I didn't come all the way out here for nothing...
                return true;
            case 30:
                // $script:0329103507006004$ 
                // - I cannot help but sigh...
                //   <font color="#909090">She sighs.</font>
                return true;
            default:
                return true;
        }
    }
}
