using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001115: Mamida
/// </summary>
public class _11001115 : NpcScript {
    internal _11001115(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003742$ 
                // - Would you be so kind as to help me?
                return true;
            case 30:
                // $script:0908154107003745$ 
                // - Valle, where have you been? Ah... I don't think I know you. I'm sorry, I haven't been myself lately. I thought you were my daughter when I heard your footsteps. 
                return true;
            default:
                return true;
        }
    }
}
