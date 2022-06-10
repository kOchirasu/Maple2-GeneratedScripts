using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004176: Lennon
/// </summary>
public class _11004176 : NpcScript {
    internal _11004176(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010614$ 
                // - It's good to see you. 
                return true;
            case 10:
                // $script:0806025707010615$ 
                // - When things get dicey, it's good to have somebody who's got your back. 
                return true;
            default:
                return true;
        }
    }
}
