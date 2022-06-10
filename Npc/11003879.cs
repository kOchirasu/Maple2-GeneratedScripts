using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003879: Antonius
/// </summary>
public class _11003879 : NpcScript {
    internal _11003879(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009874$ 
                // - Hm. Those weeds are an eyesore...
                return true;
            case 10:
                // $script:0417135107009875$ 
                // - Hm. Those weeds are an eyesore...
                return true;
            case 20:
                // $script:0419172107009858$ 
                // - I think you forgot to take the lunch box. Here is an empty one.
                return true;
            default:
                return true;
        }
    }
}
