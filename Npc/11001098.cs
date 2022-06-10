using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001098: Moif
/// </summary>
public class _11001098 : NpcScript {
    internal _11001098(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003693$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407003696$ 
                // - Hey, hey! This place is dangerous. Get out of here! We don't need you fouling up any of the valves. 
                return true;
            default:
                return true;
        }
    }
}
