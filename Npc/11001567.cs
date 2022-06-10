using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001567: Landevian
/// </summary>
public class _11001567 : NpcScript {
    internal _11001567(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006055$ 
                // - Ugh...  
                return true;
            case 10:
                // $script:0515180307006110$ 
                // - I'll be back on my feet... before you know it...  
                return true;
            case 20:
                // $script:0524142307006211$ 
                // - Don't worry about me... I'll be back on my feet in no time...  
                return true;
            default:
                return true;
        }
    }
}
