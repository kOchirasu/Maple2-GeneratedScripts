using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001889: Oska
/// </summary>
public class _11001889 : NpcScript {
    internal _11001889(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1027193507007342$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:1027193507007343$ 
                // - Thanks for all the hard work, $MyPCName$.  
                return true;
            default:
                return true;
        }
    }
}
