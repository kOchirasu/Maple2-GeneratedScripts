using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003874: Miner
/// </summary>
public class _11003874 : NpcScript {
    internal _11003874(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009864$ 
                // - All this hard work is for my lovely wife and kid! Just wait a little longer, family! 
                return true;
            case 10:
                // $script:0417135107009865$ 
                // - Daddy's got to put food on the table. 
                return true;
            default:
                return true;
        }
    }
}
