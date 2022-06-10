using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003961: Heavy Gunner
/// </summary>
public class _11003961 : NpcScript {
    internal _11003961(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010013$ 
                // - Booooring.
                return true;
            case 20:
                // $script:0614143707010014$ 
                // - Do you want me to teach you about the immense power of the lapenshards? ...No? Pfft.
                return true;
            default:
                return true;
        }
    }
}
