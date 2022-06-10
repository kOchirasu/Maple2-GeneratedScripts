using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004131: Mysterious Voice
/// </summary>
public class _11004131 : NpcScript {
    internal _11004131(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010527$ 
                // - ...
                return true;
            case 10:
                // $script:0730132107010528$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
