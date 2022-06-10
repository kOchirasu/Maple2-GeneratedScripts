using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001336: Bodis
/// </summary>
public class _11001336 : NpcScript {
    internal _11001336(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005263$ 
                // - Someday we'll have a customer who returns their board... 
                return true;
            case 30:
                // $script:1217012607005266$ 
                // - Back in my day, we'd explore the whole world on our skateboards. I even shredded over the hot desert sands... Ah, those were good times. 
                return true;
            default:
                return true;
        }
    }
}
