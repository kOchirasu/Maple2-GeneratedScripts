using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001457: Klay
/// </summary>
public class _11001457 : NpcScript {
    internal _11001457(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1222171407005458$ 
                // - Nice to meet you. 
                return true;
            case 30:
                // $script:1222171407005461$ 
                // - Coming here for my research is probably one of the best decisions I've ever made. I bet my wife and kid are happy, too. 
                return true;
            default:
                return true;
        }
    }
}
