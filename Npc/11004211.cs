using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004211: Pupu
/// </summary>
public class _11004211 : NpcScript {
    internal _11004211(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806052107010676$ 
                // - Yaaawn... 
                return true;
            case 10:
                // $script:0806052107010677$ 
                // - ♬I wanna be where the mushfolk are. I wanna see—wanna see 'em mushin'.
Bouncin' around on those stalks!♬ 
                return true;
            default:
                return true;
        }
    }
}
