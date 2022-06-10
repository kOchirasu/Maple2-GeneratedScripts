using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000265: Bordeaux
/// </summary>
public class _11000265 : NpcScript {
    internal _11000265(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001082$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0831180407001084$ 
                // - The secrets of the Land of Darkness and Shadow Word cannot be explained by logic. Nature was not created by mathematics or science. They have a life all their own, which must be understood.  
                return true;
            default:
                return true;
        }
    }
}
