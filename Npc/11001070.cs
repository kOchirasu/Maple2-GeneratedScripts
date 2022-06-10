using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001070: Flan
/// </summary>
public class _11001070 : NpcScript {
    internal _11001070(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003647$ 
                // - Nice to meet you. 
                return true;
            case 30:
                // $script:0831180407003650$ 
                // - Do you know how rewarding it is to see the seeds you've sown grow into beautiful flowers? 
                return true;
            default:
                return true;
        }
    }
}
