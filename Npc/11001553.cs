using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001553: Lusoy
/// </summary>
public class _11001553 : NpcScript {
    internal _11001553(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0415104107006019$ 
                // - What brings you here? 
                return true;
            case 40:
                // $script:0421104907006039$ 
                // - Are you here to fish? This place is wonderful. I came here with my sister, Bory, and we're having a blast! 
                return true;
            default:
                return true;
        }
    }
}
