using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001554: Bory
/// </summary>
public class _11001554 : NpcScript {
    internal _11001554(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0415104107006020$ 
                // - What is it?
                return true;
            case 40:
                // $script:0421104907006043$ 
                // - I should've worn a wide-brimmed hat today. This sun is killing me.
                return true;
            default:
                return true;
        }
    }
}
