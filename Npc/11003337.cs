using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003337: Dark Wind Commander
/// </summary>
public class _11003337 : NpcScript {
    internal _11003337(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0510143807008461$ 
                // - I will protect the lives of my men... No matter what... 
                return true;
            case 10:
                // $script:0510145607008465$ 
                // - Dark Wind doesn't give up so easily! 
                return true;
            default:
                return true;
        }
    }
}
